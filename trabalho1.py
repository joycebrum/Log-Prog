#Trabalho de lógica em programação

#formato de entrada
# f -> string
# v -> map {"bola": true, "bala": false}
#valor("ola(tudo)bem",[1,2,3])

contador =0
mapa = []
funcao = ""

def valor(f, v):
    global funcao
    print(f)
    string2 = f
    funcao=f
    if(f) :
        formula = parse3(0)
        print(formula)
        # if formula 
    else :
        return;


def parse(funcaoR):
    global funcao
    global contador
    parseado = []
    for c in range(0,len(funcaoR)):
        
        print("c= ", funcaoR[c])
        print("funcao = ", funcao)
        print("função2 = ", funcaoR)
        print("parseado = ", parseado)
        print("")
        if funcaoR[c] == '(':
            subarray = parse(funcaoR[c+1:len(funcaoR)])
            pos=0
            for d in  range(c,len(funcaoR)):
                if(funcaoR[d] == ')'):
                   pos=d
                   break

            print("*********************************")
            print(funcaoR[c:pos+1])
            print("*"+str(contador))
            print("***********************************")
            funcao.replace(funcaoR[c:pos+1],"abc")
            print(funcao)
            contador = contador+1
            parseado.append(subarray)
        elif funcaoR[c] == ')':
            return parseado
            
        else:
            parseado.append(funcaoR[c])
    return parseado


def parse0(func, positionPai):
    global contador
    global funcao
    tamanhoString = len(func)
    
    for i in range( tamanhoString ):
        if(i>=tamanhoString):
            break
        if(funcao[i] == '(') :
            posicao = parse(funcao[i+1:len(func)], i) + i
            subString = funcao[i:posicao+1]
            mapa.append(subString)
            funcao = funcao[0:positionPai] + "*" + str(contador) + funcao[posicao+1:len(funcao)]
            contador=contador+1
            print(funcao)
            tamanhoString = len(funcao)
        elif(funcao[i] == ')') :
             return i +1
    return len(funcao)

def parse3(pos):
    global funcao
    global contador
    parseado = []
     
    for i in range( pos, len(funcao)):
        print("C= ", funcao[i])
        print("funcao= ", funcao)
        if(funcao[i] == '('):
            subarray = parse3(i+1)
            parseado.append(subarray)
        elif(funcao[i] == ')'):
            f=funcao
            f.replace(funcao[pos:i], "*" + str(contador))
            print("********************")
            print(f)
            return parseado
        else:
            parseado.append(funcao[i])
    return parseado
