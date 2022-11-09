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

import csv
import codecs


app = FastAPI()


@app.post('/csv')


async def root(file: UploadFile = File(...)):
    return{"file_name":file.filename}


@app.post("/upload")
def upload(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    csvReader = csv.DictReader(codecs.iterdecode(file.file, 'latin-1'))
    background_tasks.add_task(file.file.close)
    return list(csvReader)

#prediccion = deser_model.predict([csvReader])






    