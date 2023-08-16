from dash import html, dcc
import plotly.express as px
import pandas as pd
import numpy as np

def generate_graph_bar(df, tema='N DE CASOS', x='Municipio', regions=False):

    if regions:
        x = 'RegionaldeSaude'
        df = df.groupby([x]).sum()
        df = df.reset_index()
    
    df = df.sort_values(by=tema, ascending=False)
    df = df.loc[df[tema] > 0]
    fig = px.bar(
        df,
        x=x,
        y=tema,
        color=tema,
        color_continuous_scale="Spectral")
    
    fig.update_coloraxes(colorbar_title='')
    
    bar = dcc.Graph(figure=fig)
    return bar