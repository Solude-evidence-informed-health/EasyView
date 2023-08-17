from dash import html, dcc
from components import title
import dash_bootstrap_components as dbc
from components import epidemiology_content as epc
from components import state_map as sm
from components import  ag_grid_table as agt
from components import title as t
from components import graph_bar as gb
from components import text as txt
from components import graph_pie as gp
from components import graph_scatter as gs
import geopandas as gpd

layouts = []

def reset_layouts():
    global layouts
    layouts = []

def update_layouts(item):
    global layouts
    layouts.append(item)
    
def generate_alert_modal():
    alert = dbc.Modal(
            [
                dbc.ModalHeader("Alerta"),
                dbc.ModalBody("O arquivo selecionado não está no formato correto, portanto podem haver funcionalidades desabilitadas."),
                dbc.ModalFooter(
                    dbc.Button("Compreendo", id="close-alert", className="ml-auto")
                ),
            ],
            id="modal-alert",
            centered=True,
            is_open=True,
        )
    layouts.append(alert)
    
def generate_basic_report(df, show_alert=False):
    if not show_alert:
        ag_grid = agt.generate_grid_table(df)
        state_map = sm.generate_state_map(df)
        graph_bar = gb.generate_graph_bar(df)
        
        state_map_reg = sm.generate_state_map(df, regions=True)

        graph_bar_reg = gb.generate_graph_bar(df, regions=True)
        
        #graph_pie = gp.generate_graph_pie(df)
        report = html.Div(
            id='report',
            className='',
            children=[
                dbc.Row([
                    html.H2('Visualização Geográfica', className='text-center', style={'width': '100%'}),
                    dbc.Col([
                        html.H4('Regional de Saúde', className='text-center', style={'width': '100%'}),
                        state_map_reg
                    ], width=6),
                    dbc.Col([
                        html.H4('Municípo', className='text-center', style={'width': '100%'}),
                        state_map
                    ], width=6)
                ], className='content'),
                dbc.Row([
                    html.H2('Ranking', className='text-center', style={'width': '100%'}),
                    dbc.Col([
                            html.H4('Regional de Saúde', className='text-center', style={'width': '100%'}),
                            graph_bar_reg
                    ], width=6),
                    dbc.Col([
                            html.H4('Município', className='text-center', style={'width': '100%'}),
                            graph_bar
                    ], width=6)
                ], className='content'),
                dbc.Row([
                    html.H2('Tabela', className='text-center', style={'width': '100%'}),
                    dbc.Col(ag_grid, width=12)
                ], className='content'),
            ],
        )
        return report

def generate_epidemiology_content(show_alert=False, filename=None):
    global layouts
    
    if show_alert:
        generate_alert_modal()
        
    layout = html.Div(
        id='epidemiology-content-area',
        children=layouts,
        )
    return layout