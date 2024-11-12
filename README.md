
# Titanic Survival Prediction Dashboard

This is a Dash web application that predicts Titanic passenger survival based on user input. The model used for prediction is a pre-trained machine learning model, hosted on GitHub, which is loaded and used to make predictions based on specific input features.

## Features

- User-friendly interface built with [Dash](https://dash.plotly.com/) and [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/).
- Interactive form where users can input data to see if a passenger would survive the Titanic disaster.
- Uses a pre-trained model that predicts survival probability based on input features like age, fare, and embarkation town.

## Requirements

To run this app, you'll need the following Python libraries:
```bash
pip install dash dash-bootstrap-components plotly requests
```

## Setup

1. Clone the repository or copy the code to your project.
2. Download the model directly from GitHub as specified in the code or use your own model.

## How It Works

1. **Model Loading**: The app fetches a pre-trained model from a GitHub repository. Ensure that the model URL is accessible.
2. **User Inputs**: Users enter values for each of the features (e.g., `pclass`, `sex`, `age`) on a form.
3. **Prediction**: The app uses the input values to make a prediction based on the loaded model.
4. **Display Results**: The result indicates whether the input passenger would likely survive or not.

## Input Columns

The app expects inputs for the following features:

- `pclass`: Passenger class (1, 2, or 3)
- `sex`: Gender (encoded as binary values)
- `age`: Age of the passenger
- `sibsp`: Number of siblings/spouses aboard
- `parch`: Number of parents/children aboard
- `fare`: Ticket fare
- `who`: Indicates whether the passenger is a male, female, or child
- `adult_male`: Indicates if the passenger is an adult male
- `embark_town`: Town where the passenger boarded
- `alone`: Whether the passenger was traveling alone

## Running the App

To run the app, execute the following command:

```bash
python app.py
```

Then, navigate to `http://127.0.0.1:8050` in your browser to access the dashboard.

## Example Usage

1. Open the web app.
2. Enter data in each input field according to the expected feature values.
3. View the prediction result, which will indicate if the passenger would survive or not.

## File Structure

- `app.py`: The main application code that defines the layout, model loading, and prediction logic.

