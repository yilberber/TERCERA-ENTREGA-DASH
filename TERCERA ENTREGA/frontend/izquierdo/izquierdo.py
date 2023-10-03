import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import geopandas as gpd
from dash import Dash, html,dcc, callback, Input, Output

izquierdo = dbc.Container(
    [
        html.H1('Nuevo Sondeo'),
        html.Hr(),
        html.Div([
        html.Label('Area del circulo'),
        dcc.Input(id = 'entradaCirculo', value = 5, type = 'number'),
        html.Label(id = 'salidaCirculo'),
        ]),

        html.Div([
                html.H2('Categoría del proyecto'),
                html.Label('Niveles de construcción '),
                dcc.Dropdown(
                    id = 'first dropdown',
                    options = [
                        {'label': 'Hasta 3 niveles', 'value': 'nv3'},
                        {'label': 'Entre 4 y 10 niveles', 'value': 'nv4'},
                        {'label': 'Entre 11 y 20 niveles', 'value': 'nv11'},
                        {'label': 'Mayor de 20 niveles', 'value': 'nv20'},
                    ],
                    value = 'nv3'
                ),
                
                html.Label('Cargas máximas de servicio en columnas'),
                dcc.Dropdown(
                    id = 'second dropdown',
                    options = [
                        {'label': 'Menores de 800 kN', 'value': 'M800'},
                        {'label': 'Entre 801 y 4000 kN', 'value': 'M801'},
                        {'label': 'Entre 4001 y 8000 kN', 'value': 'M4001'},
                        {'label': 'Mayores de 8000 kN', 'value': 'M8000'},
                    ],
                    value = 'M800'

                ) 

            ]
        ),




        

    ],
    style={'background-color':'orange'}
)

