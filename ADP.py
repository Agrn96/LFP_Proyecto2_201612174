
#add more record savings in non terminals 
def adp_auto(num, gram):
    nombre, noTerminal, terminal, termI, g = gram.getGram(num)
    term = set(terminal)
    noTerm = set(noTerminal)
    record = []
    print("\n\nIngresar una cadena: ", end="")
    cadena = input()
    cadena += "#"
    state = 'i'
    stack=[]
    string_len = len(cadena)

    iteracion = 0
    iterador = 0
    i=0
    try:
        while(iterador < (string_len)):
            current = cadena[iterador]
            current_ = None
            if(iterador != (string_len-1)):
                current_ = cadena[iterador+1]
            if(state=='i'):
                hold = stack.copy()
                record.append([iteracion, hold, current, "(i,$,$;p;#)"])
                iteracion+=1

                stack.append('#')
                state = 'p'
            elif(state=='p'):
                transicion = "(p,$,$;q;" + termI +")" 
                hold = stack.copy()
                record.append([iteracion, hold, current, transicion])
                iteracion+=1
                
                stack.append(termI)
                state='q'
            elif(state=='q'):
                if(stack[-1]==termI and iterador==0):   #Termino Inicial
                    transicion = "(q,$," + termI +";q,"
                    x=0
                    for item in g[i]:
                        if(x==0):
                            x+=1
                            continue
                        transicion += item + ","
                    transicion = transicion[:-1]
                    transicion += ")" 
                    hold = stack.copy()
                    record.append([iteracion, hold, current, transicion])
                    iteracion+=1

                    stack.pop()
                    random = g[i].copy()
                    random.reverse()
                    random.pop()
                    x=0
                    for item in random:
                        if(item == " " or item == ""):
                            continue
                        stack.append(item)
                    if((stack[-1] in noTerm) and stack[-1] != g[i][0]):
                        i += 1
                elif(stack[-1]=='#' and current == '#'):   #Fin del stack
                    hold = stack.copy()
                    record.append([iteracion, hold, current, "(q,$,#;f,$)" ])
                    iteracion += 1
                    stack.pop()
                    state = 'f'
                elif((stack[-1] in term) and (current == stack[-1])):   #Borrar Terminos
                    transicion = "(q," + stack[-1] + "," + stack[-1] + ";q,$)"
                    hold = stack.copy()
                    record.append([iteracion, hold, current, transicion])
                    iteracion += 1

                    stack.pop()
                    iterador+=1
                    current = cadena[iterador]
                    if((stack[-1] in term) or (stack[-1] == g[i][0])):
                        continue
                    else:
                        while((stack[-1] != g[i][0]) and (stack[-1] != '#')):
                            i+=1

                elif(stack[-1]==g[i][0]):       #Cambiar Non Terminales
                    if(current == g[i][1] or stack[-1] != g[i+1][0]):
                        transicion = "(q,$," + stack[-1] + ";q," 
                        x=0
                        for item in g[i]:
                            if(x==0):
                                x+=1
                                continue
                            transicion += item + ","
                        transicion = transicion[:-1]
                        transicion += ")" 

                        hold = stack.copy()
                        record.append([iteracion, hold, current, transicion])
                        iteracion += 1

                        stack.pop()
                        random = g[i].copy()
                        random.reverse()
                        random.pop()
                        x=0
                        for item in random:
                            if(item == " " or item == ""):
                                continue
                            stack.append(item)
                        while((stack[-1] in noTerm) and stack[-1] != g[i][0]):
                            i += 1
                    else:
                        
                        j = i + 1
                        while(stack[-1] == g[j][0]):
                            if(current == g[j][1]):
                                transicion = "(q,$," + stack[-1] + ";q," 
                                x=0
                                for item in g[j]:
                                    if(x==0):
                                        x+=1
                                        continue
                                    transicion += item + ","
                                transicion = transicion[:-1]
                                transicion += ")" 

                                hold = stack.copy()
                                record.append([iteracion, hold, current, transicion])
                                iteracion += 1

                                stack.pop()
                                random = g[j].copy()
                                random.reverse()
                                random.pop()
                                x=0
                                for item in random:
                                    if(item == " " or item == ""):
                                        continue
                                    stack.append(item)
                                while((stack[-1] in noTerm) and stack[-1] != g[i][0]):
                                    i += 1
                            else:
                                j+=1
                else:
                    hold = stack.copy()
                    record.append([iteracion, hold, current, "No Aceptado"])
                    break
            elif(state=='f'):
                record.append([iteracion, '$', '$', 'f'])
                break
    except:
        hold = stack.copy()
        record.append([iteracion, hold, current, "No Aceptado"])
    return record