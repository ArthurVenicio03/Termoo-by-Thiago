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
            tries = 1
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
                for palpite in palpites: #mostra os ultimos palpites (não me pergunte como funciona nem eu sei)
                                         #levou a aula do matheus inteira + meia hora pra fazer
                        print(f"{contations}ª", end=" - ")
                        liutras = {} #dicionário com letras e posições
                        loutras = "" #string com a palavra
                        for letra in palpite: #regitra todas as letras do palpite em uma string
                            loutras = f"{loutras}{letra[0]}"
                        for letra in loutras: #registra a quantidade de aparições de cada letra em um dicionário
                            if letra in liutras.keys():
                                liutras[letra] = liutras[letra]+1
                            else:
                                liutras[letra] = 1
                            
                        final_string=["","","","",""]
                        cont_letter = {}

                        cont_green = 0
                        for letra in palpite:#verdes
                            if letra[1] == 'rp':
                                final_string[cont_green] = f"{cores.MakeStringColored(letra[0],'green')}"
                                cont_green+= 1
                                if letra[0] in cont_letter:
                                    cont_letter[letra[0]] = cont_letter[letra[0]] + 1
                                else:
                                    cont_letter[letra[0]] = 1
                            else:
                                final_string[cont_green] = f"{cores.MakeStringColored(letra[0],'normal')}"
                                cont_green+= 1
                                
                        cont_yellow = 0
                        for letra in palpite:#amarelas
                            if letra[1] == 'np':
                                if letra[0] in cont_letter:
                                    if cont_letter[letra[0]] < palavra.count(letra[0]):
                                        cont_letter[letra[0]] = cont_letter[letra[0]] + 1
                                        final_string[cont_yellow] = f"{cores.MakeStringColored(letra[0],'yellow')}"
                                else:
                                    cont_letter[letra[0]] = 1
                                    final_string[cont_yellow] = f"{cores.MakeStringColored(letra[0],'yellow')}"
                            cont_yellow +=1

                        contations+=1
                        end = "".join(final_string)
                        new_end=end.strip()
                        print(new_end)

                if tries==6: #verifica se ele já tentou 5 vezes e dá a derrota quando chega
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

        elif inputmenu == "1": #se o jogador escol11111her ver os dados dos jogadores
            game_methods.ShowAllPlayers()
            input("Digite qualquer caractere para voltar ao menu:> ")
        elif inputmenu == "2": #se o jogador escolher sair
            break
        else:
            print("Opção inválida")
else:
    print(f"{cores.MakeStringColored('ERROR; br-sem-acentos.txt/jogadores.txt was not found, did you delete any files?','red')}")

print(f"{cores.MakeStringColored('Programa finalizado...','yellow')}") #mensagem pós loop
