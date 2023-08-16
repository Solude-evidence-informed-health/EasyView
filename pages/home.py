from dash import html, dcc
from components import main_title, generic_content

title = main_title.generate_main_title()
content = generic_content.generate_generic_content()

layout = html.Div(
    id='home',
    children=[
        title,
        content,
    ]
)
