from django.shortcuts import render
from .forms import ForecastForm
from .utils import RecurrentNetworks
import tensorflow as tf
import numpy as np
from django.conf import settings

# Create your views here.

def home(request):
  forecast = False
  if request.method == "POST":
    form = ForecastForm(request.POST)
    if form.is_valid():
      data = list(form.cleaned_data.values())
      model = RecurrentNetworks(settings.FILES_DIR,0)
      forecast = model.model_forecast(data)
  else:
    form = ForecastForm()

  ctx = {'form': form,'forecast': forecast}
  return render(request,'forecast.html',ctx)
