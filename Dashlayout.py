from dash import Dash,html,dcc

import Dashdropdown

def create_dash(app:Dash)-> html.Div:
    return html.Div(className='firstdive',children=[html.H1(app.title),html.Hr(),html.Div(className='dropdown', children=[Dashdropdown.render(app)] ) ] )