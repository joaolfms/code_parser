import os
from classes import Player, Game
from helpers import get_log_file, get_player_data, get_kill_data, json_writer

    
arquivo = get_log_file(os.environ.get('PATH_TO_LOG_FILE') or "Quake.txt")

games = []

for linha in arquivo:
    if "InitGame" in linha:
        game = Game()

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



    if "ShutdownGame:" in linha:
        games.append(game)

json_writer(games)
