# Termo — Biblioteca Python para jogo de palavras

Esta biblioteca em Python implementa a lógica base de um jogo de adivinhação de palavras inspirado no **Termo**, funcionando exclusivamente no **terminal**. O utilizador importa as funções e controla apenas o ciclo do jogo.

---

## Conteúdo da biblioteca

A biblioteca contém:

* Uma lista de palavras (`PALAVRAS`)
* Quatro funções principais:

  * `palavra_aleatoria()`
  * `palpite(palavra)`
  * `remover_acentos(palavra)`
  * `comparar(palpite, palavra_certa)`

---

## Lista de palavras

### `PALAVRAS`

Lista interna de palavras usadas como possíveis palavras secretas.

* Tipo: `list[str]`
* Contém palavras com acentos
* Não é necessário modificar ou aceder diretamente

---

## Funções

### `palavra_aleatoria()`

```python
palavra = palavra_aleatoria()
```

Seleciona aleatoriamente uma palavra da lista `PALAVRAS`.

**Retorno:**

* `str` — palavra secreta (pode conter acentos)

**Utilização:**

* Deve ser chamada no início do jogo

---

### `palpite(palavra)`

```python
tentativa = palpite(palavra)
```

Solicita ao jogador que introduza uma palavra no terminal e valida se o número de letras corresponde ao da palavra secreta.

* Caso o tamanho esteja incorreto, o jogador é convidado a tentar novamente
* Após três tentativas inválidas, é apresentada uma dica com o número correto de letras

**Parâmetros:**

* `palavra` (`str`) — palavra secreta usada apenas para validar o tamanho

**Retorno:**

* `str` — palavra introduzida pelo jogador com o tamanho correto

---

### `remover_acentos(palavra)`

```python
palavra_sem_acentos = remover_acentos(palavra)
```

Remove acentos de uma palavra, permitindo comparações corretas entre palavras com e sem acentuação.

**Parâmetros:**

* `palavra` (`str`) — palavra com ou sem acentos

**Retorno:**

* `str` — palavra sem acentos

**Observação:**

* Esta função é usada internamente na comparação das palavras

---

### `comparar(palpite, palavra_certa)`

```python
resultado = comparar(tentativa, palavra)
```

Compara o palpite do jogador com a palavra secreta, ignorando acentos, e devolve uma string colorida para ser exibida no terminal.

**Lógica de comparação:**

* Verde — letra correta na posição correta
* Amarelo — letra existente na palavra, mas noutra posição
* Vermelho — letra inexistente na palavra

**Parâmetros:**

* `palpite` (`str`) — palavra introduzida pelo jogador
* `palavra_certa` (`str`) — palavra secreta (pode conter acentos)

**Retorno:**

* `str` — palavra colorida com códigos ANSI

---

## Exemplo de utilização

```python
from termo_lib import palavra_aleatoria, palpite, comparar

palavra = palavra_aleatoria()

while True:
    tentativa = palpite(palavra)
    resultado = comparar(tentativa, palavra)
    print(resultado)

    if tentativa == palavra:
        print("\nParabéns! Acertaste a palavra.")
        break
```

---

## Fluxo do jogo

1. Gerar a palavra secreta com `palavra_aleatoria()`
2. Ler uma tentativa válida com `palpite()`
3. Comparar a tentativa com `comparar()`
4. Mostrar o resultado no terminal
5. Repetir até o jogador acertar

---

## Estrutura recomendada do projeto

```
projeto-termo/
├── termo_lib.py
├── main.py
└── README.md
```

---

## Notas finais

* A biblioteca funciona apenas em ambiente de terminal
* As cores são aplicadas usando códigos ANSI
* A comparação ignora acentos para evitar erros de validação

Esta biblioteca foi desenvolvida com fins educativos, focada na prática de funções, módulos e lógica de programação em Python.
