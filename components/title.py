from dash import dcc

def generate_title_area(id_comp='', filename=None):
    return dcc.Input(id='input-epidemiology', type='text', placeholder=filename, className='input-epidemiology space-bottom')