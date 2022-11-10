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

 

@app.post("/upload2")
def upload( file: UploadFile = File(...)):
    csvReader = csv.DictReader(codecs.iterdecode(file.file, 'latin-1'))
  
    #return list(csvReader)
    input_parameters =list(csvReader)
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)    
    
    asig = input_dictionary['d_asignatura']
    est = input_dictionary['estado']
    califi = input_dictionary['e_calificacion']
    grade = input_dictionary['nota']
    gend = input_dictionary['genero']
    age = input_dictionary['edad']
    finan = input_dictionary['financiamiento']
    work = input_dictionary['trabaja']
    reg = input_dictionary['region']
    nacio = input_dictionary['nacionalidad']
    nepa = input_dictionary['nepadre']
    nema = input_dictionary['nemadre']
    nemscore = input_dictionary['nem']
    rproce = input_dictionary['rprocedencia']
    reci = input_dictionary['recidencia']
    actextra = input_dictionary['aextra']
    rreprob = input_dictionary['rreprobados']
    hijo = input_dictionary['hijos']
    ecivi = input_dictionary['ecivil']
    apode = input_dictionary['apoderado']
    herma = input_dictionary['hermanos']
    hora = input_dictionary['horario']
    
    
    input_list =[asig, est, califi, grade, gend, age, finan, work, reg, nacio, nepa, nema, nemscore, 
                 rproce, reci, actextra, rreprob, hijo, ecivi, apode, herma, hora]
    
    
    prediccion = deser_model.predict([input_list])
    
    
    return list(prediccion)



# deser_model.predict(list(csvReader))






    