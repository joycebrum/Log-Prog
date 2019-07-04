
import constant

funcao = ""
contador = 0

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
            variavel = adicionaVariavel(variavel, parseado)
            subarray = parse(i+1)
            parseado.append(subarray)
        elif(funcao[i] == ')'):
            variavel = adicionaVariavel(variavel, parseado)
            funcao = funcao.replace(funcao[pos:i], "*" + str(contador))
            return parseado
        elif i+1 < len(funcao) and(funcao[i] + funcao[i+1]) == constant.IMPLICACAO:
            variavel = adicionaVariavel(variavel, parseado)
            parseado.append(constant.IMPLICACAO)
            i = i + 1
        elif funcao[i] == constant.PARATODOINICIO or funcao[i] == constant.ALGUMINICIO:
            variavel = adicionaVariavel(variavel, parseado)
            i = adicionaParaTodoEExiste(parseado, funcao, i)
        elif funcao[i] == constant.AND or funcao[i] == constant.OR or funcao[i]== constant.NOT :
            variavel = adicionaVariavel(variavel, parseado)
            parseado.append(funcao[i])
            
        elif funcao[i] == ' ':
            variavel = adicionaVariavel(variavel, parseado)
        else :
            variavel += funcao[i]
        i = i + 1
    variavel = adicionaVariavel(variavel, parseado)
    return parseado

def adicionaVariavel(variavel, parseado):
    if len(variavel) > 0:
        parseado.append(variavel)
        variavel = ""
    return variavel

def adicionaParaTodoEExiste(parseado, funcao, i):
    final = ''
    if(funcao[i] == constant.PARATODOINICIO):
        final = constant.PARATODOFIM
    else:
        final = constant.ALGUMFIM
    parseado.append(funcao[i])
    variavel = ""
    i = i + 1;
    while(i < len(funcao) and funcao[i]!= final):
        variavel += funcao[i]
        i = i + 1
    adicionaVariavel(variavel, parseado)
    parseado.append(funcao[i])
    return i
