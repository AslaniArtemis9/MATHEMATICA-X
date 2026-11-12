# MATHEMATICA X

An interactive educational laboratory combining symbolic mathematics, numerical analysis, orbital mechanics and 3D visualization.

## Features
- Safe AST-based symbolic expression parsing with SymPy (no Python evaluation).
- Symbolic differentiation and integration with support for selectable variables.
- Numerical derivatives, Simpson integration, bisection and Newton root finding.
- A Newtonian circular-orbit demonstration using velocity-Verlet integration, with input and stability checks.
- Interactive 3D mathematical surfaces with Plotly.
- Streamlit interface and automated tests with GitHub Actions.

## Requirements
Python 3.10 or newer.

## Run locally
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Run tests
```bash
python -m pytest -q
```

## Project structure
- `app.py`: Streamlit application.
- `mathematica_x/`: reusable mathematics and simulation modules.
- `tests/`: automated tests.

## Scientific scope
The orbit module is an educational Newtonian test-particle model around a fixed central mass. It does not model perturbations, atmospheric drag, relativistic effects, or full mutual two-body motion. Numerical accuracy depends on step size and the simulated duration.

## License
MIT. See [LICENSE](LICENSE).
