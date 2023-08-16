from dash import html, dcc

def generate_generic_content():
    layout = html.Div(
        id='content-area',
        className='box-content',
        children=[
            html.Div(children=[
                html.H3('Planilha', className='title-content'),
                html.Div(id='output-data-upload', className='content-data'),
                ],
                className='content'
            ),
            html.Div(children=[
                html.H3('Gráfico', className='title-content'),
                html.Div(id='output-data-upload2', className='content-control'),
                dcc.Graph(id='graph', className='content-data'),
                ],
                className='content'
            ),    
        ]
    )
    return layout