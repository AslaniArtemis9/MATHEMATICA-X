# MATHEMATICA X

An interactive educational laboratory combining symbolic mathematics, numerical analysis, orbital mechanics and 3D visualization.

## Features
- Symbolic differentiation and integration with SymPy.
- Numerical derivatives, Simpson integration, bisection and Newton root finding.
- A Newtonian circular-orbit demonstration using velocity-Verlet integration.
- Interactive 3D mathematical surfaces with Plotly.
- Streamlit interface and automated tests with GitHub Actions.

## Run locally
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Run tests
```bash
pytest -q
```

## Project structure
- `app.py`: Streamlit application.
- `mathematica_x/`: reusable mathematics and simulation modules.
- `tests/`: automated tests.

## Notes
This is an educational numerical model, not a precision astrodynamics package. The orbital simulation assumes a fixed central mass and a test particle.

## License
MIT. See [LICENSE](LICENSE).
