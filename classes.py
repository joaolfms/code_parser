class Game:
# Classe para definir informçoes do Game

    def __init__(self):
        self.kills = 0
        self.players = []

    def get_players_names(self): 
# Método de classe para adicionar os players a um lista com os nomes dos players

        nomes = []
        for p in self.players:
            nomes.append(p.nome)
        return(nomes)

class Player:
# Define as informções de cada player (id, nome, kills, old_names)

    def __init__(self,id, nome):
        self.id = id
        self.nome = nome
        self.kills = 0
        self.old_names = []

    def atualizar_nome(self, novo_nome):
# Método para atualizar o nome do player em caso de mudança durante a partida e adicionar o anterior a lista old_names

        if novo_nome in self.old_names:
            self.old_names.remove(novo_nome)

        self.old_names.append(self.nome)
        self.nome = novo_nome
