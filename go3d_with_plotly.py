# import dependecies

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# source: https://archive.ics.uci.edu/ml/datasets/iris
iris = pd.read_csv('/path/to/data/iris.csv')

iris
# create 3d scatter plot, set fig size and title
fig = go.Figure(data=go.Scatter3d(
    x=iris['Species'],
    y=iris['SepalLengthCm'],
    z=iris['PetalLengthCm'],
    text='Species by Sepal and Petal Length',
    mode='markers',
    marker=dict(
        sizemode='diameter',
        size=iris['SepalLengthCm'],
        color=iris['PetalLengthCm'],
        colorscale='Viridis',
        colorbar_title='Sepal and Petal Length',
        line_color='rgb(140, 140, 170)'
    )
))

fig.update_layout(height=800, width=800,
                 title='Iris Scatterplot by Sepal and Petal Length')

fig.show()


# create 3d mesh plot, set fig size and title
fig = go.Figure(data=[go.Mesh3d(
    x=iris['SepalWidthCm'],
    y=iris['SepalLengthCm'],
    z=iris['PetalLengthCm'],
    opacity=0.5,
    colorscale='Cividis')])

fig.update_layout(height=600, 
                  width=600,
                  margin=dict(r=30, l=30, b=30, t=30),
                  title='Iris Meshplot by Sepal and Petal Length')

fig.show()
