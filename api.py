from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services import get_magic_eden_collection_top_sales

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/get-top-sales/{time}&{minimum_sales}')
def top_sales(time: str, minimum_sales: str):
    """ time options: 10m, 1h.
        sales minimum: at least 30 to get good results.
    """
    data = get_magic_eden_collection_top_sales(time, minimum_sales)
    return data
