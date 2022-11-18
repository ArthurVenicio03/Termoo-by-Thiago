colors = {
    'red':'\033[41m',
    'yellow':'\033[43m',
    'green':'\033[42m',
    'normal':'\033[0;0m'
}

def MakeStringColored(Str, f='normal'): #retorna um string que altera somente a cor de fundo da msg informada
    return colors[f]+Str+colors['normal']