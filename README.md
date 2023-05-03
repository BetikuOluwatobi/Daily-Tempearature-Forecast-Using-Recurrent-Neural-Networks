# Daily Temperature Forecasting Using Recurrent Neural Networks
<h3>Introduction</h3> 
The Daily-Temperature-Forecast-Using-Recurrent-Neural-Networks project is a weather forecasting application that uses recurrent neural networks (RNNs) to predict daily temperature based on historical weather data

## Steps
Here are the steps involved in the development of the daily temperature forecasting model using RNN:

* **Data Collection**: Historical weather data was collected from 2015-2019, including daily temperature readings and other relevant variables such as humidity, wind speed, dew point, and relative humidity.

* **Data Preprocessing**: The collected data was cleaned and preprocessed, including a function to load the dataset from Google Drive, merging the chunks of data into a larger DataFrame, converting the date/time column to a Python datetime data type, sorting rows by the date/time column, handling missing values, scaling the data, and splitting it into training and test sets.

* **Model Selection**: A suitable RNN architecture (long short-term memory (LSTM)) was selected, and the hyperparameters of the model were configured. Other models such as Gated Recurrent Unit (GRU) were also experimented with, but LSTM was found to work best.

* **Model Training**: The RNN model was trained using the training set, adjusting the weights of the neural network to minimize the loss function.

* **Model Evaluation**: The performance of the trained model was evaluated on the test set using the root mean squared error (RMSE) metric.

* **Model Prediction**: The trained model was used to predict the daily temperature for future days.

* **Model Refinement**: The model was refined by adjusting the hyperparameters, changing the architecture, or collecting more data, and the training and evaluation process was repeated.

Sure, here's an improved article on the steps for running the Daily-Temperature-Forecast-Using-Recurrent-Neural-Networks project:

## How to Run the Daily-Temperature-Forecast-Using-Recurrent-Neural-Networks Project on system

### Prerequisites

Before you can run the project, you need to make sure that you have the following installed on your system:

- Python 3
- Django
- Pandas
- TensorFlow

### Steps

### 1. Open the command prompt on your system. You can do this by searching for "command prompt" in the search bar and clicking on the result.

### 2. Create a virtual environment for the project by running the following command in the command prompt:

   ```
   python3 -m venv lstm_project
   ```

   This will create a virtual environment called "lstm_project" in the current directory.

### 3. Activate the virtual environment by running the following command in the command prompt:

   ```
   lstm_project\Scripts\activate
   ```

   This will activate the virtual environment and allow you to install the project dependencies without affecting the system-wide Python installation.

### 4. Clone the project repository by running the following command in the command prompt:

   ```
   git clone https://github.com/BetikuOluwatobi/Daily-Tempearature-Forecast-Using-Recurrent-Neural-Networks.git
   ```
### 5. Move into the Project Directory

Once you have cloned the project repository, you need to move into the project directory by running the following command in the Command Prompt:

```
cd Daily-Tempearature-Forecast-Using-Recurrent-Neural-Networks
```

This will move you into the project directory.

### 6. Move into the Django Project Directory

Inside the project directory, there is a Django project directory named "temp_forecast". Move into the Django project directory by running the following command in the Command Prompt:

```
cd temp_forecast
```

This will move you into the Django project directory.

### 7. Install Dependencies

Before running the project, you need to install all the dependencies required by the project. To do this, run the following commands in the Command Prompt:

```
pip install django
pip install pandas
pip install tensorflow
```

This will install Django, Pandas, and Tensorflow on your machine.

### 8. Check for Errors

To check if everything is working fine, run the following command in the Command Prompt:

```
python manage.py check
```

This will check for any errors in the project.

### 9. Run the Project

Finally, you can run the project by running the following command in the Command Prompt:

```
python manage.py runserver
```

This will start the Django development server, and you can access the project by opening a web browser and navigating to "http://localhost:8000/". You should see the Daily Temperature Forecasting application running.

Congratulations! You have successfully run the Daily Temperature Forecasting project on your local machine.



# Conclusion
In summary, this project developed a daily temperature forecasting model using recurrent neural networks, which involved data collection, preprocessing, model selection, training, evaluation, prediction, and refinement. With further refinement, this model could potentially be used in real-world weather forecasting applications.





