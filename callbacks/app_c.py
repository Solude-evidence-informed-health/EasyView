from dash import callback, Input, Output, State
from pages import home, epidemiology
from components import epidemiology_content as epc

@callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/epidemiologia":
        epc.reset_layouts()
        return epidemiology.layout
    else:
        return "404"
    
@callback(Output("nav-bar", "children"), [Input("url", "pathname"), Input("nav-bar", "children")])
def update_nav_bar(pathname, children):
    if pathname == "/":
        children[0]["props"]["className"] = "nav-button active"
        children[1]["props"]["className"] = "nav-button"
    elif pathname == "/epidemiologia":
        children[0]["props"]["className"] = "nav-button"
        children[1]["props"]["className"] = "nav-button active"
    return children


@callback(
    Output("modal-add-content", "is_open"),
    Input("add-content", "n_clicks"),
    State("modal-add-content", "is_open"),
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    return is_open

