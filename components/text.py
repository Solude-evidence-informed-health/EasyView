from dash import dcc

def generate_text_area(id_comp=''):
    return dcc.Input(id='input-epidemiology-text', type='text', placeholder='Digite o texto', className='input-epidemiology space-bottom')