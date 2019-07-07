PARATODOINICIO = '['
PARATODOFIM = ']'

ALGUMINICIO = '<'
ALGUMFIM = '>'

OR = '|'

AND = '&'

IMPLICACAO = "->"

NOT = "!"

#W, R, V e funcao já com um caso de teste preenchido
funcao = "[ana]<beto>!p -> <carla>(q & p)"

W = ["w1", "w2", "w3"]

R = {"a": {"w1": ["w2", "w3"], "w2": ["w3"], "w3": ["w2"]},
     "b": {"w1": ["w2", "w3"], "w2": ["w3"], "w3": ["w2"]}}

V = {"p": ["w1", "w2"], "q": ["w2", "w3"], "r": ["w3"]}
