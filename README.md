# Trabalho de Lógica em Programação.

#### Programa recebe uma fórmula proposicional e um mapeamento de tabela verdade e retorna o valor booleano da formula.

### Método a ser chamado: 
    valor

### Parâmetros: 

estados, relacoes, valoracao, estado, f

- #### estados:
    array de strings onde cada string representa o nome de um estado
- #### relacoes:
    mapa onde as chaves sao um estado e o valor associado é um array de estados aos quais a chave possui uma ligação
- #### valoracao:
    mapa onde as chaves são as variáveis e os valores associados a elas são um array de estados nos quais a variavel é verdadeira
- #### f:
    string com operadores:
    
    | Símbolo  | Significado |
    | ------------- | ------------- |
    | <b>`!`</b>  | Negação  |
    | <b>`->`</b>  | Implicação  |
    | <b>`\|`</b>  | Ou  |
    | <b>`&`</b>  | E  |
    | <b>`#`</b>  | Para todo  |
    | <b>`$`</b>  | Existe  |

