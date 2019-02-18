import dash_html_components as html
import dash_core_components as dcc

# Visualization Layout
layout_visualization = html.Div([
    html.H3("Visualization"),
    # Element to output plotly chart
    dcc.Graph(id='output-data')
])
