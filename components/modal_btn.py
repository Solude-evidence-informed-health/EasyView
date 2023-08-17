from dash import html

def generate_modal_btn():
    btn = html.Button(
    id='add-content',
    className='btn btn-primary',
    children=[
        #html.Img(src='assets/add.svg', className=''),
        'Adicionar Conteúdo'
        ],
    #style={'display': 'none'}
    )
    return btn