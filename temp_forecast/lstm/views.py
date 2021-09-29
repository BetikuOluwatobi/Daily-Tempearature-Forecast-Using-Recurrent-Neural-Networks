from django.shortcuts import render
from .forms import ForecastForm,UploadFileForm
from .utils import RecurrentNetworks
import tensorflow as tf
import numpy as np
import pandas as pd
import os
from .utils import handle_uploaded_file
from django.conf import settings
from django.http import HttpResponse, Http404

# Create your views here.

def download(request):
    file_path = os.path.join(settings.STATICFILES_DIR, 'download.csv')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def multiforecast(request):
  forecast = False
  if request.method == 'POST':
      form = UploadFileForm(request.POST, request.FILES)
      if form.is_valid():
        handle_uploaded_file(request.FILES.get('upload_file'))
        data_path = os.path.join(settings.STATICFILES_DIR, 'file.csv')
        data =  pd.read_csv(data_path)
        model = RecurrentNetworks(0)
        series = model.process_data(data)
        forecast = model.model_multi_forecast(series)
        df = pd.Series(forecast,name='Temp')
        df.to_csv(os.path.join(settings.STATICFILES_DIR, 'download.csv'))
  else:
      form = UploadFileForm()
  return render(request, 'multi_forecast.html', {'form': form,'forecast':forecast})

def home(request):
  return render(request,'home.html')


def singleforecast(request):
  forecast = False
  if request.method == "POST":
    form = ForecastForm(request.POST)
    if form.is_valid():
      data = list(form.cleaned_data.values())
      model = RecurrentNetworks(0)
      forecast = str(round(model.model_forecast(data) + 5, 2)) + ' (°C)'
  else:
    form = ForecastForm()

  ctx = {'form': form,'forecast': forecast}
  return render(request,'forecast.html',ctx)
