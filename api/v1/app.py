from fastapi import FastAPI


description = """
# Attribution

You are not required to provide attribution of any kind (other than specified by the license).
"""

app = FastAPI(
    title="Nekos API v1",
    description=description,
    version="0.1.0",
    license_info={
        "name": "MIT License",
        "url": 
    }
)

@app.get('/')
async def index():
    return {"message": "Welcome to the Nekos API!"}