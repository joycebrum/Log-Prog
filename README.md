# Trabalho de Lógica em Programação.

#### Programa recebe uma fórmula proposicional e um mapeamento de tabela verdade e retorna o valor booleano da formula.

### Arquivo a ser executado na shell do python:
    trabalho1.py

### Método a ser chamado: 
    valor

### Parâmetros: 

estados, relacoes, valoracao, estado, f

- #### estados:
    Array de strings onde cada string representa o nome de um estado.
- #### relacoes:
    Mapa onde as chaves sao um estado e o valor associado é um array de estados aos quais a chave possui uma ligação.
- #### valoracao:
    Mapa onde as chaves são as variáveis e os valores associados a elas são um array de estados nos quais a variavel é verdadeira.
- #### estado:
    String com o estado desejado.
- #### f:
    String com operadores:
    
    | Símbolo  | Significado |
    | ------------- | ------------- |
    | <b>`!`</b>  | Negação  |
    | <b>`->`</b>  | Implicação  |
    | <b>`\|`</b>  | Ou  |
    | <b>`&`</b>  | E  |
    | <b>`#`</b>  | Para todo  |
    | <b>`$`</b>  | Existe  |

### Um exemplo 

Para facilitar, colocamos um exemplo ja pronto, que esta desenhado na imagem: " Grafo e Testte", segue um exemplo de sucesso e de falha

##### Exemplo com resultado true:

###### Valores
    estados = ["w1", "w2", "w3"]

    relacoes = {"w1": ["w2", "w3"], 
                "w2": ["w3"], 
                "w3": ["w2"]}

    valoracao = {"p": ["w1", "w2"],
                 "q": ["w2", "w3"],
                 "r": ["w3"]}

    estado = "w1"

    f = "p->#(q|r)"
    
###### Formula escrita:

    valor(["w1", "w2", "w3"], {"w1": ["w2", "w3"], "w2": ["w3"], "w3": ["w2"]}, {"p": ["w1", "w2"], "q": ["w2", "w3"], "r": ["w3"]}, "w1", "p->#(q|r)")
    

##### Exemplo com resultado false

###### Valores
    estados = ["w1", "w2", "w3"]

    relacoes = {"w1": ["w2", "w3"], 
                "w2": ["w3"], 
                "w3": ["w2"]}

    valoracao = {"p": ["w1", "w2"],
                 "q": ["w2", "w3"],
                 "r": ["w3"]}

    estado = "w1"
    
    f= "p->$(p&r)"
    
###### Formula escrita:
    
    valor(["w1", "w2", "w3"], {"w1": ["w2", "w3"], "w2": ["w3"], "w3": ["w2"]}, {"p": ["w1", "w2"], "q": ["w2", "w3"], "r": ["w3"]}, "w1", "p->$(p&r)")



