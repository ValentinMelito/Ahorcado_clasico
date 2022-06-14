#juego ahorcado clasico

intentos=0
errores=0
paneo=0
respuesta= ""
vista=[]
lista=[]


palabra=input("ingrese una palabra: ")
lista=list(palabra)
vista=list(palabra)
muestra=len(lista)

#transformo la palabra en guiones para mostrarla al jugador
while (paneo<muestra):
  vista[paneo]="_"
  paneo+=1
#print("lo que vemos: ", vista)
print("")
print("---------------------")
print("     AHORCADO        ")
print("---------------------")
print("")

letras= list(respuesta)
#comparo hasta que sea igual la palabra
while (vista!=lista):
  print("errores: ", errores)
  respuesta=input("ingrese una letra: ")
  intentos+=1
  #solo dejo pasar 1 letra
  while (len(respuesta)>1 or len(respuesta)==0):
    print("ingrese UNA letra")
    respuesta=input("letra: ")
  #comparamos que la letra que elegimos no se repita 
  if respuesta in letras:
    print("su letra se repite elija otra palabra")
    print("estas letras se repitieron: ", letras)
    respuesta=input("letra: ")
  letras.append(respuesta)
  #print(letras)


  #comparamos que la letra que elegimos esta en la palabra
  if respuesta in lista:
    paneo=0
    print("se encuentra en la palabra")
    #va pasando la letra uno por uno hasta marcar todos los lugares donde esta
    while (paneo<muestra):
      #print(paneo)
      if (lista[paneo]==respuesta):
        vista[paneo]=respuesta
      paneo+=1
    print(vista)
    
  else:
    print("esa letra no se encuentra en la palabra")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    errores +=1
#le dejo 5 errores antes de que pierda
  if (errores>4):
      vista=lista
      print("---------------------")
      print("PERDIO MUCHOS INTENTOS  ")
      print("---------------------")
      print("la palabra era: ", vista)

if (errores<5):
  print("")
  print("----------------------")
  print("FELICIDADES USTED GANO")
  print("----------------------")   

print("se elijieron: ", intentos,  " palabras")
print("las elejidas fueron: ", letras)
print("")
