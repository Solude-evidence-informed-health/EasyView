from dash import Dash, dcc, html
from components import header
import dash_bootstrap_components as dbc
from callbacks import app_c, home_c, epidemiology_c

app = Dash(__name__,
           meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}],
           title='EasyView',
           suppress_callback_exceptions=True,
           external_stylesheets=[dbc.themes.BOOTSTRAP],
           )
server = app.server

header_component = header.generate_header()

app.layout = html.Div(
    id='app-conteiner',
    children=[
        header_component,
        html.Div(
            children=[
                dcc.Location(id="url", refresh=False),
                html.Div(id="page-content")
            ],
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True,
                   host="0.0.0.0",
                   port=8050
    )