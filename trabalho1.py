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
        formula = parse(string2, 0)
        #print(formula)
        # if formula 
    else :
        return;


def parse(funcao):
    parseado = []
    for c in range(len(funcao)):
        if funcao[i] == '(':
            subarray = parse(funcao[c:len(funcao)])
            parseado.append(subarray)
        elif funcao[i] == ')':
            
        else :
            parseado.append(c)


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


