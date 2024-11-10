import sys
from streamlit.web import cli as stcli

sys.argv = ["streamlit", "run", "app.py"]# Escreva o seu código aqui :-)
sys.exit(stcli.main())
