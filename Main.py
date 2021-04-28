from Crear_Recorrido import genRec
from Crear_Tabla import genTabla
from ADP import adp_auto
from Gramatica import Gramatica
from Cargar_Archivo import cargar_Archivo
import os

gram = Gramatica()
def main(): 
    """Mientras x != 6, el menu sigue apareciendo
    """     
    x = 0
    print("Alberto Gabriel Reyes Ning\n201612174")
    
    while(x != 6):
        print("\nMenu Principal")
        print("1. Cargar Archivo")
        print("2. Mostrar informacion general de la gramatica")
        print("3. Generar automata de pila equivalente")
        print("4. Reporte de recorrido")
        print("5. Reporte en tabla")
        print("6. Salir")
        print("Choose Menu Option: ", end="")
        try:
            x = int(input())                                #opcion del Menu
            os.system("cls")
            if(x==1):
                gram = cargar_Archivo()        #Llamada al Menu utilizando el input del usuario
            elif(x==2):
                i=0
                try:
                    for name in gram.nombre:
                        print(i, ". ", name)
                        i+=1
                except:
                    print("No hay Gramaticas cargados")
                    continue

                try:
                    print("Selecciona una gramatica: ", end="")
                    y = int(input())
                    os.system("cls")
                    gram.out(y)
                    os.system("pause")
                    os.system("cls")
                except:
                    print("Error con el seleccion del Gramatica")
            elif(x==3):
                i=0
                try:
                    for name in gram.nombre:
                        print(i, ". ", name)
                        i+=1
                except:
                    print("No hay Gramaticas cargados")
                    continue
                try:
                    print("Selecciona una gramatica: ", end="")
                    y = int(input())
                    os.system("cls")
                    gram.genHTML(y)
                except:
                    print("Error con el seleccion del Gramatica")
            elif(x==4):
                i=0
                try:
                    for name in gram.nombre:
                        print(i, ". ", name)
                        i+=1
                except:
                    print("No hay Gramaticas cargados")
                    continue
                
                try:
                    print("Selecciona una gramatica: ", end="")
                    y = int(input())
                    os.system("cls")
                    record = adp_auto(y, gram)
                    genRec(record, gram, y)
                except:
                    print("Error con el seleccion del Gramatica")
            elif(x==5):
                i=0
                try:
                    for name in gram.nombre:
                        print(i, ". ", name)
                        i+=1
                except:
                    print("No hay Gramaticas cargados")
                    continue
                try:
                    print("Selecciona una gramatica: ", end="")
                    y = int(input())
                    os.system("cls")
                    record = adp_auto(y, gram)
                    genTabla(record)
                except:
                    print("Error con el seleccion del Gramatica")
            elif(x==6):
                raise SystemExit(0)
            else:
                os.system("cls")
                print("Error en el seleccion del menu, numero no es valido")
        except:
            os.system("cls")
            print("Error en el seleccion del menu, digito no es valido")
main()