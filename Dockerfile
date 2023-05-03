FROM python:3.10
WORKDIR /usr/src/app
RUN apt-get update && \
    apt-get -y install python3-pip && \
    apt-get install -y git
RUN pip install --upgrade pip
RUN python -m pip install django 
RUN python -m pip install tensorflow
RUN python -m pip install pandas
RUN git clone https://github.com/BetikuOluwatobi/Daily-Tempearature-Forecast-Using-Recurrent-Neural-Networks.git
WORKDIR ./Daily-Tempearature-Forecast-Using-Recurrent-Neural-Networks/temp_forecast/
EXPOSE 8000
ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]