# Biblioteca Termo

Biblioteca em Python para criar um jogo do tipo **Termo** no terminal.

Esta biblioteca fornece a lógica essencial do jogo, permitindo que quem a utiliza se foque apenas no fluxo principal (tentativas e fim do jogo).

---

## Funcionalidades

* Escolha automática de palavra secreta
* Validação do tamanho do palpite
* Avaliação do palpite com feedback visual (cores no terminal)

---

## Instalação

Coloca o ficheiro da biblioteca (por exemplo `termo_lib.py`) no mesmo diretório do teu projeto ou adiciona-o ao teu projeto Python.

---

## Utilização rápida

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

## API da biblioteca

### `palavra_aleatoria()`

```python
palavra = palavra_aleatoria()
```

**Descrição**
Seleciona aleatoriamente uma palavra da lista interna de palavras.

**Retorno**

* `str` — palavra secreta do jogo

---

### `palpite(palavra_secreta)`

```python
tentativa = palpite(palavra)
```

**Descrição**
Solicita ao jogador uma palavra e garante que esta tem o mesmo número de letras da palavra secreta. Após três tentativas inválidas, é apresentada uma dica com o número correto de letras.

**Parâmetros**

* `palavra_secreta` (`str`) — usada apenas para validar o tamanho do palpite

**Retorno**

* `str` — palavra válida introduzida pelo jogador

---

### `resultado(palpite, palavra_secreta)`

```python
resultado(tentativa, palavra)
```

**Descrição**
Compara o palpite com a palavra secreta e imprime o resultado no terminal usando cores ANSI.

**Cores utilizadas**

* Verde — letra correta na posição correta
* Amarelo — letra existente noutra posição
* Vermelho — letra inexistente

**Parâmetros**

* `palpite` (`str`) — tentativa do jogador
* `palavra_secreta` (`str`) — palavra correta

**Retorno**

* `None` (a função apenas imprime o resultado)

---

## Fluxo do jogo

1. Gerar a palavra secreta com `palavra_aleatoria()`
2. Ler um palpite válido com `palpite()`
3. Mostrar o resultado com `resultado()`
4. Repetir até o jogador acertar a palavra

---

## Regras de utilização

* A palavra secreta não deve ser alterada durante o jogo
* O jogo termina quando `tentativa == palavra`
* Não é necessário validar manualmente o tamanho do palpite

---

## Estrutura recomendada do projeto

```
projeto_termo/
│
├── termo_lib.py
├── main.py
└── README.md
```

---

## Notas

Esta biblioteca foi criada com fins educativos e pode ser facilmente estendida para:

* modos de jogo diferentes
* interfaces gráficas
* aplicações web
* bots

---

## Licença

Uso livre para fins educativos.
