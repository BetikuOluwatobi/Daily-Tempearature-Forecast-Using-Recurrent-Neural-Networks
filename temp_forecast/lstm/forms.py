from django import forms
import numpy as np

class ForecastForm(forms.Form):
  month = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','id': "formGroupExampleInput",'placeholder':'Enter your month...'}))
  day_of_month = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','id': "formGroupExampleInput",'placeholder':'Enter your day of the month...'}))
  dew_point = forms.FloatField(label='Dew Point Temp (°C)',max_value=10000, min_value=-9999999,widget=forms.NumberInput(attrs={'class': 'form-control','id': "formGroupExampleInput",'placeholder':'Enter your dew point...'}))
  relative_humidity = forms.FloatField(label='Rel Hum (%)',max_value=10000, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control','id': "formGroupExampleInput",'placeholder':'Enter your relative humidity...'}))
  wind_speed = forms.FloatField(label='Wind Spd (km/h)',max_value=10000, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control','id': "formGroupExampleInput",'placeholder':'Enter your wind speed...'}))
  stn_press = forms.FloatField(label='Stn Press (kPa)',max_value=10000, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control','id': "formGroupExampleInput",'placeholder':'Enter your Stn Pressure...'}))

class UploadFileForm(forms.Form):
  upload_file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class':"form-control",'id':"inputGroupFile01"}))
