#Trabalho de lógica em programação

#formato de entrada
# f -> string
# v -> map {"bola": true, "bala": false}
#valor("ola(tudo)bem",[1,2,3])
#valor("!a | ( b & ! ( c -> d))",{'a':True, "b":False, "c":True, "d":True})
#valor("(a&(b|c)&(c))",{'a':True, "b":True, "c":False})

contador =0
mapa = {}
funcao = ""

def valor(f, v):
    global funcao
    global mapa
    string2 = f
    funcao=f
    mapa = v
    if(f) :
        formula = parse(0)
        print(formula)
        print(mapa)
        return execute(formula)
    else :
        return "erro, entrada inválida";


def parse(pos):
    global funcao
    global contador
    parseado = []
    i = pos
    #for i in range( pos, len(funcao)):
    while i < len(funcao):
        #print("C = " + funcao[i])
        #print(funcao)
        if funcao[i] == '*':
            while funcao[i] != ')':
                i = i + 1
        elif(funcao[i] == '('):
            subarray = parse(i+1)
            parseado.append(subarray)
        elif(funcao[i] == ')'):
            funcao = funcao.replace(funcao[pos:i], "*" + str(contador))
            return parseado
        elif funcao[i] == '-' and funcao[i+1] == '>':
            parseado.append("->")
            i = i + 1
        elif funcao[i] != ' ':
            parseado.append(funcao[i])
        i = i + 1
    return parseado

def execute(formula):
    global mapa
    if isinstance(formula, str):
        return mapa[formula]
    elif isinstance(formula, bool):
        return formula
    else:
        i = 0
        while i < len(formula):
            if formula[i] == '!':
                valor = execute(formula[i+1])
                formula.remove(formula[i+1])
                formula[i] = not valor
                i=i-1
            i = i+1
        i=0
        while i < len(formula) :
            if formula[i] == '&' or formula[i] == '|':
                
                valorEsquerdo = execute(formula[i-1])
                valorDireito = execute(formula[i+1])
                if formula[i] == '&':
                    formula[i] = valorEsquerdo and valorDireito
                else:
                    formula[i] = valorEsquerdo or valorDireito
                    
                formula.remove(formula[i+1])
                formula.remove(formula[i-1])
                i=i-2
            i = i + 1
        i = 0
        while i < len(formula) :
            if formula[i] == '->' :
                valorEsquerdo = execute(formula[i-1])
                valorDireito = execute(formula[i+1])
                formula[i] = (not valorEsquerdo) or valorDireito
                formula.remove(formula[i+1])
                formula.remove(formula[i-1])
                i=i-2
            i=i+1
        return execute(formula[0])
            
