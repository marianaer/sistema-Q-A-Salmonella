
# coding: utf-8

# Buscando las las entidades en las tripletas, cada grupo por separado 

# In[25]:


###Sigma54###
import re#Importamos RE
lista=[]#Creamos una lista para la platilla actual 

with open('/home/jwong/Escritorio/BioNLP/CM_sigma54.txt','r') as plantilla:#Abrimos archivo plantilla 
    for line in plantilla:#Iteramos en cada linea 
        line=line.split()#Spliteamos 
        lista.append(line[0])#Añadimos la entidad a la lista 

salida=open('/home/jwong/Escritorio/BioNLP/Clasificacion_sigma54_W1.0.txt','w')#Archivo de salida

with open('/home/jwong/Escritorio/BioNLP/Salm_Inf_Lines_W1.0.txt','r') as archivo: #Cargamos el archivo en el que vamos a buscar
    lista_anterior=[]#Declaramos una lista vacia     
    for line in archivo:#Iteramos en cada linea del archivo 
        line=line.split()#Spliteamos, lo que ingresa a la linea a una lista 
        for i in lista:#Iteramos en cada item de la lista 
            if(i in line):#Si encontramos un match de la lista de entidades a buscar con la oraccion 
                if not (line==lista_anterior):#Y si esta linea no esta repetida
                    sent=str(line)#Lo transformamos a cadena 
                    sent=sent.replace('[','',100)#Limpiando los caracteres
                    sent=sent.replace(']','',100)
                    sent=sent.replace(',','',100)
                    sent=sent.replace('\'','',100)
                    salida.write(sent+'\n')#Lo escirbimos en el archivo de salida 
                    lista_anterior=line#Actualizamos la linea anterior para no tener repeticiones 
salida.close()#Cerrando archivo de salida


# In[24]:


###Sigma_54###
import re#Importamos RE
lista=[]#Creamos una lista para la platilla actual 

with open('/home/jwong/Escritorio/BioNLP/CM_sigma_54.txt','r') as plantilla:#Abrimos archivo plantilla 
    for line in plantilla:#Iteramos en cada linea 
        line=line.split()#Spliteamos 
        lista.append(line[0])#Añadimos la entidad a la lista 

salida=open('/home/jwong/Escritorio/BioNLP/Clasificacion_sigma_54_W1.0.txt','w')#Archivo de salida

with open('/home/jwong/Escritorio/BioNLP/Salm_Inf_Lines_W1.0.txt','r') as archivo: #Cargamos el archivo en el que vamos a buscar
    lista_anterior=[]#Declaramos una lista vacia     
    for line in archivo:#Iteramos en cada linea del archivo 
        line=line.split()#Spliteamos, lo que ingresa a la linea a una lista 
        for i in lista:#Iteramos en cada item de la lista 
            if(i in line):#Si encontramos un match de la lista de entidades a buscar con la oraccion 
                if not (line==lista_anterior):#Y si esta linea no esta repetida
                    sent=str(line)#Lo transformamos a cadena 
                    sent=sent.replace('[','',100)#Limpiando los caracteres
                    sent=sent.replace(']','',100)
                    sent=sent.replace(',','',100)
                    sent=sent.replace('\'','',100)
                    salida.write(sent+'\n')#Lo escirbimos en el archivo de salida 
                    lista_anterior=line#Actualizamos la linea anterior para no tener repeticiones 
salida.close()#Cerrando archivo de salida


# In[26]:


###NTL01ST_NTmisc_RNA0001###
import re#Importamos RE
lista=[]#Creamos una lista para la platilla actual 

with open('/home/jwong/Escritorio/BioNLP/CM_NTL01ST_NTmisc_RNA0001.txt','r') as plantilla:#Abrimos archivo plantilla 
    for line in plantilla:#Iteramos en cada linea 
        line=line.split()#Spliteamos 
        lista.append(line[0])#Añadimos la entidad a la lista 

salida=open('/home/jwong/Escritorio/BioNLP/Clasificacion_NTL01ST_NTmisc_RNA0001_W1.0.txt','w')#Archivo de salida

with open('/home/jwong/Escritorio/BioNLP/Salm_Inf_Lines_W1.0.txt','r') as archivo: #Cargamos el archivo en el que vamos a buscar
    lista_anterior=[]#Declaramos una lista vacia     
    for line in archivo:#Iteramos en cada linea del archivo 
        line=line.split()#Spliteamos, lo que ingresa a la linea a una lista 
        for i in lista:#Iteramos en cada item de la lista 
            if(i in line):#Si encontramos un match de la lista de entidades a buscar con la oraccion 
                if not (line==lista_anterior):#Y si esta linea no esta repetida
                    sent=str(line)#Lo transformamos a cadena 
                    sent=sent.replace('[','',100)#Limpiando los caracteres
                    sent=sent.replace(']','',100)
                    sent=sent.replace(',','',100)
                    sent=sent.replace('\'','',100)
                    salida.write(sent+'\n')#Lo escirbimos en el archivo de salida 
                    lista_anterior=line#Actualizamos la linea anterior para no tener repeticiones 
