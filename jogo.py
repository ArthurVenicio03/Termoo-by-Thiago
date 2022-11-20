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

nickname_check_chars="QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm1234567890"

def Menu():
    print(("|"*15)+" JOGO "+("|"*15))
    print("Do Termo".center(36))
    print(" ")
    print(f"{cores.MakeStringColored('[0]','green')} Jogar\n{cores.MakeStringColored('[1]','yellow')} Jogadores\n{cores.MakeStringColored('[2]','red')} Sair\n")
    print("|"*36)

def CheckName(name): #validação do input do nome do jogador
    for l in name:
            if l not in nickname_check_chars:
                return False
    if len(name) > 12:
        return False
    return True

if game_methods.RunFileCheck(): #verifica se os arquivos .txt existem antes de começar o jogo
    while True: #Menu principal

        all_words = game_methods.Filter5CharWords() #cria uma lista com todas as palavras 
        upper_all_words = [] #armazena em maisuculo
        for word in all_words:
            upper_all_words.append(word.upper())

        Menu() #Mostra o menu

        inputmenu = input("-> ").strip() #pergunta o que o jogador quer fazer

        if inputmenu == "0": #se o jogador escolher jogar
            while True:
                player_name = input("Nome do jogador: ").strip() #salva o nome do jogador em uma variável
                if CheckName(player_name):
                    break
                else:
                    print("ERRO; Só são aceitos letras de A-Z e Números")

            palavra = game_methods.GiveRandomWord().upper().strip()
            tries = 0 #número de tentativas do jogador, vai aumentando até chegar a 5
            palpites = [] #onde vão ser registrados os palpites
            alfabeto = { #salva o estado das letras e reinicia com o loop
                'A':'ns', #ns = not selected
                'B':'ns', #ne = non existent
                'C':'ns', #np = not positioned
                'D':'ns', #rp = right positioned
                'E':'ns', 
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
                num_palpites=1
                for palpite in palpites: #mostra os ultimos palpites 
                    
                        print(f"{num_palpites}ª", end=" - ") #printa as posições dos palpites
                        pos_letras = {} #dicionário com letras e posições
                        string_palavra = "" #string com a palavra

                        for letra in palpite: #regitra todas as letras do palpite
                            string_palavra = f"{string_palavra}{letra[0]}"
                            
                        for letra in string_palavra: #registra a quantidade de aparições de cada letra
                            if letra in pos_letras.keys():
                                pos_letras[letra] = pos_letras[letra]+1
                            else:
                                pos_letras[letra] = 1
                            
                        final_list=["","","","",""] #onde vai ficar os caracteres
                        cont_letter = {} #conta a quantidade de letras que já apareceram 

                        cont_green = 0 #vai servir para verificar em qual sessão do loop a letra vai estar
                        for letra in palpite:#verdes
                            if letra[1] == 'rp':
                                final_list[cont_green] = f"{cores.MakeStringColored(letra[0],'green')}"
                                cont_green+= 1
                                if letra[0] in cont_letter:
                                    cont_letter[letra[0]] = cont_letter[letra[0]] + 1
                                else:
                                    cont_letter[letra[0]] = 1
                            else:
                                final_list[cont_green] = f"{cores.MakeStringColored(letra[0],'normal')}"
                                cont_green+= 1
                                
                        cont_yellow = 0 #vai servir para verificar em qual sessão do loop a letra vai estar
                        for letra in palpite:#amarelas
                            if letra[1] == 'np':
                                if letra[0] in cont_letter:
                                    if cont_letter[letra[0]] < palavra.count(letra[0]):
                                        cont_letter[letra[0]] = cont_letter[letra[0]] + 1
                                        final_list[cont_yellow] = f"{cores.MakeStringColored(letra[0],'yellow')}"
                                else:
                                    cont_letter[letra[0]] = 1
                                    final_list[cont_yellow] = f"{cores.MakeStringColored(letra[0],'yellow')}"
                            cont_yellow +=1

                        num_palpites+=1
                        palpite_com_espaços = "".join(final_list)
                        palpite_colorido=palpite_com_espaços.strip()
                        print(palpite_colorido)

                if tries==5: #verifica se ele já tentou 5 vezes e dá a derrota quando chega
                    if game_methods.CheckRegister(player_name): #se o jogador está registrado
                        game_methods.RegisterDerrota(player_name)
                        print(f"{cores.MakeStringColored('[!]','red')} Você perdeu!!! A palavra era '{palavra}'")
                        sleep(1.5)
                    else: #se o jogador não está registrado
                        game_methods.RegisterPlayer(player_name)
                        game_methods.RegisterDerrota(player_name)
                        print(f"{cores.MakeStringColored('[!]','red')} Você perdeu!!! A palavra era '{palavra}'")
                        sleep(1.5)
                    break

                while True: #verifica o input do usuário e valida ou não
                    resposta = input("Escreva seu palpite:> ").strip().upper() #pergunta o palpite do jogador
                    if resposta in upper_all_words and len(resposta) == 5:
                        break
                    else:
                        print("Esta palavra não existe no português brasileiro, não contém o número de letras necessário,\ncontem acentuação de letras, ou não é uma respota válida.")

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

                    palpite = [] #registra cada letra do palpite
                                 #vai conter listas com as letras e seu estado
                                 #exemplo: [A, 'ns'],[B,'np']

                    #altera o estado das letras no dicionário do alfabeto
                    for letra in range(0,5): 
                        if resposta[letra] in palavra: #se a letra estiver na resposta certa
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
