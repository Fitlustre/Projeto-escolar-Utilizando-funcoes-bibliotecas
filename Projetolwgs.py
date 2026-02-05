import termo_lib as jogo


def executar_jogo():

    palavra_secreta = jogo.palavra_aleatoria()
    palavra_limpa = jogo.remover_acentos(palavra_secreta).lower()

    tentativas = 6
    vitoria = False

    print('=' * 30)
    print(f'\033[1;34mJOGO TERMO - ADIVINHE A PALAVRA')
    print(f'Dica: A palavra tem {len(palavra_secreta)} letras.\033[m')
    print('=' * 30)
    print('As palavras são:\n',
          '\033[4mpercurso\033[m, \033[4mdetalhe\033[m, \033[4mmemória\033[m, \033[4mcontexto\033[m, \033[4mdesafio\033[m, \033[4mrecurso\033[m, \033[4mreflexão\033[m, \033[4mconceito\033[m\n',
          '\033[4mimpacto\033[m, \033[4mequilíbrio\033[m, \033[4mproposta\033[m, \033[4miniciativa\033[m, \033[4mestrutura\033[m, \033[4mlimite\033[m, \033[4mprocesso\033[m, \033[4mresposta\033[m\n',
          '\033[4msolução\033[m, \033[4melemento\033[m, \033[4mperspetiva\033[m, \033[4mobjetivo\033[m, \033[4mestratégia\033[m, \033[4mrelação\033[m, \033[4mfunção\033[m, \033[4mcenário\033[m\n',
          '\033[4mdinâmica\033[m,\033[4mcritério\033[m, \033[4mpotencial\033[m, \033[4minfluência\033[m, \033[4mresultado\033[m, \033[4morigem\033[m, \033[4mfator\033[m, \033[4msequência\033[m\n',
          '\033[4mnoção\033[m, \033[4mevidência\033[m, \033[4mabordagem\033[m, \033[4mreação\033[m, sentido\033[m, vbase, ligação\033[m, \033[4metapa\033[m\n',
          '\033[4mcondição\033[m, \033[4malternativa\033[m, \033[4mprincípio\033[m, \033[4mcontrolo\033[m, \033[4mdecisão\033[m, \033[4madaptação\033[m, \033[4mevolução\033[m, \033[4manálise\n\033[m')

    for i in range(1, tentativas + 1):
        print(f'\nTentativa {i}/{tentativas}:', end=' ')


        tnt = jogo.palpite(palavra_secreta).lower()


        resultado = jogo.comparar(tnt, palavra_secreta)
        print(f'Resultado: {resultado}')

        if tnt == palavra_limpa:
            vitoria = True
            break


    if vitoria:
        print(f'\n\033[32mBoa! Você acertou a palavra','\tSEM BATOTAS NÃO É?', f'{palavra_secreta.upper()}\033[m')
    else:
        print(f'\n\033[31mAcabaram as chances!', 'KKKKK, ITs OVER', f'A palavra era: {palavra_secreta.upper()}\033[m')


if __name__ == '__main__':
    executar_jogo()