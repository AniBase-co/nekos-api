import subprocess

# subprocess.run(
#     [
#         'python3', 
#         '-m', 
#         'gunicorn', 
#         'app:app', 
#         '--workers=4',
#         '--worker-class=uvicorn.workers.UvicornWorker',
#         '--bind=0.0.0.0:8000', 
#         '--reload'
#     ]
# )

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