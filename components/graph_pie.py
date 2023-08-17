from dash import html, dcc
import plotly.express as px

def generate_graph_pie(df, tema='N DE CASOS', x='Municipio'):
    df = df.sort_values(by=tema, ascending=False)
    df = df.loc[df[tema] > 0]
    fig = px.pie(
        df,
        values=tema,
        names=x,
        color=x,
        color_continuous_scale="Spectral")
    
    pie = dcc.Graph(figure=fig)
    return pie