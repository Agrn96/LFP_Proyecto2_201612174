from graphviz import Digraph
import webbrowser

class Gramatica:
    def __init__(self):
        self.nombre = []
        self.noTerminales = []
        self.terminales = []
        self.terminalesI = []
        self.stack = []

    def actualizar(self, nombre, noTer, ter, terI, stack):
        self.nombre = nombre
        self.noTerminales = noTer
        self.terminales = ter
        self.terminalesI = terI
        self.stack = stack

    def out(self, num):
        x = int(num)
        print("\nNombre de la gramatica tipo 2: ", end="")
        print(self.nombre[x])

        print("No terminales = { ", end="")
        for item in self.noTerminales[x]:
            print(item, end=" ")
        print("}")

        print("Terminales = { ", end="")
        for item in self.terminales[x]:
            print(item, end=" ")
        print("}")

        print("No terminal inicial = ", end="")
        print(self.terminalesI[x])

        print("Producciones: ", end="")
        for item in self.stack[x]:
            print("\n" + item[0] + " -> ", end="")
            skip = 0
            for _ in item:
                if(skip == 0):
                    skip+=1
                    continue
                print(_ + " ", end="")
        print("\n")
    
    def getGram(self, num):
        x = int(num)
        return self.nombre[x], self.noTerminales[x], self.terminales[x], self.terminalesI[x], self.stack[x]

    def genGram(self, num):
        dot = Digraph(comment='Grammmatica')
        dot.attr(rankdir='LR')

        dot.attr('node', shape='doublecircle')
        dot.node('f')

        dot.attr('node', shape='circle')
        dot.node('i')
        dot.node('p')
        dot.node('q')
        
        dot.edge('i','p','λ,λ;#')
        dot.edge('p','q','λ,λ;' + self.terminalesI[num])
        dot.edge('q','f','λ,#,λ')

        string = ""
        for item in self.stack[num]:
            x = 0
            for _ in item:
                if(x==0):
                    string += 'λ,' + _ + ';'
                    x+=1
                else:
                    string += _

            string += "\\n"
        dot.edge('q:n','q:n', string)

        string = ""
        for item in self.terminales[num]:
            string += item + "," + item + ";λ\\n"
        dot.edge('q:s','q:s', string)
        dot.render('.\Documentacion\Grafica.dot', format='png', view=False)

    def genHTML(self,num):
        self.genGram(num)
        name = ".\Documentacion\ADP"
        with open(name + ".html", "w") as f:
            f.write("<!DOCTYPE html>\n<html>\n<body style=\"text-align:center\">\n")
            f.write("\n<div><H1>" + self.nombre[num] + "</H1></div>\n")

            f.write("\n<br>Terminales={ ")
            for item in self.terminales[num]:
                if(item == self.terminales[num][-1]):
                    f.write(item + " }<br>")
                    break
                f.write(item + ",")

            f.write("\n<br>Alfabeto de pila={ ")
            for item in self.terminales[num]:
                f.write(item + ",")

            f.write(self.terminalesI[num] + ",")

            for item in self.noTerminales[num]:
                f.write(item + ",")
            f.write("# }<br>")

            f.write("Estados = { i,p,q,f }<br>\nEstado inicial = { i }<br>\nEstado de aceptacion = { f }<br><br><br>\n")
            f.write("<img src = \"Grafica.dot.png\">")
            f.write("\n</body>\n</html>")
            webbrowser.open(".\Documentacion\ADP.html")


    def genGram_(self, num, record, i):
        dot = Digraph(comment='Grammmatica')
        dot.attr(rankdir='LR')

        dot.attr('node', shape='plaintext')
        dot.node('name', "Gramatica: " +self.nombre[num])
        dot.node('it',"iteracion " + str(i))

        dot.attr('node', shape='record')
        temp = ""
        for item in record[1]:
            temp += item
        temp = temp[::-1]
        dot.node('P',"Pila: " + temp)
        dot.node('E',"Entrada: " + record[2])
        dot.node('tran',"Transicion: " + record[3])

        dot.attr('node', shape='doublecircle')
        dot.node('f')

        dot.attr('node', shape='circle')
        dot.node('i')
        dot.node('p')
        dot.node('q')
        
        dot.edge('i','p','λ,λ;#')
        dot.edge('p','q','λ,λ;' + self.terminalesI[num])
        dot.edge('q','f','λ,#,λ')

        string = ""
        for item in self.stack[num]:
            x = 0
            for _ in item:
                if(x==0):
                    string += 'λ,' + _ + ';'
                    x+=1
                else:
                    string += _

            string += "\\n"
        dot.edge('q:n','q:n', string)

        string = ""
        for item in self.terminales[num]:
            string += item + "," + item + ";λ\\n"
        dot.edge('q:s','q:s', string)
        name = ".\Documentacion\Grafica" + str(i) + ".dot"
        dot.render(name, format='png', view=False)