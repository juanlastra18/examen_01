#coding=utf-8
#examen 1
#fumigacion en hogares


#Inicialización de la variable de control

roedores = 0
insectos = 0
hongos = 0

casas_fumigadas = 0
hogares = 12
print('programa de control de fumigacion')
print('que tipo de plaga desea fumigar : roedores/insectos/hongos)')
tipo_plaga = input('ingrese el tipo de plaga que desea fumigar: ')

while casas_fumigadas < hogares:
      tipo_plaga = input('ingrese el tipo de plaga que desea fumigar:( roedores/insectos/hongos): ')
      if tipo_plaga == roedores:
       casas_fumigadas += 1
       roedores += 1
      elif tipo_plaga == insectos:
        casas_fumigadas += 1
        insectos += 1
      elif tipo_plaga == hongos:
        casas_fumigadas += 1
        hongos += 1
      else:
        print('tipo de plaga no es valido')
     

print(f'el total de casas fumigadas es {casas_fumigadas}')     
print(f'el total casas fumigadas para roedores es {roedores}')
print(f'el total casas fumigadas para insectos es {insectos}')
print(f'el total casas fumigadas para hongos es {hongos}')
