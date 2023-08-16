from dash import html, dcc

def generate_main_title():
    layout = html.Div(
                id='upload-area',
                className='box box-primary',
                children=[
                    html.H1(
                        id='upload-title',
                        children=['Visualize Dados com ',
                                html.Span('Facilidade', className='title-star'),
                                ' e ',
                                html.Span('Rapidez', className='title-star'),
                                ],
                        className='title title-primary',
                    ),
                    html.P(
                        id='upload-description',
                        children=['EasyView é a ferramenta que te permite visualizar seus dados de forma simples e rápida. Basta carregar um arquivo excel ou csv e começar a visualizar seus dados em diferentes tipos de gráficos.'],
                        className='description',
                    ),
                    html.Img(id='upload-image', src='assets/data-title.svg', className='image-title'),
                    dcc.Upload(
                        id='upload-data',
                        children=[
                            html.Img(className='upload-icon', src='assets/upload-icon.svg'),
                            html.A('Arraste e Solte ou Selecione uma Planilha', className='text')
                        ],
                        className='dropzone',
                        multiple=False
                    ),
                ]
            )
    return layout