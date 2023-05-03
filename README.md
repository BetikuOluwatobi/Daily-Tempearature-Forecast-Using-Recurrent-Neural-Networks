# Daily Temperature Forecasting Using Recurrent Neural Networks
<h2>Introduction</h2> <br>
Daily temperature forecasting using recurrent neural networks (RNNs) is a popular application of deep learning in weather forecasting. RNNs are particularly well-suited to this task because they can model the temporal dependencies between past and future weather conditions.

## Steps
Here are the steps involved in the development of the daily temperature forecasting model using RNN:

* **Data Collection**: Historical weather data was collected from 2015-2019, including daily temperature readings and other relevant variables such as humidity, wind speed, dew point, and relative humidity.

* **Data Preprocessing**: The collected data was cleaned and preprocessed, including a function to load the dataset from Google Drive, merging the chunks of data into a larger DataFrame, converting the date/time column to a Python datetime data type, sorting rows by the date/time column, handling missing values, scaling the data, and splitting it into training and test sets.

* **Model Selection**: A suitable RNN architecture (long short-term memory (LSTM)) was selected, and the hyperparameters of the model were configured. Other models such as Gated Recurrent Unit (GRU) were also experimented with, but LSTM was found to work best.

* **Model Training**: The RNN model was trained using the training set, adjusting the weights of the neural network to minimize the loss function.

* **Model Evaluation**: The performance of the trained model was evaluated on the test set using the root mean squared error (RMSE) metric.

* **Model Prediction**: The trained model was used to predict the daily temperature for future days.

* **Model Refinement**: The model was refined by adjusting the hyperparameters, changing the architecture, or collecting more data, and the training and evaluation process was repeated.

# Conclusion
In summary, this project developed a daily temperature forecasting model using recurrent neural networks, which involved data collection, preprocessing, model selection, training, evaluation, prediction, and refinement. With further refinement, this model could potentially be used in real-world weather forecasting applications.

## search for command prompt from the search bar
Open your command prompt 

## Create a virtual environment for the project
python3 -m venv lstm_project

## Activate virtual environment
lstm_project\Scripts\activate

## Paste the code in the opened command prompt
git clone https://github.com/BetikuOluwatobi/Daily-Tempearature-Forecast-Using-Recurrent-Neural-Networks.git 

## Move into the project directory
cd Daily-Tempearature-Forecast-Using-Recurrent-Neural-Networks

## move into django project directory
cd temp_forecast

## Install all dependencies for this project
pip install django
pip install pandas

### Make sure your system supports tensorflow or else you will get an error.
pip install tensorflow

## Check if there are no errors
python manage.py check 

## Copy the output and paste in browser to open application
python manage.py runserver


