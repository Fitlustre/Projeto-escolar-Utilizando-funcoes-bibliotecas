import pro


def jogar():
    opcoes = ["pedra", "papel", "tesoura"]

    while True:
        computador = random.choice(opcoes)
        usuario = input("\nEscolha pedra, papel, tesoura (ou 'sair'): ").lower()

        if usuario == "sair":
            break

        if usuario not in opcoes:
            print("Escolha inválida!")
            continue

        if usuario == computador:
            print(f"Empate! Ambos escolheram {usuario}.")
        elif (usuario == "pedra" and computador == "tesoura") or \
                (usuario == "papel" and computador == "pedra") or \
                (usuario == "tesoura" and computador == "papel"):
            print(f"Você venceu! {usuario} ganha de {computador}.")
        else:
            print(f"Você perdeu! {computador} ganha de {usuario}.")


jogar()
