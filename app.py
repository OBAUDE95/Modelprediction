import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash import Input, Output
import dash 
import plotly.graph_objs as go
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc,html
from dash import Output,Input
import pickle

# Define the list of columns for input
columns = ['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'who', 'adult_male', 'embark_town', 'alone']

# Load the model from the file
with open("first_model.pkl", 'rb') as model_file:
    loaded_model = pickle.load(model_file)

app = dash.Dash(external_stylesheets=[dbc.themes.YETI])

# Define the layout for the app
app.layout = dbc.Container([
    dbc.Card(id='card1', children=[
        dbc.CardHeader("Fill the data"),
        dbc.CardBody([dcc.Input(id=x, placeholder=x) for x in columns]),
    ]),
    dbc.Card(id='card2', children=[
        dbc.CardHeader("Prediction Result"),
        dbc.CardBody(id='result1'),
    ]),
])

# Define the callback to make predictions and update the result
@app.callback(Output('result1', 'children'), [Input(x, 'value') for x in columns])
def input_data_callback(*input_values):
    try:
        # Convert input values to a list of integers
        input_data = [int(val) for val in input_values]

        # Make predictions using the loaded model
        predictions = loaded_model.predict([input_data])

        # Map the predictions to user-friendly text
        result = 'This user will survive' if predictions[0] == 1 else 'This user will not survive'

        return result
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run_server(debug=True)
