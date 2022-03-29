import os
from classes import Player, Game
from helpers import get_log_file, get_player_data, get_kill_data, json_writer
# Importações necessárias para execução do programa.
    
arquivo = get_log_file(os.environ.get('PATH_TO_LOG_FILE') or "Quake.txt")
# Definindo o arquivo a ser mapeado.

games = [] 
# Lista com os games mapeados no log.

for linha in arquivo:
    if "InitGame" in linha:
        game = Game()
# Condição para definir o inicio de cada game.

    if "ClientUserinfoChanged" in linha:
        player_ja_existe = 0
        nome_do_player, _id = get_player_data(linha)
        player = Player(_id, nome_do_player) 
        for p in game.players:
            if player.id == p.id:
                player_ja_existe = 1

            if player.id == p.id and player.nome != p.nome:
                p.atualizar_nome(player.nome)

        if player_ja_existe != 1: 
            game.players.append(player)
# Condição para definir e atualizar o nome de cada player.

    if "Kill" in linha:
        game.kills += 1
        assassino, morto = get_kill_data(linha)

        if assassino == "<world>":
            for p in game.players:
                if p.nome == morto:
                    p.kills -= 1 
        else:
            for p in game.players:
                if p.nome == assassino and p.nome != morto:
                    p.kills += 1 
# Condição para deinir o número de kills para cada players.



    if "ShutdownGame:" in linha:
        games.append(game)
# Condição que defini o final de um game e adiciona-o a lista de games com suas informações.

json_writer(games)
# Retorna o arquivo em json.
