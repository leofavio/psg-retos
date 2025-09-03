
luzSolar=eval(input()) 
humedad=int(input())    

activar=(luzSolar or humedad < 30)and not(luzSolar and humedad < 30)

mensajes=["El sistema de riego no se activa.","El sistema de riego se activa."]

print(mensajes[activar])
