from dash import callback, State, Input, Output, html, dcc
import dash_ag_grid as dag
import base64
import io
import pandas as pd
import plotly.express as px
from components import epidemiology_content as epc
from components import state_map as sm
from components import  ag_grid_table as agt
from components import title as t
from components import graph_bar as gb
from components import text as txt
from components import graph_pie as gp
from components import graph_scatter as gs


dict_options_url = {
    'table': 'assets/12.svg',
    'title': 'assets/17.svg',
    'text': 'assets/18.svg',
    'map_state': 'assets/14.svg',
    'bar': 'assets/13.svg',
    'pie': 'assets/16.svg',
    'scatter': 'assets/15.svg',
}

df = pd.DataFrame()

# @Callback that reads the excel file and displays it in a editable dash_ag_grid
@callback(
    [Output('content-placeholder', 'children'), Output('content-placeholder', 'style'), Output('upload-area-epidemiology', 'style'), Output('add-area', 'style')],
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename'), State('upload-data', 'last_modified')],
    [Input('upload-data-button', 'contents')],
    [State('upload-data-button', 'filename'), State('upload-data-button', 'last_modified')]
)
def update_output(contents, filename, date, contentsButton, filenameButton, dateButton):
    global df
    show_alert = False
    
    if contentsButton is not None:
        contents = contentsButton
        filename = filenameButton
        date = dateButton
        
    if contents is not None:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        try:
            if 'xlsx' in filename:
                df = pd.read_excel(io.BytesIO(decoded))
            elif 'xls' in filename:
                df = pd.read_excel(io.BytesIO(decoded))
            elif 'csv' in filename:
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        except Exception as e:
            print(e)
            return html.Div([
                'There was an error processing this file.'
            ])
        
        try:
            df_demo = pd.read_csv('data/DemografiaPI.csv', sep=',')
            df_demo.rename(columns={'CO_MUNICIPIO_GESTOR': 'GEOCODIGO'}, inplace=True)
            df = df.merge(df_demo, on='GEOCODIGO', how='outer')
            df['N DE CASOS'] = df['N DE CASOS'].fillna(0)
            df['TAXA DE INCIDENCIA'] = df.apply(lambda x: 0 if x['N DE CASOS'] == 0 else (x['N DE CASOS'] / x['PopulacaoEstimada_2021_']) * 100000, axis=1)
            df['TAXA DE INCIDENCIA'] = df['TAXA DE INCIDENCIA'].apply(lambda x: round(x, 2))
        except Exception as e:
            show_alert = True
        
        epc.update_layouts(t.generate_title_area(filename=filename))
        
        epc.update_layouts(epc.generate_basic_report(df, show_alert))
        
        return epc.generate_epidemiology_content(show_alert), {'display': 'block'}, {'display': 'none'}, {'display': 'block'}
    else:
        return html.Div(), {'display': 'none'}, {}, {'display': 'none'}
    
initial_n = 0

@callback(
    [Output('content-placeholder', 'children', allow_duplicate=True), Output("modal-add-content", "is_open", allow_duplicate=True)],
    [Input('add-content-ok', 'n_clicks'), Input('add-content-dropdown', 'value')],
    prevent_initial_call=True
)
def add_layout_content(n1, content):
    global df
    global initial_n
    if n1 > initial_n:
        initial_n = n1
        if content == 'table':
            epc.update_layouts(agt.generate_grid_table(df))
        elif content == 'map_state':
            epc.update_layouts(sm.generate_state_map(df))
        elif content == 'bar':
            print("inin")
            epc.update_layouts(gb.generate_graph_bar(df))
        elif content == 'pie':
            epc.update_layouts(gp.generate_graph_pie(df))
        elif content == 'scatter':
            epc.update_layouts(gs.generate_graph_scatter(df))
        elif content == 'title':
            epc.update_layouts(t.generate_title_area())
        elif content == 'text':
            epc.update_layouts(txt.generate_text_area())
        else:
            pass
        return epc.generate_epidemiology_content(), False
    
@callback(
    Output('content-image-placeholder', 'children'),
    Input('add-content-dropdown', 'value')
)
def update_image(selected):
    return html.Img(className='', src=dict_options_url.get(selected))

@callback(
    Output("dummy-download", "data"),
    Input("button-model-epidemiology", "n_clicks"),
    prevent_initial_call=True
)
def func(n_clicks):
    print("n_clicks: ", n_clicks)
    if n_clicks:
        excel_path = 'data/Planilha Epidemiologia Modelo.xlsx'
        return dcc.send_file(excel_path)

@callback(
Output("dummy-download", "data", allow_duplicate=True),
Input("button-model-epidemiology-aux", "n_clicks"),
prevent_initial_call=True
)
def func(n_clicks):
    print("n_clicks: ", n_clicks)
    if n_clicks:
        excel_path = 'data/Planilha Epidemiologia Auxiliar.xlsx'
        return dcc.send_file(excel_path)
    
@callback(
    Output("modal-alert", "is_open"),
    Input("close-alert", "n_clicks"),
    State("modal-alert", "is_open"),
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    return is_open