# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 19:17:10 2022

@author: Eduardo
"""

from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json
import pandas as pd

#from fastapi.responses import StreamingResponse
#import io

import csv
import codecs


app = FastAPI()

#class file_input(BaseModel):
        
deser_model = pickle.load(open('modelo_desercion.sav','rb'))

@app.post('/csv')
async def root(file: UploadFile = File(...)):
    return{"file_name":file.filename}


@app.post("/upload")
def upload( file: UploadFile = File(...)):
    csvReader = csv.DictReader(codecs.iterdecode(file.file, 'latin-1'))
  
    return list(csvReader)

 


# deser_model.predict(list(csvReader))






    