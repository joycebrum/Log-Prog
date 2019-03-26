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
    string2 = f
    funcao=f
    if(f) :
        formula = parse(0)
        print(formula)
        return execute(formula,v)
    else :
        return "erro, entrada inválida";


def parse(pos):
    global funcao
    global contador
    parseado = []
    i = pos
    #for i in range( pos, len(funcao)):
    while i < len(funcao):
        print("C = " + funcao[i])
        print(funcao)
        if funcao[i] == '*':
            while funcao[i] != ')':
                i = i + 1
            i = i + 1
            print("pulou para o char " + funcao[i])
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

def execute(formula, v):
    if isinstance(formula, list):
        i = 0
        while i < len(formula) :
            
            if formula[i] == '^' or formula[i] == 'v':
                valorEsquerdo = execute(formula[i-1], v)
                valorDireito = execute(formula[i+1], v)
                formula.remove(formula[i-1])
                formula.remove(formula[i+1])
                if element == '^':
                    formula[i] = valorEsquerdo and valorDireito
                else:
                    formula[i] = valorEsquerdo or valorDireito

            i = i + 1
    elif isinstance(formula, str):
        return v[formula]
    elif isinstance(formula, bool):
        return formula
    else:
        print("erro, formato invalido")
        return false
            
