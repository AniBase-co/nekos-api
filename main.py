import subprocess
subprocess.run(
    [
        'python3', 
        '-m', 
        'uvicorn', 
        'app:app', 
        '--host', 
        '0.0.0.0', 
        '--reload'
    ]
)