# Git Guide

### 1. Clone a repository:
``` git clone https://github.com/isacostaf/UNB25-1.git```

O link deve ser copiado no proprio git do repositorio

### 2. Comitar
```git add .```

```git commit -m "Primeiro commit"```

```git push```

### 3. Branch

#### 3.1 criar e acessar branch
1. criei a branch no proprio git web
2. precisamos primeiro baixar as mudanças web para o repositorio - atualizar as info do web com a maquina:

```git fetch```

4. git checkout agora vamos entrar na branch

```git checkout gitbranch```

5. agora podemos somente dar um ```git add.``` que tudo vai ser automaticamente comitado na branch

#### 3.2 Atualizar pra ta pegando tudo que ta na branch main
```git pull origin main```

#### 3.3 Atualizar pra pegar dados de uma branch específica
Por exemplo: eu tenho a main, dentro da main tenho a gitbranch, e dentro de gitbranch tenho a git2
estou trabalhando e usando a git2 e gostaria de atualizar os dados pra pegar todas as atualizacoes que foram feitas e comitadas na gitbranch, mas nao quero pegar as mudancas e atualizacoes da main, porque eles tao fazendo o back, pode dar erro ou sei la, nao quero.
Eu faço então:
```git pull origin gitbranch```

#### 3.4 Merge
- Vai lá no web e faz um merge request, diz que quer juntar a sua branch na main, explica o porque e posta
- O administrador vai olhar e aceitar fazer o merge - ou não
- Tudo eh feito pela propria pagina

## Eu já passei:

#### Main local e remota tem commits diferentes, e ai quem ganha?
O erro que você está recebendo ocorre porque o seu repositório local (na branch main) e o repositório remoto (também na main) têm commits divergentes. Ou seja, as duas versões estão diferentes e o Git precisa saber como lidar com essas diferenças para integrar as alterações.

Como Resolver:
Escolher uma estratégia de merge: Você precisa decidir se deseja fazer um merge ou um rebase para resolver essa divergência.

Merge: Vai criar um commit de merge unindo as alterações das duas branches.

```git config pull.rebase false```

Rebase: Vai tentar aplicar suas alterações por cima das alterações remotas, reescrevendo o histórico.

git config pull.rebase true

Depois de escolher a estratégia de reconciliação, você pode executar o comando git pull novamente.

Se você escolheu **merge**, então simplesmente execute: ```git pull```

Se escolheu rebase, **execute**: ```git pull --rebase```

**Fazer o Push:** Após resolver a divergência (com merge ou rebase), o próximo passo é fazer o push das alterações locais para o repositório remoto:
```git push```

