class Game:
    def __init__(self):
        self.kills = 0
        self.players = []

    def get_players_names(self):
        nomes = []
        for p in self.players:
            nomes.append(p.nome)
        return(nomes)

class Player:
    def __init__(self,id, nome):
        self.id = id
        self.nome = nome
        self.kills = 0
        self.old_names = []

    def atualizar_nome(self, novo_nome):
        if novo_nome in self.old_names:
            self.old_names.remove(novo_nome)

        self.old_names.append(self.nome)
        self.nome = novo_nome
