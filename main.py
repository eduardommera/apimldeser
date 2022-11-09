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


    
@app.post('/csv')


async def root(file: UploadFile = File(...)):
    return{"file_name":file.filename}



    ides= pd.read_csv(file,encoding='latin-1')
    ides.rename(columns = {'DescRIpcion Asignatura':'d_asignatura'}, inplace = True)
ides.rename(columns = {'DescRIpcionEstado':'estado'}, inplace = True)
ides.rename(columns = {'EstadoCalificacion':'e_calificacion'}, inplace = True)
ides.rename(columns = {'Nota':'nota'}, inplace = True)
ides.rename(columns = {'Genero':'genero'}, inplace = True)
ides.rename(columns = {'Fnacimiento':'Fnacimiento'}, inplace = True)
ides.rename(columns = {'Edad':'edad'}, inplace = True)
ides.rename(columns = {'Financiamiento':'financiamiento'}, inplace = True)
ides.rename(columns = {'Trabaja':'trabaja'}, inplace = True)
ides.rename(columns = {'Region':'region'}, inplace = True)
ides.rename(columns = {'colegio':'colegio'}, inplace = True)
ides.rename(columns = {'Nacionalidad':'nacionalidad'}, inplace = True)
ides.rename(columns = {'NivelEstudiosPadre':'nepadre'}, inplace = True)
ides.rename(columns = {'NivelEstudiosMadre':'nemadre'}, inplace = True)
ides.rename(columns = {'NEM':'nem'}, inplace = True)
ides.rename(columns = {'Region procedencia':'rprocedencia'}, inplace = True)
ides.rename(columns = {'Recidencia':'recidencia'}, inplace = True)
ides.rename(columns = {'Actividadesextracurriculares':'aextra'}, inplace = True)
ides.rename(columns = {'RamosReprobados':'rreprobados'}, inplace = True)
ides.rename(columns = {'Hijosdependientes':'hijos'}, inplace = True)
ides.rename(columns = {'Estadocivil':'ecivil'}, inplace = True)
ides.rename(columns = {'apoderado':'apoderado'}, inplace = True)
ides.rename(columns = {'hermanos':'hermanos'}, inplace = True)
ides.rename(columns = {'Jornadadeestudios':'horario'}, inplace = True)

ides=ides.replace(to_replace="NULL",value=0)
ides=ides.replace(to_replace="null",value=0)

ides.estado.fillna("Reprobado", inplace=True)
ides['genero'] =ides['genero'].map({'M':0,'F':1}).astype(int)
ides['d_asignatura'] =ides['d_asignatura'].map({'MATEMÁTICAS BÁSICAS':0,
                                                'COMUNICACIÓN ESCRITA':1,
                                                'CALCULO I':2,
                                                'INGENIERÍA DE SOFTWARE':3,
                                                'ADMINISTRACIÓN DE BASE DE DATOS':4,
                                                'PROGRAMACIÓN ORIENTADA A OBJETOS I(JAVA)':5,
                                                'MODELAMIENTO CON BUSINESS INTELLIGENCE':6,
                                                'DESIGN THINKING':7,
                                                'DESARROLLO SOFTWARE ESCRITORIO Y GESTIÓN':8,
                                                'DESARROLLO EN .NET':9,
                                                'SQL SERVER APLICADO':10,
                                                'PORTAFOLIO DE TÍTULO':11,
                                                'INGLES BASICO I':12,
                                                'ETICA':13,
                                                'PRINCIP.FE CRISTIANA':14,
                                                'ANTROPOLOGIA':15,
                                                'COMUNICACIÓN ORAL':16,
                                                'MODELAMIENTO DE PROCESOS DE NEGOCIOS':17,
                                                'INGLES BASICO II':18,
                                                'HABILIDADES BÁSICAS DE COMUNICACIÓN':19,
                                                'NIVELACIÓN MATEMÁTICA':20}).astype(int)
