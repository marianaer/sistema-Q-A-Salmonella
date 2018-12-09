
# coding: utf-8

# In[136]:


import re#Importamos RE
import codecs #Importamos codecs para leer el archivo 

'''Llenamos la lista para la busqueda de las entidades '''
lista=[]#Lista en donde guardaremos  las entidades 
with codecs.open('/home/jwong/Escritorio/BioNLP/CM_Genes.txt','r', encoding='latin-1') as archivo:#Abrimos el primer archivo
    for line in archivo:#Iterando en cada linea
        line=line.split()#Spliteamos 
        lista.append(line[0])#Agregamos la entidad a la lista 

with codecs.open('/home/jwong/Escritorio/BioNLP/CM_Genes2.txt','r', encoding='latin-1') as archivo:#Abrimos el segundo archivo
    for line in archivo:#Iterando en cada linea
        line=line.split()#Spliteamos 
        lista.append(line[0])#Agregamos la entidad a la lista 

with codecs.open('/home/jwong/Escritorio/BioNLP/CM_NTL01ST_NTmisc_RNA0001.txt','r', encoding='latin-1') as archivo:#Abrimos el tercer archivo
    for line in archivo:#Iterando en cada linea
        line=line.split()#Spliteamos 
        lista.append(line[0])#Agregamos la entidad a la lista 
        
with codecs.open('/home/jwong/Escritorio/BioNLP/CM_sigma54.txt','r', encoding='latin-1') as archivo:#Abrimos el cuarto archivo
    for line in archivo:#Iterando en cada linea
        line=line.replace('\n','')
        lista.append(line)#Agregamos la entidad a la lista 

with codecs.open('/home/jwong/Escritorio/BioNLP/CM_sigma_54.txt','r', encoding='latin-1') as archivo:#Abrimos el quinto archivo
    for line in archivo:#Iterando en cada linea
        line=line.split()#Spliteamos 
        lista.append(line[0])#Agregamos la entidad a la lista 

#En este punto, la lista está completa 

salida=open('/home/jwong/Escritorio/BioNLP/Ult_Cuart_W1.0.txt','w')#Archivo de salida 
        
lista_anterior=[]#Lista en la que guardaremos la linea anterior del arcchivo, evitaremos repeticiones       
for line in codecs.open('/home/jwong/Escritorio/BioNLP/SalmUniqTrp.txt', encoding='latin-1'):#Abriendo archivo 
    line=line.split()#Spliteamos
    for i in lista:#Iteramos en cada item de la lista 
        if(i in line):#Si encontramos un match de la lista con la oraccion 
            if not (line==lista_anterior):#Y dicho match no es repeticion de la linea anterior 
                sent=str(line)#Lo transformamos a cadena + un tab
                sent=sent.replace('[','',100)#Limpiando los caracteres especiales de la lista que ahora estan en nuestra linea 
                sent=sent.replace(']','',100)
                sent=sent.replace(',','',100)
                sent=sent.replace('\'','',100)
                salida.write(sent+'\n')#Escribimos la linea en el archivo de salida
                lista_anterior=line#Ahora la linea actual sera la anterior
salida.close()#Cerramos archivo de salida 

