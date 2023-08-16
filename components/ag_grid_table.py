from dash import html
import dash_ag_grid as dag

def generate_grid_table(df_in):
    grid = html.Div([
        dag.AgGrid(
            id='grid',
            columnDefs=[
                {'headerName': col, 'field': col, 'editable': True, 'sortable': True, 'filter': True} for col in df_in.columns
            ],
            rowData=df_in.to_dict('records'),
        ),
    ],
    className='space-bottom')
    return grid