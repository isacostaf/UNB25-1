# Risc Primeiros Passos

```
.data
hello: .asciiz "Oi, mundo!\n"

.text
main:
    li a7, 4        # código do syscall print_string
    la a0, hello
    ecall

    li a7, 10       # código do syscall para encerrar
    ecall
```

### Bloco .data
```
.data
hello: .asciiz "Oi, mundo!\n"
```

é onde declaramos as variaveis globais

```hello``` 
 é o nome da variavel, tipo var1, podemos criar qualquer nome

```.asciiz``` 
 é dizendo que eh uma string acabada em 0

```"Oi, mundo!\n"```
 é a mensagem da string

 ### Bloco .text

```
 .text
main:
    li a7, 4        # instrucao pro syscall: print_string
    la a0, hello
    ecall

    li a7, 10       # código do syscall para encerrar
    ecall
```

é onde fazemos o codigo funcionar
dividimos por blocos!

**1. damos a instrução**

```li a7, 4 ```

sempre fazemos li a7 **(codigo)**
essa primeira linha eh pq temos que dizer pra maquina oq ela vai fazer (ler um int, imprimir um int, imprimir uma string...) e é dessa forma que fazemos: li a7 [e o codigo syscall para o comando que queremos]
no caso de printar string o codigo é 4

*! códigos syscall estão no final*

**2. damos o dado**

```la a0, hello ```

estamos carregando o endereco de hello (string que queremos imprimir) em a0
*load address*

o código sempre vai realizar a isntrucao dita no syscall pegando o dado no a0 (quando aplicavel), sempre no a0 nunca em outra por isso sempre carregamos o que queremos em a0 e ele reconhece sem que tenhamos que decir

*e se quisermos imprimir duas coisas?*
lembre-se que em assembly fazemos uma coisa de cada vez, entao se queremos imprimir duas mensagens (como eh o exemplo do codigo) temos que fazer dois blocos diferentes

**3. dar o play**

```ecall```

sempre no final do codigo, dizemos pra rodar aquele bloco
ele vai subir ler o li, ver qual eh a instrucao (no caso, imprimir string) depois descer pegar a string que ta no endereco de a0 e fazer a instrucao (no caso imprimir)

### Encerrar

```
li a7, 10  
    ecall
```

da mesma forma que usavamos li a7 e passavamos o que o sistema devia fazer, faremos aqui de novo
so que a instrucao dessa vez eh: encerrar o sistema
*codigo para encerrar o sistema: 10*

ja que nao precisamos pegar um dado para isso por isso nao usamos a0 pra guardar algo

## Outros exemplos:

#### Duas impressões

```
.data
hello: .asciiz "Oi, mundo!\n"
bye:   .asciiz "Até logo!\n"

.text
main:
    li a7, 4        # Código de syscall para imprimir string
    la a0, hello    # Carrega o endereço de "hello" em a1
    ecall           # Imprime "Oi, mundo!"
    
    li a7, 4        # Código de syscall para imprimir string novamente
    la a0, bye      # Carrega o endereço de "bye" em a1
    ecall           # Imprime "Até logo!"

    li a7, 10       # Código de syscall para encerrar o programa
    ecall
```


#### Imprimir um numero:

```
.data
hello: .asciiz "O número é: "

.text
main:
    li a7, 4        # Código para imprimir string
    la a0, hello    # Endereço da string "O número é: "
    ecall           # Imprime a string
    
    li a7, 1        # Código para imprimir um número
    li a0, 5        # Número que queremos imprimir (5)
    ecall           # Imprime "5"

    li a7, 10       # Código de syscall para encerrar
    ecall

```

#### Ler um inteiro e imprimir:

```
.data
prompt: .asciiz "Digite um número: "  # Mensagem solicitando o número

.text
main:
    # Imprimir a mensagem "Digite um número: "
    li a7, 4         # Código para imprimir string
    la a0, prompt    # Carrega o endereço da mensagem em a1
    ecall            # Imprime a mensagem

    # Ler um número inteiro
    li a7, 5         # Código para ler inteiro
    ecall            # Lê o número e coloca em a0

    # Imprimir o número que foi lido
    li a7, 1         # Código para imprimir inteiro
    ecall            # Imprime o número armazenado em a0 (o número lido)

    # Finalizar o programa
    li a7, 10        # Código para encerrar o programa
    ecall
```


## Exemplo de syscalls:
**Imprimir string (código 4 em a0):**

a7 = 4: Imprimir uma string.

O endereço da string é esperado no registrador a0

**Imprimir número inteiro (código 1 em a0):**

a7 = 1: Imprimir um número inteiro.

O número a ser impresso está em a0

**Encerrar o programa (código 10 em a0):**

a7 = 10: Finalizar a execução do programa.

Não importa o valor em a0

**Leitura de inteiro (código 5 em a0):**

a7 = 5: Ler um número inteiro do teclado.

O número lido será colocado em a0
