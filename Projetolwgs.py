pedra = 1
papel = 2
tesoura = 3

def jogar_jokenpo(escolha_usuario, escolha_computador):
    if escolha_usuario == escolha_computador:
        return "Empate!"
    elif (escolha_usuario == pedra and escolha_computador == tesoura) or \
         (escolha_usuario == papel and escolha_computador == pedra) or \
         (escolha_usuario == tesoura and escolha_computador == papel):
        return "Jogador 1 Venceu!"
    
def numero_para_escolha(numero):
    if numero == pedra:
        return "Pedra"
    elif numero == papel:
        return "Papel"
    elif numero == tesoura:
        return "Tesoura"
    else:
        return "Escolha inválida"
    
def representar_jogo(escolha_usuario, escolha_computador):
    escolha_usuario_str = numero_para_escolha(escolha_usuario)
    escolha_computador_str = numero_para_escolha(escolha_computador)
    resultado = jogar_jokenpo(escolha_usuario, escolha_computador)
    
    return f"Jogador 1 escolheu: {escolha_usuario_str}\n" \
           f"Computador escolheu: {escolha_computador_str}\n" \
           f"Resultado: {resultado}"