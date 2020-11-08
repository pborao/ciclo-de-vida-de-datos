#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importamos los paquetes que necesitamos
import pandas as pd
#librería para http
import requests
# Para trabajar con archivos csv
import csv
# Librería para hacer web scraping
from bs4 import BeautifulSoup

#Inicializamos lista con los meses 
lista = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov"]
#Inicializamos con las columnas correspondientes a los datos que vamos a obtener
columnas = ['ID','Tipo','Coordenadas','Fecha','Hora','Magnitud','Distancia','Ubicacion','Pais']
#Creando el dataframe
df_new = pd.DataFrame(columns = columnas)
df = pd.DataFrame(columns = columnas)


# In[2]:


#Para cada uno de los meses
for x in range(0,len(lista)):
#Creamos la URL del mes y obtenemos el código HTML de ese mes 
    URL = 'https://www.volcanodiscovery.com/earthquakes/archive/2020-'+lista[x]+'.html'      
    page = requests.get(URL)
#Convertimos a objeto de la clase BeautifulSoup con el parseador a utilizar
    soup = BeautifulSoup(page.text, 'html.parser')
# Creamos una lista con los posibles valores que hemos identificado como diferentes tipos de seismo
    qi = ["q3","q4","q5","q6","q7","q8"]
# Iniciamos un bucle para cada uno de los qi
    for i in range(0,len(qi)):
# Obtenemos todos los elementos tr para la clase qi (de la iteración del bucle)
        q = soup.find_all('tr', class_=qi[i])
        nroFila=1
# Para cada fila encontrada, construimos los datos
        for job_elem in q: 
#Trabajamos el string para quedarnos con lo que nos interesa
            reportes_sismo = job_elem.find('a', class_='sl2')
            reportes_sismo = str(reportes_sismo).replace('<a class="sl2" href="','')
            reporte_id = reportes_sismo[23:30] 
            coordenadas_sismo = job_elem.find_all('a', href = True, title = True, onclick = True, style = False) 
            coordenadas_sismo = str(coordenadas_sismo).replace(' - Show on map">Map</a>]','')
            coordenadas_sismo = coordenadas_sismo.split('title="')[1]
            coordenadas_sismo = str(coordenadas_sismo).replace(' / ',',')
            names = []
            filas = []
#Recogemos toda la información y la formateamos con funciones de texto eliminando lo que no interesa como dato 
# Bucle para repasar todas las 'celdas' que contienen la información que queremos extraer.
            for celda in job_elem.find_all('td'):
                name=celda.text
                names.append(name)
            fechas_horas = names[0].split('UTC')
            fecha_hora = fechas_horas[0].split(' ')
#Dividmos en dos campos la fecha y la hora            
            fecha = fecha_hora[0]
            hora = fecha_hora[1]
#Formateamos la información de magnitud eliminando y troceando para quedarnos con los datos que interesan
            mags_dists = str(names[1]).replace(' - Info','')
            mags_dists = mags_dists.split(' / ')
            magnitud = str(mags_dists[0]).replace('M ','')
            if len(mags_dists) > 1:
                distancia = str(mags_dists[1]).replace(' km','')
            ubicaciones = str(names[3]).replace('I FELT IT ','')
            ubicaciones = ubicaciones.split(', ')
            ubicacion = ubicaciones[0]
            tipo = qi[i]
            if len(ubicaciones) > 1:
                paises = ubicaciones[1]
                paises = str(paises).replace(' report','')
                paises = str(paises).replace('s','')
            elif len(ubicaciones) > 2:
                region = ubicaciones[2]
            else:
                paises = ' '
#Incrementamos para pasar al siguiente tipo de 'q'        
            nroFila=nroFila+1
# Utilizamos el método append para añadir la información que hemos obtenido
            df=df.append({'ID': reporte_id,'Tipo': tipo, 'Coordenadas': coordenadas_sismo,'Fecha': fecha,'Hora': hora,'Magnitud': magnitud,
                              'Distancia': distancia,'Ubicacion': ubicacion,'Pais': paises} , ignore_index=True)
        df_new = pd.concat([df_new, df], ignore_index=True)


# In[3]:


#Una vez ya hemos iterado por todos los elementos de la lista (de todos los meses) escribimos en el fichero csv
df_new.to_csv('earthquakes.csv')

