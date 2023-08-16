from dash import html, dcc
import plotly.express as px

def generate_graph_scatter(df, tema='N DE CASOS', x='Municipio'):
    df = df.sort_values(by=tema, ascending=False)
    df = df.loc[df[tema] > 0]
    fig = px.scatter(
        df,
        x=x,
        y=tema,
        color=tema,
        color_continuous_scale="Spectral")
    
    scatter = dcc.Graph(figure=fig)
    return scatter