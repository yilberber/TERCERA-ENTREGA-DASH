import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
#importamos el frontend
from frontend.main import layout
from backend.calculosondeos import clasificación_categorias
import math
import pandas as pd
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
                
app.layout = layout

@app.callback(
    Output('salidaCirculo', 'children'),
    Input('entradaCirculo', 'value'),
)
def areaCirculo(entradaCirculo):
    areaCirculo = math.pi * (entradaCirculo**2)
    return 'El área del circulo es: ' + str(areaCirculo)

if __name__ == '__main__' :
    app.run_server(debug=True)

niveles_construccion = (
    "Hasta 3 niveles",
    "Entre 4 y 10 niveles",
    "Entre 11 y 20 niveles",
    "Mayor de 20 niveles"
)

cargas_máximas=(
    "Menores de 800 kN",
    "Entre 801 y 4000 kN",
    "Entre 4001 y 8000 kN",
    "Mayores de 8000 kN"
)

categoría_construcción=(
    "Baja",
    "Media",
    "Alta",
    "Especial"
)
clasificación_categorias = pd.DataFrame ({
    "Niveles": niveles_construccion,
    "Cargas máximas": cargas_máximas,
    "Categoría": categoría_construcción
})