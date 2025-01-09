import threading

def Area(base, altura, figura):
  global areaTotal
  area = 0
#   print(f"Base:{base} \n altura:{altura} \n figura:{figura} \n ")
  
  if(figura == "triangulo" ):
      area = (base*altura)/2
      areaTotal += area
  else:
      area = base * altura
      areaTotal += area

figuras = [["triangulo",10,12],["cuadrilatero",12,8],["cuadrilatero",6,4],["triangulo",2,5]]

areaTotal=0
hilos = list()
for f in figuras: 
  t = threading.Thread(target=Area, args=(f[1],f[2],f[0]))
  hilos.append(t)
  t.start()

print (areaTotal)