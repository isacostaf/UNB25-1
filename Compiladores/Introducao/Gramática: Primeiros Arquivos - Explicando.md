## Explicando a Gramática do código
Vamos aprender o que eh cada coisa, o que cada coisa faz

```lex
%{
#include "hello.tab.h"  /* Importa definições dos tokens */
#include <stdio.h>
%}

%%

"Hello"    { return HELLO; }  /* Se encontrar "Hello", retorna o token HELLO */
"World"    { return WORLD; }  /* Se encontrar "World", retorna o token WORLD */

[ \t\n]+   { /* Ignora espaços e quebras de linha */ }

.          { /* Ignora qualquer outro caractere */ }

%%

int yywrap(void) {
    return 1;  /* Indica fim da entrada */
}

int main(int argc, char **argv) {
    return yyparse();  /* Chama o parser gerado pelo Bison */
}

```

A unica coisa que vamos fazer eh mexer com o que ta dentro dos dois *%%*

```lex "_palavra que queremos encontrar no texto_"   { return _NOMETOKEN_; }```

**[ \t\n]+** significa espaços, tabulações ou quebras de linha

colocamos ele pra significar _espaços, tabulações ou quebras de linha_
e depois dizemos ao codigo o que devemos fazer ao encontrar eles

```lex [ \t\n]+    {_ordem_}```

do mesmo jeito que tinhamso usado no reocnhecimento e agregacao de token:

```lex "_palavra que queremos encontrar no texto_"   { return _NOMETOKEN_; }```

se deixamos as chaves vazias

```lex [ \t\n]+    {}```

queremos dizer para ignorar esses caracteres

o mesmo acontece com o **.**
ele significa _qualquer outro caracter que nao seja _espaços, tabulações ou quebras de linha_

nesse codigo então estamos pedindo que ele ignore espaços, tabulações e qualquer outro caracter lixo

**Exemplo:**
```Hello   World!```

**[ \t\n]+:** O Flex vai passar pelos espaços e não vai fazer nada com eles, vai apenas pular para o próximo caractere, que é W.

**.:** O Flex vai passar pelo !, que não corresponde a "Hello" nem "World", e como não há ação associada, ele apenas descarte esse caractere.
