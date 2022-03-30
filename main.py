from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

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
def get_pixels(picture: Picture_Info):
    return "The dimensions you sent are: "+picture.dimensions+".  The corners you sent are "+picture.corners
    # need to fix this later
    # in your picture class need to remember to convert the strings to tuple and list
    # need to also figure out how to send two strings, maybe you don't even need to picture info class.  Need to look into post on fast api


    # Python note from ast import literal_eval and use literal_eval to convert the strings 