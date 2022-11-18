from time import sleep

try: #verifica se o arquivo game_methods está no diretório
    import game_methods
except:
    print("ERROR; game_methods.py was not found")
    exit()
else:
    import game_methods

try: #verifica se o arquivo cores está no diretório
    import cores
except: 
    print("ERROR; cores.py was not found")
    exit()
else:
    import game_methods

def Menu():
    print(("|"*15)+" JOGO "+("|"*15))
    print("Do Termo".center(36))
    print(" ")
    print(f"{cores.MakeStringColored('[0]','green')} Jogar\n{cores.MakeStringColored('[1]','yellow')} Jogadores\n{cores.MakeStringColored('[2]','red')} Sair\n")
    print("|"*36)

if game_methods.RunFileCheck(): #verifica se os arquivos .txt existem antes de começar o jogo
    while True: #Menu principal

        all_words = game_methods.Filter5CharWords() #cria uma lista com todas as palavras 
        upper_all_words = [] #armazena em maisuculo
        for word in all_words:
            upper_all_words.append(word.upper())

        Menu() #Mostra o menu

        inputmenu = input("-> ").strip() #pergunta o que o jogador quer fazer

        if inputmenu == "0": #se o jogador escolher jogar
            player_name = input("Nome do jogador: ") #salva o nome do jogador em uma variável
            palavra = game_methods.GiveRandomWord().upper().strip()
            tries = 0
            print(palavra)
            palpites = []
            alfabeto = { #salva o estado das letras e reinicia com o loop
                'A':'ns', #ns = not selected
                'B':'ns', #ne = non existent
                'C':'ns', #np = not positioned
                'D':'ns',
                'E':'ns', #rp = right positioned
                'F':'ns',
                'G':'ns',
                'H':'ns',
                'I':'ns',
                'J':'ns',
                'K':'ns',
                'L':'ns',
                'M':'ns',
                'N':'ns',
                'O':'ns',
                'P':'ns',
                'Q':'ns',
                'R':'ns',
                'S':'ns',
                'T':'ns',
                'U':'ns',
                'V':'ns',
                'W':'ns',
                'X':'ns',
                'Y':'ns',
                'Z':'ns'
            }
            
            while True: #jogo
                print("-"*52)
                print("*** Jogo Termo | By Thiago ***".center(50))
                print("-"*52)
                for letter in alfabeto: #mostra as letras do alfabeto e seu estado
                    if alfabeto[letter] == 'ns':
                        print(letter,end=" ")
                    elif alfabeto[letter] == 'ne':
                        print(f"{cores.MakeStringColored(letter,'red')}",end=" ")
                    elif alfabeto[letter] == 'np':
                        print(f"{cores.MakeStringColored(letter,'yellow')}",end=" ")
                    elif alfabeto[letter] == 'rp':
                        print(f"{cores.MakeStringColored(letter,'green')}",end=" ")
                print("\n"+"-"*52)

                contations=1
                for palpite in palpites: #mostra os ultimos palpites

                        print(f"{contations}ª", end=" - ")

                        loutras = []
                        for letra in palpite:
                            liutras = []
                            liutras[0] = letra[0]
                            liutras[1] = letra[1]
                            loutras.append(liutras)
                        
                        repetidas = []
                        leetras = []
                        for lonitras in loutras:
                            if lonitras[0] in leetras:
                                repetidas.append(lonitras[0])
                            else:
                                leetras.append(lonitras[0])
                        

                        
                        for letra in palpite:
                            if letra[1] == 'ns':
                                print(f"{cores.MakeStringColored(letra[0],'normal')}",end="")
                            elif letra[1] == 'np':
                                print(f"{cores.MakeStringColored(letra[0],'yellow')}",end="")
                            elif letra[1] == 'rp':
                                print(f"{cores.MakeStringColored(letra[0],'green')}",end="")
                            elif letra[1] == 'ne':
                                print(f"{cores.MakeStringColored(letra[0],'normal')}",end="")
                        contations+=1
                        print()

                if tries==5: #verifica se ele já tentou 5 vezes e dá a derrota quando chega
                    if game_methods.CheckRegister(player_name): #se o jogador está registrado
                        game_methods.RegisterDerrota(player_name)
                    else: #se o jogador não está registrado
                        game_methods.RegisterPlayer(player_name)
                        game_methods.RegisterDerrota(player_name)
                        print(f"{cores.MakeStringColored('[!]','red')} Você perdeu!!! A palavra era '{palavra}'")
                        sleep(1.5)
                        break

                while True: #verifica o input do usuário
                    resposta = input("Escreva seu palpite:> ").strip().upper() #pergunta o palpite do jogador
                    if len(resposta) != 5:
                        print("Esta palavra não contem apenas 5 letras")
                        continue
                    if resposta not in upper_all_words:
                        print("Esta palavra não existe no português brasileiro")
                        continue
                    break
                    

                if resposta == palavra: #se o jogador acertar

                    if game_methods.CheckRegister(player_name): #se o jogador está registrado
                        game_methods.RegisterVitoria(player_name)
                    else: #se o jogador não está registrado
                        game_methods.RegisterPlayer(player_name)
                        game_methods.RegisterVitoria(player_name)

                    print(f"{cores.MakeStringColored('[!]','green')} Você venceu!!! A palavra era '{palavra}'")
                    sleep(1.5)
                    break
                else: #se ele não acertar
                    palpite = []
                    for letra in range(0,5): #para cada letra no input
                        if resposta[letra] in palavra: #se a letra estiver na resposta final
                            if resposta[letra] == palavra[letra]: #se a letra estiver na mesma posição
                                lista = [resposta[letra],'rp']
                                palpite.append(lista)
                                if alfabeto[resposta[letra]] == 'ns' or alfabeto[resposta[letra]] == 'np':
                                    alfabeto[resposta[letra]] = 'rp'
                            else: #se não estiver na posição certa
                                lista = [resposta[letra],'np']
                                palpite.append(lista)
                                if alfabeto[resposta[letra]] == 'ns':
                                    alfabeto[resposta[letra]] = 'np'
                        else: #se não estiver
                            lista = [resposta[letra],'ne']
                            palpite.append(lista)
                            if alfabeto[resposta[letra]] == 'ns':
                                alfabeto[resposta[letra]] = 'ne'
                    palpites.append(palpite)
                    tries=tries+1

        elif inputmenu == "1": #se o jogador escolher ver os dados dos jogadores
            game_methods.ShowAllPlayers()
            input("Digite qualquer caractere para voltar ao menu:> ")
        elif inputmenu == "2": #se o jogador escolher sair
            break
        else:
            print("Opção inválida")
else:
    print(f"{cores.MakeStringColored('ERROR; br-sem-acentos.txt/jogadores.txt was not found, did you delete any files?','red')}")

print(f"{cores.MakeStringColored('Programa finalizado...','yellow')}") #mensagem pós loop