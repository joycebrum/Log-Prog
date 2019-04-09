'''
Feito por Joyce Brum e Thiago Outeiro
formato de entrada:
    estados -> array de strings, onde cada string representa o nome de um estado
    relacoes -> mapa onde as chaves sao um estado e o valor associado é um array de estados
                aos quais a chave possui uma ligação
    valoracao -> mapa onde as chaves são as variáveis e os valores associados a elas são um
                array de estados nos quais a variavel é verdadeira
    f -> string
'''

import constant

contador =0
funcao = ""

#W, R, V já com um caso de teste preenchido
W = ["w1", "w2", "w3"]

R = {"w1": ["w2", "w3"], "w2": ["w3"], "w3": ["w2"]}

V = {"p": ["w1", "w2"], "q": ["w2", "w3"], "r": ["w3"]}

def valor(estados, relacoes, valoracao, estado, f):
    global W, R, V, funcao
    W, R, V, funcao = estados, relacoes, valoracao, f
    mapa = montaValoracaoLocal(estado)
    if(f) :
        formula = parse(0)
        print(formula)
        return execute(estado, formula, mapa)
    else :
        return "erro, entrada inválida";

def transformaFormula(f):
    global funcao
    funcao = f
    if f:
        return parse(0)
    return []

def parse(pos):
    global funcao
    global contador
    parseado = []
    i = pos
    #for i in range( pos, len(funcao)):
    variavel = ""
    while i < len(funcao):
        #print("C = " + funcao[i])
        #print(funcao)
        if funcao[i] == '*':
            while funcao[i] != ')':
                i = i + 1
        elif(funcao[i] == '('):
            if len(variavel) > 0:
                parseado.append(variavel)
                variavel = ""
            subarray = parse(i+1)
            parseado.append(subarray)
        elif(funcao[i] == ')'):
            if len(variavel) > 0:
                parseado.append(variavel)
                variavel = ""
            funcao = funcao.replace(funcao[pos:i], "*" + str(contador))
            return parseado
        elif i+1 < len(funcao) and(funcao[i] + funcao[i+1]) == constant.IMPLICACAO:
            if len(variavel) > 0:
                parseado.append(variavel)
                variavel = ""
            parseado.append(constant.IMPLICACAO)
            i = i + 1
        elif funcao[i] == constant.AND or funcao[i] == constant.OR or funcao[i]== constant.NOT or funcao[i]==constant.PARATODO or funcao[i]==constant.ALGUM :
            if len(variavel) > 0:
                parseado.append(variavel)
                variavel = ""
            parseado.append(funcao[i])
            
        elif funcao[i] == ' ':
            if len(variavel) > 0:
                parseado.append(variavel)
                variavel = ""
        else :
            variavel += funcao[i]
        i = i + 1
    if len(variavel) > 0:
        parseado.append(variavel)
    return parseado

def execute(estado, formula, mapa):
    if isinstance(formula, str):
        return mapa[formula]
    elif isinstance(formula, bool):
        return formula
    else:
        i = 0
        while i < len(formula):
            if formula[i] == constant.NOT:
                valor = execute(estado, formula[i+1], mapa)
                formula.remove(formula[i+1])
                formula[i] = not valor
            else :
                i = i + 1
        i=0
        while i < len(formula):
            if formula[i] == constant.PARATODO:
                valor = paraTodoVizinho(estado, formula[i+1])
                formula.remove(formula[i+1])
                formula[i] = valor
            else:
                 i = i + 1
        i = 0
        while i < len(formula):
            if formula[i] == constant.ALGUM:
                valor = existeAlgumVizinho(estado, formula[i+1])
                formula.remove(formula[i+1])
                formula[i] = valor
            else:
                 i = i + 1
        i = 0
        while i < len(formula) :
            if formula[i] == constant.AND or formula[i] == constant.OR:
                
                valorEsquerdo = execute(estado, formula[i-1], mapa)
                valorDireito = execute(estado, formula[i+1], mapa)
                if formula[i] == constant.AND:
                    formula[i] = valorEsquerdo and valorDireito
                else:
                    formula[i] = valorEsquerdo or valorDireito
                    
                formula.remove(formula[i+1])
                formula.remove(formula[i-1])
                i=i-2
            i = i + 1
        i = 0
        while i < len(formula) :
            if formula[i] == constant.IMPLICACAO :
                valorEsquerdo = execute(estado, formula[i-1], mapa)
                valorDireito = execute(estado, formula[i+1], mapa)
                formula[i] = (not valorEsquerdo) or valorDireito
                formula.remove(formula[i+1])
                formula.remove(formula[i-1])
                i=i-2
            i=i+1
        return execute(estado, formula[0], mapa)

#W array com nome dos estados
# R mapa com as relacoes entre os estados
# V mapa com as valoracoes (estado w pertence a V[p])
def montaValoracaoLocal(estado):
    global V
    valoracaoLocal = {}
    for variavel, estados in V.items():
        valoracaoLocal[variavel] = valoracao(variavel, estado, V)
    return valoracaoLocal

def existeAlgumVizinho(estado, formula):
    global W, R, V
    
    if not estado in R:
        return False #Sumidouro
    
    for vizinho in R[estado]:
        valoracaoLocal = montaValoracaoLocal(vizinho)
        formulaSave = formula.copy()
        if execute(vizinho, formulaSave, valoracaoLocal):
            return True
    return False

def paraTodoVizinho(estado, formula):
    global W, R, V

    if not estado in R:
        return True #Sumidouro
    
    for vizinho in R[estado]:
        valoracaoLocal = montaValoracaoLocal(vizinho)
        formulaSave = formula.copy()
        if not execute(vizinho, formulaSave, valoracaoLocal):
            return False
    return True
        

# p é verdadeiro no estado w - true, se não, false
def valoracao(var, w, V):
    for estado in V[var]:
        if estado == w:
            return True
    return False

# se w2 é vizinho de w1
def ehVizinho(w1, R, w2):
    for vizinho in R[w1]:
        if vizinho == w2:
            return True

    return False





'''
W = ["w1", "w2", "w3"]

R = {"w1": ["w2", "w3"], "w2": ["w3"], "w3": ["w2"]}

V = {"p": ["w1", "w2"], "q": ["w2", "w3"], "r": ["w3"]}

paraTodoVizinho(["w1", "w2", "w3"], {"w1": ["w2", "w3"], "w2": ["w3"], "w3": ["w2"]}, {"p": ["w1", "w2"], "q": ["w2", "w3"], "r": ["w3"]}, "w1", "r | q")

'''
