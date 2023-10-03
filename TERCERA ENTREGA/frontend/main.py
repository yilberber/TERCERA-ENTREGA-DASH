import dash 
from dash import html,dcc
import dash_bootstrap_components as dbc

#importamos el frontend
from frontend.navegador.navegador import navegador
from frontend.derecho.derecho import derecho
from frontend.izquierdo.izquierdo import izquierdo

layout = dbc.Container([
    dbc.Row([
        dbc.Col(navegador,md=12),
        dbc.Col(izquierdo,md=8 , style={'background-color':'orange'}),
        dbc.Col(derecho,md=4 , style={'background-color':'silver'}),
    ])

])