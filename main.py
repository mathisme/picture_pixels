from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from picture import Picture

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"],allow_credentials=True,
allow_methods=["*"],allow_headers=["*"])

class Picture_Info(BaseModel):
    dimensions: str
    corners: str

@app.get("/")
def read_root():
    return "Please send data as a POST request"


@app.post("/")
def get_pixels(picture_info: Picture_Info):
    picture = Picture(dims = picture_info.dimensions, corners=picture_info.corners)
    if not picture.valid_dimensions() or not picture.valid_corners():
        return "Please give valid data"
    return str(picture.get_pixels())
    #return "The dimensions you sent are: "+str(picture.dims)+".  The corners you sent are "+str(picture.corners)
    