ides['estado'] =ides['estado'].map({'Reprobado':0,'Aprobado':1}).astype(int)
ides['e_calificacion'] =ides['e_calificacion'].map({'Asistencia':0,'Correcto':1}).astype(int)
ides['financiamiento'] =ides['financiamiento'].map({'Apoderado':0,'CAE':1,'Beca':2,'Propio':3,'Gratuidad':4}).astype(int)
ides['rprocedencia'] =ides['rprocedencia'].map({'Santiago':0,
                                                'LOS RÍOS':1,
                                               'LOS LAGOS':2,
                                               'COQUIMBO':3,
                                               'OHIGGINS':4,
                                               'VALPARAÍSO':5,
                                               'ÑUBLE':6,
                                               'MAULE':7,
                                               'ARAUCANÍA':8,
                                               'ATACAMA':9,
                                               'BIOBÍO':10,
                                               'ARICA Y PARINACOTA':11,
                                               'ANTOFAGASTA':12,
                                               }).astype(int)
ides['recidencia'] =ides['recidencia'].map({'Pedro Aguirre Cerda':0,
                                                'Quilicura':1,
                                               'Recoleta':2,
                                               'La Reina':3,
                                               'Cerro Navia':4,
                                               'Lo Prado':5,
                                               'Quinta Normal':6,
                                               'La Pintana':7,
                                               'Lo Barnechea':8,
                                               'El Bosque':9,
                                               'Providencia':10,
                                               'Santiago \xa0':11,
                                               '\xa0Conchalí':12,
                                                'San Ramón':13,
                                                'Macul':14,
                                                'La Florida':15,
                                                'Pudahuel':16,
                                                'Cerrillos':17,
                                                'Huechuraba':18,
                                                'Peñalolén':19,
                                                'La Cisterna':20,
                                                'Renca':21,
                                                'Estación Central':22,
                                                'Maipú':23,
                                                'San Miguel':24,
                                                'La Granja':25,
                                                'Lo Espejo':26,
                                                'Vitacura':27,
                                                'Ñuñoa':28,
                                                'Las Condes':29,
                                                'Independencia':30,
                                                'San Joaquín':31,
                                               }).astype(int)
ides['aextra'] =ides['aextra'].map({'Sin Actividad':0,
                                                'Pastoral':1,
                                               'Deportiva':2,
                                               }).astype(int)
ides['hijos'] =ides['hijos'].map({'sin hijos':0,
                                                'tiene hijos':1,
                                               }).astype(int)
ides['ecivil'] =ides['ecivil'].map({'divorciado':0,
                                    'soltero':1,
                                     'viudo':2,
                                     'casado':3,
                                               }).astype(int)
ides['apoderado'] =ides['apoderado'].map({'padres':0,
                                    'tercero':1,
                                     'propio':2,
                                               }).astype(int)
ides['horario'] =ides['horario'].map({'Diurno':0,
                                    'vespertino':1,
                                     'PEV':2,
                                               }).astype(int)
ides['trabaja'] =ides['trabaja'].map({'Cesante':0,
                                    'Dependiente':1,
                                     'Independiente':2,
                                               }).astype(int)
ides['region'] =ides['region'].map({'Santiago':0,
                                                'Regiones':1,
                                               }).astype(int)
ides['nacionalidad'] =ides['nacionalidad'].map({'Chileno':0,
                                                'Extranjero':1,
                                               }).astype(int)
ides['nepadre'] =ides['nepadre'].map({'Sin Estudios':0,
                                                'Basica':1,
                                      'Media':2,
                                      'Superior':3,
                                               }).astype(int)
ides['nemadre'] =ides['nemadre'].map({'Sin Estudios':0,
                                                'Basica':1,
                                      'Media':2,
                                      'Superior':3,
                                               }).astype(int)

ides = ides[['d_asignatura','estado','e_calificacion','nota','genero','edad','financiamiento','trabaja','region','nacionalidad',
              'nepadre','nemadre','nem','rprocedencia','recidencia','aextra','rreprobados','hijos','ecivil','apoderado','hermanos','horario']]
    


prediccion = deser_model.predict([ides])

ides['prediccion']=prediccion

ides.to_csv("your_preferred_name.csv")

    