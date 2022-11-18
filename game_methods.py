import os
from sys import path
from random import choice
import cores

def RunFileCheck(): #Verifica se o arquivo está lá
    try:
        arquivo = open(os.path.join(path[0],"br-sem-acentos.txt"), "r")
        arquivo2 = open(os.path.join(path[0],"jogadores.txt"), "r")
    except:
        return False
    else:
        arquivo.close()
        arquivo2.close()
        return True

def Filter5CharWords(): #Retorna uma lista com todas as palavras com 5 letras
    arquivo = open(os.path.join(path[0],"br-sem-acentos.txt"), "r")
    fiveChars = []
    for line in arquivo:
        if len(line) == 6:
            line = line[:len(line) - 1]
            fiveChars.append(line)
    arquivo.close()
    return fiveChars

def GiveRandomWord(): #Retorna uma palavra de 5 letras aleatória
    words = Filter5CharWords()
    word = choice(words)
    return word

def RegisterPlayer(player): #registra o jogador no banco de dados txt
    arquivo = open(os.path.join(path[0],"jogadores.txt"), "a")
    with arquivo as f:
        f.write(f"{player}:0;0\n")
        f.close()

def RegisterVitoria(player):
    if CheckRegister(player):
        arquivo = open(os.path.join(path[0],"jogadores.txt"), "r")
        with arquivo as f:
            linhas = f.readlines()
            index_player = GetPlayerIndex(player)
            valor_vic = GetCurrentVitoria(player)
            linea = f"{player}:{int(valor_vic)+1};{GetCurrentDerrota(player)}\n"
            linhas[index_player] = linea
            f.close()
        arquivo2 = open(os.path.join(path[0],"jogadores.txt"), "w")
        with arquivo2 as f:
            f.writelines(linhas)
            f.close()
    else:
        return "player not found"

def RegisterDerrota(player):
    if CheckRegister(player):
        arquivo = open(os.path.join(path[0],"jogadores.txt"), "r")
        with arquivo as f:
            linhas = f.readlines()
            index_player = GetPlayerIndex(player)
            valor_der = GetCurrentDerrota(player)
            linea = f"{player}:{GetCurrentVitoria(player)};{int(valor_der)+1}\n"
            linhas[index_player] = linea
            f.close()
        arquivo2 = open(os.path.join(path[0],"jogadores.txt"), "w")
        with arquivo2 as f:
            f.writelines(linhas)
            f.close()
    else:
        return "player not found"

def GetCurrentVitoria(player):
    arquivo = open(os.path.join(path[0],"jogadores.txt"), "r+")
    with arquivo as f:
        linhas = f.readlines()
        index_player = GetPlayerIndex(player)
        count=0
        for char in linhas[index_player]: #encontra index de :
            if char == ":":
                index_thing = count
                break
            count+=1
        index_vic = index_thing+1 #registra o index do valor de vitorias
        valor_vic = linhas[index_player][index_vic]
        f.close()
        return valor_vic

def GetCurrentDerrota(player):
    arquivo = open(os.path.join(path[0],"jogadores.txt"), "r+")
    with arquivo as f:
        linhas = f.readlines()
        index_player = GetPlayerIndex(player)
        count=0
        for char in linhas[index_player]: #encontra index de :
            if char == ";":
                index_thing = count
                break
            count+=1
        index_vic = index_thing+1 #registra o index do valor de vitorias
        valor_vic = linhas[index_player][index_vic]
        f.close()
        return valor_vic

def GetPlayerName(index):
    arquivo = open(os.path.join(path[0],"jogadores.txt"), "r")
    with arquivo as f:
        linhas = f.readlines()
        name=''
        for char in linhas[index]: #encontra index de :
            if char == ":":
                break
            name+=char
        return name

def CheckRegister(player): #verificar se o jogador está registrado
    arquivo = open(os.path.join(path[0],"jogadores.txt"), "r")
    with arquivo as f:
        conteudo = f.readlines()
        for linha in conteudo:
            nome=""
            for char in linha:
                if char == ":":
                    break
                else:
                    nome+=char
            if nome == player:
                f.close()
                return True
        return False

def GetPlayerIndex(player): #pega o index da linha do jogador
    arquivo = open(os.path.join(path[0],"jogadores.txt"), "r")
    with arquivo as f:
        conteudo = f.readlines()
        index=0
        for linha in conteudo:
            nome=""
            for char in linha:
                if char == ":":
                    break
                else:
                    nome+=char
            if nome == player:
                f.close()
                return index    
            index+=1
        return "não encontrado"

def ShowAllPlayers():
    arquivo = open(os.path.join(path[0],"jogadores.txt"), "r")
    with arquivo as f:
        linhas = f.readlines()
        for i in range(len(linhas)):
            jogations = GetPlayerName(i)
            print("-"*30)
            print(f"{jogations}:")
            espaços = (" "*len(jogations))
            print(f"{espaços}Vitórias: {cores.MakeStringColored(GetCurrentVitoria(jogations),'green')}")
            print(f"{espaços}Jogos: {cores.MakeStringColored(str(int(GetCurrentDerrota(jogations))+int(GetCurrentVitoria(jogations))),'yellow')}")
            print(f"{espaços}Derrotas: {cores.MakeStringColored(GetCurrentDerrota(jogations),'red')}")
            print("-"*30)
        f.close()
