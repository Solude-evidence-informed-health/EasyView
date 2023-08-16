import pandas as pd
import geopandas as gpd
import plotly.express as px
from dash import dcc, html
from statistics import mean

df_cities = gpd.read_file('data/municipios.geojson')

def generate_state_map(df, column_cod='GEOCODIGO', tema='N DE CASOS', regions=False):
    
    df[column_cod] = df[column_cod].astype(float)
    
    global df_cities
    df_cities_copy = df_cities.copy()
    
    df_cities_copy['code_muni'] = df_cities_copy['code_muni'].astype(int)

    df_cities_copy['code_muni'] = df_cities_copy['code_muni'].astype(str)

    df_cities_copy['code_muni'] = df_cities_copy['code_muni'].str[:-1]

    df_cities_copy['code_muni'] = df_cities_copy['code_muni'].astype(float)

    
    df_cities_copy = df_cities_copy.loc[df_cities_copy['code_muni'].isin(list(df[column_cod]))]

    df_cities_copy = df_cities_copy.rename(columns={'code_muni': column_cod})

    df_cities_copy = pd.merge(df_cities_copy, df, how='left', on = column_cod)
    
    if regions:
        column_index = 'RegionaldeSaude'
        df_cities_copy = df_cities_copy.dissolve(by=column_index, aggfunc='sum')
        df_cities_copy = df_cities_copy.reset_index()
    else:
        column_index = 'name_muni'
    df_cities_copy.index = list(df_cities_copy[column_index])
    


    fig = px.choropleth_mapbox(
        df_cities_copy,
        geojson=df_cities_copy.geometry,
        locations=df_cities_copy.index,
        color=tema,
        color_continuous_scale="Spectral",
        opacity=0.6,
        center={"lat": (((mean(list(df_cities_copy.geometry.bounds.maxy))-mean(list(df_cities_copy.geometry.bounds.miny)))/2)+mean(list(df_cities_copy.geometry.bounds.miny)))
        , "lon": (((mean(list(df_cities_copy.geometry.bounds.maxx))-mean(list(df_cities_copy.geometry.bounds.minx)))/2)+mean(list(df_cities_copy.geometry.bounds.minx)))},
        labels={'index':'Município'},
        mapbox_style="open-street-map",
        zoom=5.2,
    )
    fig.update_layout(
        dragmode=False,
        margin=dict(l=1, r=1, t=1, b=1),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        )
    fig.update_coloraxes(colorbar_title='')
    
    map = html.Div(
        className='space-bottom',
        children=[
            dcc.Graph(figure=fig)
        ],
    )
    return map