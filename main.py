# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 19:17:10 2022

@author: Eduardo
"""

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json




app = FastAPI()


    
@app.post('/')


async def root(file: UploadFile = File(...)):
    return{"file_name":file.filename}

    


    
    
    
    
    
