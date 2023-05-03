# Daily Temperature Forecast Using Recurrent Neural Networks

This project uses recurrent neural networks (RNNs) to predict daily temperatures based on historical weather data.

## Getting Started

### Prerequisites

To run the project, you need to have the following installed:

- Python 3
- Django
- Pandas
- TensorFlow

### Installing

1. Clone the project repository:

   ```
   git clone https://github.com/BetikuOluwatobi/Daily-Temperature-Forecast-Using-Recurrent-Neural-Networks.git
   ```

2. Install the project dependencies:

   ```
   pip install django pandas tensorflow
   ```

3. Run the project:

   ```
   python manage.py runserver
   ```

   This will start the Django development server. Navigate to "http://localhost:8000/" in a web browser to access the application.

### Development Process

Here are the steps involved in the development of the daily temperature forecasting model using RNN:

1. **Data Collection**: Historical weather data was collected from 2015-2019, including daily temperature readings and other relevant variables.

2. **Data Preprocessing**: The collected data was cleaned, preprocessed, and split into training and test sets.

3. **Model Selection**: A suitable RNN architecture (long short-term memory (LSTM)) was selected, and the hyperparameters of the model were configured.

4. **Model Training**: The RNN model was trained using the training set, adjusting the weights of the neural network to minimize the loss function.

5. **Model Evaluation**: The performance of the trained model was evaluated on the test set using the root mean squared error (RMSE) metric.

6. **Model Prediction**: The trained model was used to predict the daily temperature for future days.

7. **Model Refinement**: The model was refined by adjusting the hyperparameters, changing the architecture, or collecting more data, and the training and evaluation process was repeated.

## Running the Project in a Docker Container

1. Make sure Docker is installed on your system.

2. Build the Docker image:

   ```
   docker build -t daily_temp_forecast .
   ```

3. Run the Docker container:

   ```
   docker run -p 8000:8000 daily_temp_forecast
   ```

   Navigate to "http://localhost:8000/" in a web browser to access the application.

## Conclusion

This project demonstrates the use of recurrent neural networks to forecast daily temperatures based on historical weather data. By following the steps outlined in this README, you can run the project on your local machine or in a Docker container.
