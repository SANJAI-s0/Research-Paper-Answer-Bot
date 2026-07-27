import subprocess
import sys

subprocess.run(
    [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        "streamlit_app.py",
    ]
)