salida.close()#Cerrando archivo de salida


# In[27]:


###Genes 2###
import re#Importamos RE
lista=[]#Creamos una lista para la platilla actual 

with open('/home/jwong/Escritorio/BioNLP/CM_Genes2.txt','r') as plantilla:#Abrimos archivo plantilla 
    for line in plantilla:#Iteramos en cada linea 
        line=line.split()#Spliteamos 
        lista.append(line[0])#Añadimos la entidad a la lista 

salida=open('/home/jwong/Escritorio/BioNLP/Clasificacion_Genes2_W1.0.txt','w')#Archivo de salida

with open('/home/jwong/Escritorio/BioNLP/Salm_Inf_Lines_W1.0.txt','r') as archivo: #Cargamos el archivo en el que vamos a buscar
    lista_anterior=[]#Declaramos una lista vacia     
    for line in archivo:#Iteramos en cada linea del archivo 
        line=line.split()#Spliteamos, lo que ingresa a la linea a una lista 
        for i in lista:#Iteramos en cada item de la lista 
            if(i in line):#Si encontramos un match de la lista de entidades a buscar con la oraccion 
                if not (line==lista_anterior):#Y si esta linea no esta repetida
                    sent=str(line)#Lo transformamos a cadena 
                    sent=sent.replace('[','',100)#Limpiando los caracteres
                    sent=sent.replace(']','',100)
                    sent=sent.replace(',','',100)
                    sent=sent.replace('\'','',100)
                    salida.write(sent+'\n')#Lo escirbimos en el archivo de salida 
                    lista_anterior=line#Actualizamos la linea anterior para no tener repeticiones 
salida.close()#Cerrando archivo de salida


# In[28]:


###Genes###
import re#Importamos RE
lista=[]#Creamos una lista para la platilla actual 

with open('/home/jwong/Escritorio/BioNLP/CM_Genes.txt','r') as plantilla:#Abrimos archivo plantilla 
    for line in plantilla:#Iteramos en cada linea 
        line=line.split()#Spliteamos 
        lista.append(line[0])#Añadimos la entidad a la lista 

salida=open('/home/jwong/Escritorio/BioNLP/Clasificacion_Genes_W1.0.txt','w')#Archivo de salida

with open('/home/jwong/Escritorio/BioNLP/Salm_Inf_Lines_W1.0.txt','r') as archivo: #Cargamos el archivo en el que vamos a buscar
    lista_anterior=[]#Declaramos una lista vacia     
    for line in archivo:#Iteramos en cada linea del archivo 
        line=line.split()#Spliteamos, lo que ingresa a la linea a una lista 
        for i in lista:#Iteramos en cada item de la lista 
            if(i in line):#Si encontramos un match de la lista de entidades a buscar con la oraccion 
                if not (line==lista_anterior):#Y si esta linea no esta repetida
                    sent=str(line)#Lo transformamos a cadena 
                    sent=sent.replace('[','',100)#Limpiando los caracteres
                    sent=sent.replace(']','',100)
                    sent=sent.replace(',','',100)
                    sent=sent.replace('\'','',100)
                    salida.write(sent+'\n')#Lo escirbimos en el archivo de salida 
                    lista_anterior=line#Actualizamos la linea anterior para no tener repeticiones 
salida.close()#Cerrando archivo de salida


# Combinaremos los resultados obtenidos con una lista de verbos elegidos por el equipo, para remover tripletas no informativas. (La manera en que fueron escritos los verbos permite a RE encontrar varias formas del mismo)

# In[9]:


###Verbos_Sigma_54###
import re#Importamos RE
lista=['inhibit','repress','silenc','activat','initiat','bind','regulat']#Creamos una lista con los verbos que vamos a buscar

salida=open('/home/jwong/Escritorio/BioNLP/Verbos_sigma_54_W1.0.txt','w')#Archivo de salida

