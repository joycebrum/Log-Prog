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

from parserModule import transformaFormula
from constant import W
from constant import R 
from constant import V 
from constant import funcao
from processaEntrada import execute
import constant
    

def valor(estados, relacoes, valoracao, estado, f):
    global W, R, V, funcao
    #W, R, V, funcao = estados, relacoes, valoracao, f
    mapa = montaValoracaoLocal(estado)
    if(f) :
        formula = transformaFormula(funcao)
        print(formula)
        return execute(estado, formula, mapa)
    else :
        return "erro, entrada inválida";


'''
W = ["w1", "w2", "w3"]

R = {"w1": ["w2", "w3"], "w2": ["w3"], "w3": ["w2"]}

V = {"p": ["w1", "w2"], "q": ["w2", "w3"], "r": ["w3"]}

paraTodoVizinho(["w1", "w2", "w3"], {"w1": ["w2", "w3"], "w2": ["w3"], "w3": ["w2"]}, {"p": ["w1", "w2"], "q": ["w2", "w3"], "r": ["w3"]}, "w1", "r | q")

'''
