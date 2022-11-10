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

class model_input(BaseModel):
    d_asignatura :int
    estado :int
    e_calificacion :int
    nota :int
    genero :int
    edad :int
    financiamiento :int
    trabaja :int
    region :int
    nacionalidad :int
    nepadre :int
    nemadre :int
    nem :int
    rprocedencia :int
    recidencia :int
    aextra :int
    rreprobados :int
    hijos :int
    ecivil :int
    apoderado :int
    hermanos :int
    horario :int

#class file_input(BaseModel):
        
deser_model = pickle.load(open('modelo_desercion.sav','rb'))

@app.post('/csv')


async def root(file: UploadFile = File(...)):
    return{"file_name":file.filename}


@app.post("/upload")
def upload( file: UploadFile = File(...)):
    csvReader = csv.DictReader(codecs.iterdecode(file.file, 'latin-1'))
  
    #return list(csvReader)
    input_parameters =list(csvReader)
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)    

    prediccion = deser_model.predict([input_list])
    return {"prueba": prediccion}
 


# deser_model.predict(list(csvReader))






    