python -m venv .venv
call .\.venv\Scripts\activate.bat
python -m pip install maturin
maturin init -b pyo3