with open('/home/jwong/Escritorio/BioNLP/Clasificacion_sigma_54_W1.0.txt','r') as archivo: #Cargamos el archivo en el que vamos a buscar
    lista_anterior=[]#Declaramos una lista vacia     
    for line in archivo:#Iteramos en cada linea del archivo 
        for i in lista:#Iteramos en cada item de la lista 
            if(re.findall(i,line,flags=re.IGNORECASE)):#Si encontramos un match de la lista de entidades a buscar con la oraccion 
                if not (line==lista_anterior):#Y si esta linea no esta repetida
                    salida.write(line)#Lo escirbimos en el archivo de salida 
                    lista_anterior=line#Actualizamos la linea anterior para no tener repeticiones 
salida.close()#Cerrando archivo de salida


# In[10]:


###Verbos_Sigma54###
import re#Importamos RE
lista=['inhibit','repress','silenc','activat','initiat','bind','regulat']#Creamos una lista con los verbos que vamos a buscar

salida=open('/home/jwong/Escritorio/BioNLP/Verbos_sigma54_W1.0.txt','w')#Archivo de salida

with open('/home/jwong/Escritorio/BioNLP/Clasificacion_sigma54_W1.0.txt','r') as archivo: #Cargamos el archivo en el que vamos a buscar
    lista_anterior=[]#Declaramos una lista vacia     
    for line in archivo:#Iteramos en cada linea del archivo 
        for i in lista:#Iteramos en cada item de la lista 
            if(re.findall(i,line,flags=re.IGNORECASE)):#Si encontramos un match de la lista de entidades a buscar con la oraccion 
                if not (line==lista_anterior):#Y si esta linea no esta repetida
                    salida.write(line)#Lo escirbimos en el archivo de salida 
                    lista_anterior=line#Actualizamos la linea anterior para no tener repeticiones 
salida.close()#Cerrando archivo de salida


# In[11]:


###Verbos_NTL01ST_NTmisc_RNA0001###
import re#Importamos RE
lista=['inhibit','repress','silenc','activat','initiat','bind','regulat']#Creamos una lista con los verbos que vamos a buscar

salida=open('/home/jwong/Escritorio/BioNLP/Verbos_NTL01ST_NTmisc_RNA0001_W1.0.txt','w')#Archivo de salida

with open('/home/jwong/Escritorio/BioNLP/Clasificacion_NTL01ST_NTmisc_RNA0001_W1.0.txt','r') as archivo: #Cargamos el archivo en el que vamos a buscar
    lista_anterior=[]#Declaramos una lista vacia     
    for line in archivo:#Iteramos en cada linea del archivo 
        for i in lista:#Iteramos en cada item de la lista 
            if(re.findall(i,line,flags=re.IGNORECASE)):#Si encontramos un match de la lista de entidades a buscar con la oraccion 
                if not (line==lista_anterior):#Y si esta linea no esta repetida
                    salida.write(line)#Lo escirbimos en el archivo de salida 
                    lista_anterior=line#Actualizamos la linea anterior para no tener repeticiones 
salida.close()#Cerrando archivo de salida


# In[12]:


###Verbos_Genes###
import re#Importamos RE
lista=['inhibit','repress','silenc','activat','initiat','bind','regulat']#Creamos una lista con los verbos que vamos a buscar

salida=open('/home/jwong/Escritorio/BioNLP/Verbos_Genes_W1.0.txt','w')#Archivo de salida

with open('/home/jwong/Escritorio/BioNLP/Clasificacion_Genes_W1.0.txt','r') as archivo: #Cargamos el archivo en el que vamos a buscar
    lista_anterior=[]#Declaramos una lista vacia     
    for line in archivo:#Iteramos en cada linea del archivo 
        for i in lista:#Iteramos en cada item de la lista 
            if(re.findall(i,line,flags=re.IGNORECASE)):#Si encontramos un match de la lista de entidades a buscar con la oraccion 
                if not (line==lista_anterior):#Y si esta linea no esta repetida
                    salida.write(line)#Lo escirbimos en el archivo de salida 
                    lista_anterior=line#Actualizamos la linea anterior para no tener repeticiones 
salida.close()#Cerrando archivo de salida


# In[13]:


###Verbos_NTL01ST_NTmisc_RNA0001###
import re#Importamos RE
lista=['inhibit','repress','silenc','activat','initiat','bind','regulat']#Creamos una lista con los verbos que vamos a buscar

salida=open('/home/jwong/Escritorio/BioNLP/Verbos_Genes2_W1.0.txt','w')#Archivo de salida

