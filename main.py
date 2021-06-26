import random, string

def clave_tarjeta(region):
  
  mayusculas=(string.ascii_uppercase)
  #se crea y se llena la tupla con el abecedario mayuscula ascii
  minusculas=(string.ascii_lowercase)
  #se crea y se llena la lista con el abecedario minuscula ascii
  numeros =(string.digits)
  #se crea y se llena la lista con los numeros del 0 al 9
     
  union=mayusculas+minusculas+numeros
  #se concatenan 3 tuplas y una lista
    
  clave=random.choices(union,k=20)
  #se seleccionan 20 caracteres aletorios de la lista union

  codigo_ver=list(clave[3]+clave[5]+clave[7])
  #se convierte los caracteres extraidos en una lista 
  clave=clave+codigo_ver
  #se concatenan los caracteres extraidos a la clave de 20 valores aletorios al final
  
  clave[9]=region[0]
  #se modifica el indice 9 de la clave por la primera letra de la region
  clave[11]=region[1]
  #se modifica el indice 11 de la clave por la primera letra de la region

  return clave

r_clave=clave_tarjeta("PUTUMAYO") # NO BORRAR 
print(r_clave)
