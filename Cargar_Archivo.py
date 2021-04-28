from Gramatica import Gramatica
from tkinter import *
from tkinter import filedialog
import codecs

def cargar_Archivo():
    """Funcion para abrir el archivo que se utiliza para la programa

    Args:
        lista (class): Listas para guardar informacion del archivo
    """
    try:
        gram = Gramatica()
        with codecs.open(filedialog.askopenfilename(filetypes=[("Text files","*.glc")]), encoding='utf-8') as filename:
            nombre, noTerminales, terminales, terminalesI, stack = adp(filename)
            gram.actualizar(nombre, noTerminales, terminales, terminalesI, stack)
        filename.close()
    except:
        print("Error con el seleccion del archivo")
    return gram

def adp(file):    
    nombre = []
    noTerminales = []
    terminales = []
    terminalesI = []
    stack = [[]]

    i = 0
    j = 0
    k = 0
    for line in file:
        if(j==0):
            temp = line.split('\n')
            temp[0].replace(" ","")
            nombre.append("AP_"+temp[0])
            j+=1
        elif(j==1):
            temp = line.split(';')
            temp1 = temp[0].split(',')
            noTerminales.append(temp1)
            temp2 = temp[1].split(',')
            terminales.append(temp2)
            terminalesI.append(temp[2][0])
            j+=1
        elif(j==2):
            if(line[0]=='*'):
                j=0
                i+=1
                k=0
                stack.append([])
                continue
            temp = line.split('->')
            stack[i].append([])
            temp[0] = temp[0].replace(" ","")
            stack[i][k].append(temp[0])
            temp1 = temp[1].split(' ')
            for item in temp1:
                if(item == " " or item == ""):
                    continue
                item.replace(" ","")
                hold = item.split('\r\n')
                hold[0].replace(" ","")
                stack[i][k].append(hold[0])
            k+=1
    stack.pop()
    return nombre, noTerminales, terminales, terminalesI, stack
