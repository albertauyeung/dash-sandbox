# -*- coding: utf-8 -*-
from dash import Dash, dcc, html
import time

from dash.dependencies import Input, Output

app = Dash(__name__)
server = app.server

options = [
    {'label': 'Option 1', 'value': 'opt1'},
    {'label': 'Option 2', 'value': 'opt2'},
    {'label': 'Option 3', 'value': 'opt3'}
]


app.layout = html.Div(
    children=[
        html.H3("Loading Example"),
        html.Div(
            [
                dcc.Dropdown(
                    id='dropdown',
                    options=options,
                    value='opt1'
                ),
                dcc.Loading(
                    id="loading",
                    children=[
                        html.Div([
                            html.Div(
                                id="loading-output",
                                style={"margin-top": "25px"}
                            )
                        ])
                    ],
                    type="graph",
                )
            ]
        ),
    ],
)


@app.callback(Output("loading-output", "children"), Input("dropdown", "value"))
def input_triggers_spinner(value):
    time.sleep(2)
    return value


if __name__ == "__main__":
    app.run_server(app)
