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
            #print(f"Ola player: {p.nome}")
            if player.id == p.id:
                player_ja_existe = 1

            if player.id == p.id and player.nome != p.nome:
                p.atualizar_nome(player.nome)

        if player_ja_existe != 1: 
            game.players.append(player)

        #print(f"{player.id} : {player.nome}")

    if "Kill" in linha:
        game.kills += 1
        assassino, morto = get_kill_data(linha)
        #print(f"Assassino: {assassino} - Morto: {morto}")

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



with open('data.json', 'w', encoding='utf-8') as f:
    contador = 1
    for g in games: 
        play = g.players
        klls = g.kills
        f.writelines(json.dumps(
            {
                "game" : contador,
                "status" : {
                "total_kills" : klls,
                "players" : []
            }
        }, 
    indent=4
))
        for p in play:
            kl = p.kills
            uid = p.id
            nome = p.nome
            old_name = p.old_names
            f.writelines(json.dumps(dict(
                [
                ("id", uid),
                ("nome", nome),
                ("kills", kl),
                ("old_names", old_name)
                ]
            ),sort_keys=True, indent=4
        ))
        contador += 1


#json_writer(games)