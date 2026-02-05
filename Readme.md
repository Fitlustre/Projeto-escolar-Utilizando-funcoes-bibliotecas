# Termo — Biblioteca Python para jogo de palavras

Esta biblioteca em Python implementa a lógica base de um jogo de adivinhação de palavras inspirado no **Termo**. O foco da biblioteca é fornecer funções simples e diretas para que o utilizador consiga criar um jogo funcional no terminal sem se preocupar com a lógica interna.

---

## Conteúdo da biblioteca

A biblioteca disponibiliza:

* Uma lista interna de palavras (`PALAVRAS`)
* Funções para gerir o funcionamento do jogo:

  * `palavra_aleatoria()`
  * `palpite(palavra)`
  * `resultado(palpite, palavra_certa)`

---

## Funcionamento

### `palavra_aleatoria()`

```python
palavra = palavra_aleatoria()
```

Seleciona aleatoriamente uma palavra da lista interna, que será usada como palavra secreta do jogo.

**Retorno:**

* `str` — palavra secreta

---

### `palpite(palavra)`

```python
tentativa = palpite(palavra)
```

Solicita ao jogador que introduza uma palavra e verifica se esta tem o mesmo número de letras que a palavra secreta. Caso o tamanho esteja incorreto, o jogador é convidado a tentar novamente. Após três tentativas inválidas, é apresentada uma dica com o número correto de letras.

**Parâmetros:**

* `palavra` (`str`) — palavra secreta usada para validação do tamanho

**Retorno:**

* `str` — palavra válida introduzida pelo jogador

---

### `resultado(palpite, palavra_certa)`

```python
resultado(tentativa, palavra)
```

Compara o palpite com a palavra correta e imprime no terminal o resultado com cores, indicando o estado de cada letra.

**Significado das cores:**

* Verde — letra correta na posição correta
* Amarelo — letra presente na palavra mas noutra posição
* Vermelho — letra ausente da palavra

**Parâmetros:**

* `palpite` (`str`) — tentativa do jogador
* `palavra_certa` (`str`) — palavra secreta

**Retorno:**

* `None` (a função apenas imprime o resultado)

---

## Exemplo de utilização

```python
from termo_lib import palavra_aleatoria, palpite, resultado

palavra = palavra_aleatoria()

while True:
    tentativa = palpite(palavra)
    resultado(tentativa, palavra)

    if tentativa == palavra:
        print("\nParabéns! Acertaste a palavra.")
        break
```

---

## Fluxo do jogo

1. Gerar a palavra secreta
2. Pedir um palpite válido ao jogador
3. Avaliar o palpite e mostrar o resultado
4. Repetir até a palavra ser descoberta

---

## Estrutura sugerida do projeto

```
projeto-termo/
├── termo_lib.py
├── main.py
└── README.md
```

---

## Notas finais

Esta biblioteca foi desenvolvida com fins educativos, permitindo praticar o uso de funções, módulos e lógica de programação em Python. Pode ser facilmente adaptada ou expandida para outros tipos de interface ou modos de jogo.
