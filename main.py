from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from picture import Picture

app = FastAPI()

# This was added to avoid CORS errors
app.add_middleware(CORSMiddleware, allow_origins=["*"],allow_credentials=True,
allow_methods=["*"],allow_headers=["*"])

# the POST body will contain a json object with two strings, one being the dimensions and two the corner coordinates
# this class is created to save the POST body
class Picture_Info(BaseModel):
    dimensions: str
    corners: str

# as it was requested to be a POST request, any get request will return 'Please send data as a POST request'
@app.get("/")
def read_root():
    return "Please send data as a POST request"

# Here the POST request is handled, a picture instance is created, the dimensions and corner coordinates are validated, 
# finally the list of coordinates is calculated and returned. 
@app.post("/")
def get_pixels(picture_info: Picture_Info):
    picture = Picture(dims = picture_info.dimensions, corners=picture_info.corners)
    if not picture.valid_dimensions() or not picture.valid_corners():
        return "Please give valid data"
    return str(picture.get_pixels())

    