import numpy as np
from server import app
from dash.dependencies import Input, Output
import plotly.graph_objs as go

def _generate_chart(series):
    # Create a trace
    trace = go.Scatter(
        y = series
    )

    data = [trace]

    fig = {
        'data': data
    }
    return fig

@app.callback(Output('output-data', component_property='figure'),
              [Input('input-mean', 'value'),
              Input('input-stdv', 'value'),])
def update_visualization(mean, stdv):
    # Generates a random sample from a Normal Distribution
    time_series = np.random.normal(mean, stdv, 1000)
    # Generates a plotly chart
    chart_layout = _generate_chart(time_series)
    return chart_layout
