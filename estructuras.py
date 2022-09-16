# cundicionales multiples
x=5
if 0<x:
    if x < 10:
         print("x es un numero positivo de un solo digito.") # no recomendable

if 0 < x and x < 10:
    print("es un numero positivo de un solo digito.") # recomendable

if 0 < x < 10:
    print("x es un numero positivo de un solo digito.")   # recomendable
             
            
# ejercicio
""""el profesor le indica a diego que durante el curso se sacaron cuatro notas y todas tienen el mismo valor,Ademas le solicita que debe elaborar un programa 
le ayude a calcular si aprobo o debe recuperar la materia no solo a el si no a todos sus compañeros para esto debe planificar correctamente un codigo en python 
que les ayude automizar esta nota.""""
nota1=2.9
nota2=3.8
nota3=3.0
nota4=3.5

promedio= round((nota1+nota2+nota3+nota4)/4,1)
#promedio(nota1+nota2+nota3+nota4)/4

if promedio >=3:
    print(f"su fue de{promedio},usted aprobo")
else:
    print(f"su fue de{promedio},usted reprobo")    