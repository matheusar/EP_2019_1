# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Matheus Amaral Ricardo, matheusar@al.insper.edu.br
# - aluno B: Leonardo Alvarez, leonardosa2@al.insper.edu.br



def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor e avistou uma luz estranha no fim do corredor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor",
                "investigar": "Ir até a luz"
                
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e quer devorar sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "explorar": "Explorar o ambiente"
            }
        },
        "investigar": {
            "titulo": "Shazam",
            "descricao": "Voce achou o a maquina de teleporte!",
            "opcoes": {
                    "inicio": "teleportar para o saguao de entrada",
                    "andar professor": "teleportar para o andar do professor",
                    "professor": "teleportar para a sala do professor",
                    "biblioteca": "teleportar para a biblioteca"
            }
        },
        "explorar": {
            "titulo": "Uau",
            "descricao": "Voce achou uma armadura!",
            "opcoes": {
                    "inicio": "Voltar para o saguao de entrada"
            }
        },
        "fuga": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e quer devorar sua alma."
                         "Por sorte, sua armadura te salvou do primeiro golpe do monstro,"
                         "mas nao te salvará do segundo!",
            "opcoes": {
                    "fugir": "Fugir da sala imediatamente!",
                    "ficar": "Aceitar o fim"
            }
        },
        "fugir": {
            "titulo": "Parabens",
            "descricao": "Voce vonseguiu escapar com vida!",
            "opcoes": {
                    "gg": "FIM DE JOGO"
                    
            }
        },
        "ficar": {
            "titulo": "Que pena!",
            "descricao": "Voce morreu.",
            "opcoes": {
                    "gg": "FIM DE JOGO"
                    
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    armadura = 0
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        print(cenario_atual['titulo'])
        barreira = '-' * len(cenario_atual['titulo'])
        print(barreira)
        descricao_atual = cenario_atual['descricao']
        print(descricao_atual)
        # Imprime o nome do cenário e sua descrição
        
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print("Qual seu próximo movimento?")
            for x, y in opcoes.items():
                if nome_cenario_atual != "investigar":
                    print("{0}: {1}".format(x,y))
                # Imprime as opções de escolha para o jogador
                
            escolha = input("O que fará a seguir? ")
            if escolha in opcoes:
                
                nome_cenario_atual = escolha
                if escolha == "explorar":
                    armadura += 1
                elif escolha == "professor" and armadura > 0:
                    nome_cenario_atual = "fuga"
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
                # Jogador vai para o cenário que escolheu ou morre se 
                # escolher um cenário inexistente
    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
