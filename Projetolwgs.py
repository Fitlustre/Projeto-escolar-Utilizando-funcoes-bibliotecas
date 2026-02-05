import termo_lib as jogo

tentativas = 6
vitoria = False

print("=" * 30)
print("\033[1;34mJOGO TERMO - ADIVINHE A PALAVRA\033[m")
print("=" * 30)

palavra_secreta = jogo.palavra_aleatoria()
palavra_limpa = jogo.remover_acentos(palavra_secreta)

print(f"Dica: a palavra tem {len(palavra_limpa)} letras.")

for i in range(1, tentativas + 1):

    print(f"\nTentativa {i}/{tentativas}: ", end="")

    tentativa = jogo.palpite(palavra_limpa)

    resultado = jogo.comparar(tentativa, palavra_secreta)
    print(resultado)

    if tentativa == palavra_limpa:
        vitoria = True
        break


if vitoria:
    print(f'\n\033[32mBoa! Você acertou a palavra','\tSEM BATOTAS NÃO É?', f'{palavra_secreta.upper()}\033[m')
else:
    print(f'\n\033[31mAcabaram as chances!', 'KKKKK, ITs OVER', f'A palavra era: {palavra_secreta.upper()}\033[m')