with open('/home/jwong/Escritorio/BioNLP/Clasificacion_Genes2_W1.0.txt','r') as archivo: #Cargamos el archivo en el que vamos a buscar
    lista_anterior=[]#Declaramos una lista vacia     
    for line in archivo:#Iteramos en cada linea del archivo 
        for i in lista:#Iteramos en cada item de la lista 
            if(re.findall(i,line,flags=re.IGNORECASE)):#Si encontramos un match de la lista de entidades a buscar con la oraccion 
                if not (line==lista_anterior):#Y si esta linea no esta repetida
                    salida.write(line)#Lo escirbimos en el archivo de salida 
                    lista_anterior=line#Actualizamos la linea anterior para no tener repeticiones 
salida.close()#Cerrando archivo de salida


# Tendremos listas con los grupos de identidades asi como de los verbos, por separado

# In[18]:


#Cargamos los elementos de sigma54
lista_sigma54=[]
with open('/home/jwong/Escritorio/BioNLP/CM_sigma54.txt','r') as plantilla:#Abrimos archivo plantilla 
    for line in plantilla:#Iteramos en cada linea 
        line=line.split()#Spliteamos 
        lista_sigma54.append(line[0])#Añadimos la entidad a la lista 

#Cargamos los elementos de sigma_54
lista_sigma_54=[]
with open('/home/jwong/Escritorio/BioNLP/CM_sigma_54.txt','r') as plantilla:#Abrimos archivo plantilla 
    for line in plantilla:#Iteramos en cada linea 
        line=line.split()#Spliteamos 
        lista_sigma_54.append(line[0])#Añadimos la entidad a la lista 

#Cargamos los elementos de NTL01ST_NTmisc_RNA0001
lista_NTL01ST_NTmisc_RNA0001=[]
with open('/home/jwong/Escritorio/BioNLP/CM_NTL01ST_NTmisc_RNA0001.txt','r') as plantilla:#Abrimos archivo plantilla 
    for line in plantilla:#Iteramos en cada linea 
        line=line.split()#Spliteamos 
        lista_NTL01ST_NTmisc_RNA0001.append(line[0])#Añadimos la entidad a la lista

#Cargamos los elementps de Genes2
lista_genes2=[]
with open('/home/jwong/Escritorio/BioNLP/CM_Genes2.txt','r') as plantilla:#Abrimos archivo plantilla 
    for line in plantilla:#Iteramos en cada linea 
        line=line.split()#Spliteamos 
        lista_genes2.append(line[0])#Añadimos la entidad a la lista 

#Cargamos los elementos de Genes 
lista_genes=[]
with open('/home/jwong/Escritorio/BioNLP/CM_Genes.txt','r') as plantilla:#Abrimos archivo plantilla 
    for line in plantilla:#Iteramos en cada linea 
        line=line.split()#Spliteamos 
        lista_genes.append(line[0])#Añadimos la entidad a la lista 

#Lista de verbos
lista_verbos=['inhibit','repress','silenc','activat','initiat','bind','regulat']


# Buscarmos patrones de ExpReg en las oraciones para seguir filtrando la informacion

# In[52]:


#Cargamos los elementos de Genes 
lista_genes=[]
with open('/home/jwong/Escritorio/BioNLP/CM_Genes.txt','r') as plantilla:#Abrimos archivo plantilla 
    for line in plantilla:#Iteramos en cada linea 
        line=line.split()#Spliteamos 
        lista_genes.append(line[0])#Añadimos la entidad a la lista 
        
salida=open('/home/jwong/Escritorio/BioNLP/Verbos_Genes_RegExp_W1.0.txt','w')#Archivo de salida 

Ex_Reg_genes=[]#Lista con las expresiones regulares que vamos a buscar  
oracion1=str('by')+' '+i#ExpReg1
oracion2=i+' '+str('[a-z]+es')#ExpReg2
oracion3=i+' '+str('[a-z]{1,2}by')#ExpReg3
Ex_Reg_genes.append(oracion1)#Agregamos a la lista 
Ex_Reg_genes.append(oracion2)
Ex_Reg_genes.append(oracion3)

oracion_anterior=[]#Lista en donde guardaremos la oracion anterior para evitar repeticiones 
with open('/home/jwong/Escritorio/BioNLP/Verbos_Genes_W1.0.txt','r') as archivo:#Abrimos el archivo 
    for line in archivo:#Iteramos en cada linea 
        for i in Ex_Reg_genes:#Iteramos en la lista con las RegExp
            if(re.findall(i,line,flags=re.IGNORECASE)):#Si encuentra una de las expresiones regulares en la linea 
                if not(line==oracion_anterior):#Y si no es una repeticion de la oracion 
                    salida.write(line+'\n')#Se escribe en el archivo de salida 
                    oracion_anterior=line#La oracion actual ahora sera la anterior 
salida.close()#Cerramos archivo de salida 

