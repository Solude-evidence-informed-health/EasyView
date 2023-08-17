from dash import html, dcc

def generate_header():
    layout = html.Div(
        id='header',
        children=[
            html.A(
                id='product-name',
                children=[
                    html.Span('Solude ', className='product-name-1'),
                    html.Span('EasyView', className='product-name-2'),
                    ],
                href='https://www.s3biotech.com',
            ),
            html.Div(
                id="nav-bar",
                className="nav",
                children=[
                    html.A(
                        id='home-button',
                        className='nav-button',
                        children=['Genérico'],
                        href='/',
                    ),
                    html.A(
                        id='epidemiology-button',
                        className='nav-button',
                        children=['Epidemiologia'],
                        href='/epidemiologia',
                    ),
                ],
            ),
            dcc.Upload(
                id='upload-data-button',
                children=html.Button(
                    id='upload-button',
                    children=['Carregar Arquivo'],
                    className='btn btn-primary',
                ),
                multiple=False,
            ),
        ]
    )
    return layout