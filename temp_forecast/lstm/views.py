from django.shortcuts import render
from .forms import ForecastForm
from .utils import RecurrentNetworks
import tensorflow as tf
import numpy as np
# Create your views here.

def home(request):
  return render(request,'base.html')


def forecast(request):
  forecast = False
  if request.method == "POST":
    form = ForecastForm(request.POST)
    if form.is_valid():
      data = list(form.cleaned_data.values())
      model = RecurrentNetworks(0)
      forecast = model.model_forecast(data)
      print(forecast)
  else:
    form = ForecastForm()

  ctx = {'form': form,'forecast': forecast}
  return render(request,'forecast.html',ctx)
