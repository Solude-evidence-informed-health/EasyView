from dash import html, dcc
import dash_bootstrap_components as dbc
from components import epidemiology_title, epidemiology_content, modal, modal_btn, ag_grid_table

title = epidemiology_title.generate_epidemiology_title()
add_content_button = modal_btn.generate_modal_btn()
add_content_modal = modal.generate_modal()
report_button = html.Button(
    id='generate-report',
    className='btn btn-primary space-left',
    children=[
        "Gerar Relatório"
    ],
    disabled=True,
)

layout = html.Div(
    id='epidemiology',
    children=[
        title,
        dcc.Download(
            id='dummy-download',
        ),
        html.Div(
            id="content-placeholder",
            style={'display': 'none'},
        ),
        html.Div(
            id='add-area',
            children=[
                add_content_modal,
                html.Div(
                    id = 'btn-area',
                    children=[
                        add_content_button,
                        report_button,
                    ],
                ),
            ],
            style={'display': 'none'},
        ), 
    ]
)