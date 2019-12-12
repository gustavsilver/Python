# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:34:00 2019

@author: Gsilva
"""
import webbrowser
import time
import os
import glob
import pandas as pd

totalPausa= 1
contarPausa= 0

s1='466015'	
s2='465995'		
s3='465985'	
s4='465978'	
s5='465974'
s6='431717'
s7='431715'
s8='431498'

DIRa="https://www.onetecnyca.com/Sensor/ExportData?id="
DIRb="&uxExportAll=Sensor&Sensor_Name=on&Date=on&Value=on"


print ("inicio a las" + time.ctime())

while(contarPausa < totalPausa):
             
    webbrowser.open("https://www.onetecnyca.com")
    contarPausa =contarPausa+1


#-------------------limpiar descargas---------------
archivosBorrados = [] # a efecto de tener un reporte de qué se ha borrado

# se buscan todos los archivos ".flac" en el directorio objetivo
for archivo_csv in glob.glob('SensorHistory*.csv'): 
    archivosBorrados.append(archivo_csv) # opcional, es  para saber que se borrar
    os.unlink(archivo_csv)               # sólo se elimina una vez sino aparecerá error
    #os.remove(archivo_csv)              # también es válido

if archivosBorrados != []:
    print(archivosBorrados)
else:
    print('Ningun Archivo SensorHistory**.csv Borrado')    
# ------------------fin---limpiar descargas------------

    

webbrowser.open(DIRa + s1 + DIRb)
webbrowser.open(DIRa + s2 + DIRb)
webbrowser.open(DIRa + s3 + DIRb)
webbrowser.open(DIRa + s4 + DIRb)
webbrowser.open(DIRa + s5 + DIRb)
webbrowser.open(DIRa + s6 + DIRb)
webbrowser.open(DIRa + s7 + DIRb)
webbrowser.open(DIRa + s8 + DIRb)



time.sleep(1)


#df=pd.read_csv('SensorHistory.csv')
#print (df)
#SensorName=(df['SensorID'][1])
#print (SensorName)