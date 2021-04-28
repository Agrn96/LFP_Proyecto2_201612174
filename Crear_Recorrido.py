import webbrowser

def genRec(record, gram, num):

    name = ".\Documentacion\ADP_rec"
    with open(name + ".html", "w") as f:
        f.write("<!DOCTYPE html>\n<html>\n<body style=\"text-align:center\">\n")
        f.write("\n<div><H1>Recorridos</H1></div>\n")
        i=0
        for item in record:
            gram.genGram_(num, item, i)
            i+=1

        for j in range(i):
            f.write("<img src = \"Grafica" + str(j) +".dot.png\">")
        f.write("\n</body>\n</html>")
        webbrowser.open(".\Documentacion\ADP_rec.html")