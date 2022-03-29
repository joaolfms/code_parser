import json


def get_log_file(file_path):
    file = open(file_path)

    try:
        arquivo = file.readlines()
    finally:
        file.close()
    
    return(arquivo)

def get_player_data(linha):
    i = 0
    name_start = 0
    nome_do_player = ""
    _id = 0
    for l in linha:
        if l == "n" and linha[i+1] == "\\" and name_start == 0:
            name_start = 1
            inicio_nome = i+2
            _id = linha[i-2]

        
        if l == "\\" and linha[i+1] == "t" and name_start == 1:
            name_start = 0
            fim_nome = i
            nome_do_player = linha[inicio_nome:fim_nome]

        i += 1

    
    return(nome_do_player, _id)


def get_kill_data(linha):
    i = 0
    contador_dois_pontos = 0
    for l in linha:
        if l == ":":
            contador_dois_pontos += 1
            if contador_dois_pontos == 3:
                inicio_nome_assassino = i + 2
        
        if l == "k" and linha[i+1] == "i" and linha[i-1] == " ":
            fim_nome_assassino = i - 1
            assassino = linha[inicio_nome_assassino:fim_nome_assassino]
            inicio_nome_morto = i + 7

        if l == "b" and linha[i+1] == "y" and linha[i-1] == " ":
            fim_nome_morto = i - 1
            morto = linha[inicio_nome_morto:fim_nome_morto]
        
        i += 1
    
    return(assassino, morto)


def json_writer(games_list):
    with open('data.json', 'w', encoding='utf-8') as f:
        contador = 1
        f.writelines("[")
        for g in games_list:
            #print(f"[{{\n\"game\": {contador}, \n\"status\": {{\n\"total_kills\": {g.kills}")
            f.writelines(f"{{\n\"game\": {contador}, \n\"status\": {{\n\"total_kills\": {g.kills},")
            f.writelines("\n\"players\": [\n")
            #print("\"players\": \n")
            contador_players = 1
            for p in g.players:
                #print("numero de players no game: ", len(g.players), "contador players: ", contador_players)
                if contador_players == len(g.players):
                    f.writelines(f"{{\n  \"id\": {p.id}, \n  \"nome\": \"{p.nome}\", \n  \"kills\": {p.kills}, \n  \"old_names\": {json.dumps(p.old_names)}\n}}\n")
                else:
                    f.writelines(f"{{\n  \"id\": {p.id}, \n  \"nome\": \"{p.nome}\", \n  \"kills\": {p.kills}, \n  \"old_names\": {json.dumps(p.old_names)}\n}},\n")
                contador_players += 1
            f.writelines("\n]\n}\n")
            if contador == len(games_list):
                f.writelines("\n}\n")
            else:
                f.writelines("\n},\n")
            contador += 1 
        f.writelines("]")