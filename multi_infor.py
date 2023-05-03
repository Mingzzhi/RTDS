from dash import Dash, html, dcc,ctx,State,Output,Input




def B1info(dash,Stream):
    # @dash.callback(
    #     Output("B1dis",component_property='children'),
    #     Input(component_id="Timeforreal", component_property="n_intervals"),
    # )
    # def B1update(n):
    #     house=Stream.findhouse('B1')
    #     Pvalue="P1:"+  str( house.active[len(Stream.time)-1])+'kW'
    #     Qvalue ="Q1:"+ str(house.reactive[len(Stream.time) - 1])+'kVAR'
    #     Vvalue ="V1:"+str(house.voltage[len(Stream.time) - 1])+'V'
    #     return [html.H6(children=Pvalue,),
    #                                         html.H6(children=Qvalue),
    #                                         html.H6(children=Vvalue)]
    return html.Div( id= "B1dis", children=[html.H6(children="P1",),
                                            html.H6(children="Q1"),
                                            html.H6(children="V1")],style={'position': 'absolute','top': '600px', 'left': '830px','height':'30px','width':'50px'})








