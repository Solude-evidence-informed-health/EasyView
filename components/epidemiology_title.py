from dash import html, dcc
import dash_bootstrap_components as dbc

def generate_epidemiology_title():
    layout = html.Div(
                id='upload-area-epidemiology',
                className='box box-primary',
                children=[
                    html.H1(
                        id='upload-title',
                        children=['Visualize Dados ',
                                html.Span('Epidemiológicos', className='title-star'),
                                ' com ',
                                html.Span('Confiabilidade', className='title-star'),
                                ' e ',
                                html.Span('Rapidez', className='title-star'),
                                ],
                        className='title title-primary',
                    ),
                    html.Div(
                        className='column-description',
                        children=[
                            html.Div([
                                html.Img(id='sheet-main', src='assets/undraw_connected_world_wuay.svg', className='main-image'),
                            ], className='flex-big'),
                            html.Div([
                                html.P(
                                    id='upload-description',
                                    children=['EasyView é a ferramenta que te permite visualizar seus dados epidemiológicos em 3 simples passos.',
                                            html.Br(),
                                            html.Br(),
                                            html.Span('1. ', className='title-star bold'),
                                            'Baixe nosso modelo de planilha para a visualização de dados epidemiológicos, é necessário que o arquivo excel ou csv esteja no formato adequado.',
                                            html.Br(),
                                            html.Br(),
                                            html.Span('2. ', className='title-star bold'),
                                            'Preencha de acordo com seus dados.',
                                            html.Br(),
                                            html.Br(),
                                            html.Span('3. ', className='title-star bold'),
                                            'Realize o upload do arquivo final nesta página e visualize seus dados em diferentes tipos de gráficos.',
                                            html.Br(),
                                    ],
                                    className='description text-left text-less-larger',
                                ),
                                html.Div(
                                    className='row-div',
                                    children=[
                                        html.Button(
                                            id='button-model-epidemiology',
                                            children=[
                                                html.Img(src='assets/sheet_icon.svg', className='icon-image'),
                                                'Baixar Modelo'
                                            ],
                                            className='btn btn-secondary',
                                            n_clicks=0,
                                        ),
                                        html.Button(
                                            id='button-model-epidemiology-aux',
                                            children=[
                                                html.Img(src='assets/sheet_icon.svg', className='icon-image'),
                                                'Baixar Referências'
                                            ],
                                            className='btn btn-secondary space-left',
                                            n_clicks=0,
                                        ),
                                    ]
                                ),
                            ], className='flex-small'),
                        ],
                    ),
                    dcc.Upload(
                        id='upload-data',
                        children=[
                            html.Img(className='upload-icon', src='assets/upload-icon.svg'),
                            html.A('Arraste e Solte ou Selecione uma Planilha', className='text')
                        ],
                        className='dropzone',
                        multiple=False
                    ),
                ],
            )
    return layout