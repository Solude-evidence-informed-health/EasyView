from dash import callback, State, Input, Output, html, dcc
import dash_ag_grid as dag
import base64
import io
import pandas as pd
import plotly.express as px

# @Callback that reads the excel file and displays it in a editable dash_ag_grid
@callback(
    [Output('output-data-upload', 'children'), Output('content-area', 'style')],
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename'), State('upload-data', 'last_modified')],
    [Input('upload-data-button', 'contents')],
    [State('upload-data-button', 'filename'), State('upload-data-button', 'last_modified')]
)
def update_output(contents, filename, date, contentsButton, filenameButton, dateButton):
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
        grid = html.Div([
            dag.AgGrid(
                id='grid',
                columnDefs=[
                    {'headerName': col, 'field': col, 'editable': True, 'sortable': True, 'filter': True} for col in df.columns
                ],
                rowData=df.to_dict('records'),
            ),
        ])
        return grid, {'display': 'block'}
    else:
        return html.Div(), {'display': 'none'}

# @Callback that reads the dash ag grid and displays it in a graph with 2 dropdown menu to x axis and y axis to select columns and a third dropdown menu to select the type of graph
@callback(Output('output-data-upload2', 'children'),
                Input('grid', 'rowData'),
                Input('grid', 'columnDefs'))
def update_output2(rowData, columnDefs):
    if rowData is not None:
        df = pd.DataFrame(rowData)
        return html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value=df.columns[0]
            ),
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value=df.columns[1]
            ),
            dcc.Dropdown(
                id='graph-type',
                options=[{'label': i, 'value': i} for i in ['Scatter', 'Line', 'Bar']],
                value='Scatter'
            ),
        ])
    
# @Callback that reads the dash ag grid and displays it in a graph with 2 dropdown menu to x axis and y axis to select columns and a third dropdown menu to select the type of graph
@callback(Output('graph', 'figure'),
                Input('xaxis-column', 'value'),
                Input('yaxis-column', 'value'),
                Input('graph-type', 'value'),
                Input('grid', 'rowData'),
                Input('grid', 'columnDefs'))
def update_graph(xaxis_column_name, yaxis_column_name, graph_type, rowData, columnDefs):
    if rowData is not None:
        df = pd.DataFrame(rowData)
        if graph_type == 'Scatter':
            fig = px.scatter(x=df[xaxis_column_name], y=df[yaxis_column_name])
            fig.update_traces(mode='markers')
        elif graph_type == 'Line':
            fig = px.line(x=df[xaxis_column_name], y=df[yaxis_column_name])
            fig.update_traces(mode='lines')
        elif graph_type == 'Bar':
            fig = px.bar(x=df[xaxis_column_name], y=df[yaxis_column_name])
            fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
        fig.update_layout(transition_duration=500, title=f'{graph_type} Plot', xaxis_title=xaxis_column_name, yaxis_title=yaxis_column_name)
        return fig
