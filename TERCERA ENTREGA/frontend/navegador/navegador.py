import dash
import dash_bootstrap_components as dbc
from dash import html

navegador = dbc.Container([
    html.H2('Sondeo Civil Pro'),
    html.Hr(),
    html.H2('¿Quienes Somos?'),
    dbc.Row([
        dbc.Col(["la mejor app diseñada para simplificar y optimizar el proceso de determinar la cantidad de sondeos necesarios en proyectos de obras civiles"],md=12,style={'background-color':'white'}),
        dbc.Col(["Seleccione la siguiente información"],md=12,style={'background-color':'yellow'}),
    ])

])