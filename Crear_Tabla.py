import webbrowser

def genTabla(record):   
    cnt = 1

    name = ".\Documentacion\ADP_tabla"
    with open(name + ".html", "w") as f:
        f.write("<!DOCTYPE html>\n<html>\n<body style=\"text-align:center\">\n")
        f.write("\n<div><H1>Tabla de Iteraciones</H1></div>\n")

        f.write("<table><thead>")
        f.write("\n<tr><th>Iteraciones</th>\n<th>Pila <-</th>\n<th>Entrada</th>\n<th>Transiciones</th>\n</tr></thead>")
        for item in record:
            if(cnt == 0):
                f.write("\n<tr style=\"background-color:#d3d3d3\">")
                cnt = 1
            else:
                f.write("\n<tr>")
                cnt = 0
            f.write("\n\t<td>" + str(item[0]) + "</td>")
            f.write("\n\t<td style=\"text-align:right\">")
            string = ""
            for _ in item[1]:
                string += _
            string = string[::-1]
            f.write(string + "</td>\n\t<td>" + str(item[2]) + "</td>")
            f.write("\n\t<td>" + item[3] + "</td>")
            f.write("\n</tr>")
        f.write("</table>")
        f.write("\n</body>\n</html>")
        webbrowser.open(".\Documentacion\ADP_tabla.html")