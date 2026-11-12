import streamlit as st
import numpy as np
import plotly.graph_objects as go
from mathematica_x.symbolic import differentiate, integrate
from mathematica_x.numerical import bisection, newton, simpson
from mathematica_x.orbits import simulate_two_body
from mathematica_x.plotting import surface_figure

st.set_page_config(page_title="MATHEMATICA X", page_icon="∑", layout="wide")
st.title("∑ MATHEMATICA X")
st.caption("An interactive laboratory for symbolic mathematics, numerical methods and orbital mechanics.")
tab1, tab2, tab3 = st.tabs(["Symbolic mathematics", "Numerical methods", "Orbital mechanics"])
with tab1:
    expr = st.text_input("Expression", "sin(x)**2 + cos(x)**2")
    variable = st.text_input("Variable", "x", key="symbolic_variable")
    if st.button("Differentiate"):
        try: st.latex(differentiate(expr, variable))
        except Exception as exc: st.error(str(exc))
    if st.button("Integrate"):
        try: st.latex(integrate(expr, variable))
        except Exception as exc: st.error(str(exc))
with tab2:
    col1, col2 = st.columns(2)
    with col1:
        expr_n = st.text_input("f(x)", "x**2 - 2")
        a = st.number_input("Left endpoint", value=0.0)
        b = st.number_input("Right endpoint", value=2.0)
        if st.button("Find root (bisection)"):
            try: st.success(f"Root ≈ {bisection(expr_n, a, b):.10f}")
            except Exception as exc: st.error(str(exc))
    with col2:
        integ = st.text_input("Integrand", "sin(x)")
        lo = st.number_input("Integration start", value=0.0)
        hi = st.number_input("Integration end", value=float(np.pi))
        n = st.slider("Intervals", 10, 2000, 200, step=10)
        if st.button("Integrate numerically"):
            try: st.success(f"Integral ≈ {simpson(integ, lo, hi, n):.10f}")
            except Exception as exc: st.error(str(exc))
with tab3:
    mass = st.number_input("Central mass (kg)", value=5.972e24, format="%.3e")
    radius = st.number_input("Initial orbital radius (m)", value=7.0e6, format="%.3e")
    duration = st.number_input("Simulation duration (hours)", min_value=1.0, value=2.0)
    if st.button("Simulate orbit"):
        try:
            t, pos = simulate_two_body(mass, radius, duration * 3600)
            fig = go.Figure(data=[go.Scatter3d(x=pos[:,0], y=pos[:,1], z=pos[:,2], mode="lines", name="Orbit"),
                                  go.Scatter3d(x=[0], y=[0], z=[0], mode="markers", name="Central body")])
            fig.update_layout(scene_aspectmode="data", title="Two-body orbit")
            st.plotly_chart(fig, use_container_width=True)
        except Exception as exc: st.error(str(exc))
st.divider()
st.subheader("Explore a mathematical surface")
surface = st.selectbox("Surface", ["sin(sqrt(x²+y²))", "saddle: x²-y²", "radial: cos(r)"])
if st.button("Render surface"):
    st.plotly_chart(surface_figure(surface), use_container_width=True)
