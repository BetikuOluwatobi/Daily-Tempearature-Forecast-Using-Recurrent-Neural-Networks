from django import forms
import numpy as np

class ForecastForm(forms.Form):
  month = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','id': "formGroupExampleInput",'placeholder':'Enter your month...'}))
  day_of_month = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','id': "formGroupExampleInput",'placeholder':'Enter your day of the month...'}))
  dew_point = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','id': "formGroupExampleInput",'placeholder':'Enter your dew point...'}))
  stn_press = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','id': "formGroupExampleInput",'placeholder':'Enter your Stn Pressure...'}))
  wind_speed = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','id': "formGroupExampleInput",'placeholder':'Enter your wind speed...'}))
  relative_humidity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','id': "formGroupExampleInput",'placeholder':'Enter your relative humidity...'}))

  

