# Risc Primeiros Passos

```.data
hello: .asciiz "Oi, mundo!\n"

.text
main:
    li a0, 4        # código do syscall print_string
    la a1, hello
    ecall

    li a0, 10       # código do syscall para encerrar
    ecall
```
