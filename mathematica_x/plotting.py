"""Plotly surface helpers."""
import numpy as np
import plotly.graph_objects as go

def surface_figure(kind="sin(sqrt(x²+y²))"):
    axis = np.linspace(-8, 8, 120)
    x, y = np.meshgrid(axis, axis)
    r = np.sqrt(x*x + y*y)
    if kind.startswith("saddle"): z = x*x - y*y
    elif kind.startswith("radial"): z = np.cos(r)
    else: z = np.sin(r)
    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale="Viridis")])
    fig.update_layout(title=kind, scene={"xaxis_title":"x", "yaxis_title":"y", "zaxis_title":"z"})
    return fig
