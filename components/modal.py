import dash_bootstrap_components as dbc
from dash import html, dcc

def generate_modal():
    modal = dbc.Modal(
            [
                dbc.ModalHeader(
                    dbc.ModalTitle("Escolha o conteúdo a ser adicionado"), 
                    close_button=True
                ),
                #"Aqui havera um dropdown com as opções de visualização"
                dbc.ModalBody(
                    [
                        dcc.Dropdown(
                            id='add-content-dropdown',
                            options=[
                                {'label': 'Tabela', 'value': 'table'},
                                {'label': 'Titulo', 'value': 'title'},
                                {'label': 'Texto', 'value': 'text'},
                                {'label': 'Mapa do Estado', 'value': 'map_state'},
                                {'label': 'Gráfico de Barras', 'value': 'bar'},
                                {'label': 'Gráfico de Pizza', 'value': 'pie', 'disabled': True},
                                {'label': 'Gráfico de Dispersão', 'value': 'scatter'},
                                {'label': 'Linha do Tempo', 'value': 'timeseries', 'disabled': True}
                            ],
                            value='bar',
                            placeholder="Selecione o tipo de conteúdo",
                        ),
                        html.Div(id="content-image-placeholder", style={'justify-content': 'center', 'display': 'flex', 'align-items': 'center', 'margin':'10px'}),
                    ]
                ),
                dbc.ModalFooter(
                    html.Button(
                        "Adicionar",
                        className="btn btn-primary",
                        id="add-content-ok",
                        n_clicks=0,
                    )
                ),
            ],
            id="modal-add-content",
            centered=True,
            is_open=False,
            backdrop=True,
        )
    return modal