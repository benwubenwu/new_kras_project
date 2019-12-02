import dash
import dash_core_components as dcc
import dash_html_components as html
# from ...models import Colon

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# control1 = Colon[1].control1
# control2 = Colon[1].control2
# control3 = Colon[1].control3
# control4 = Colon[1].control4
# control5 = Colon[1].control5

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5],
                    'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
