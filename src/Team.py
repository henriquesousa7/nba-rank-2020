class Team:

    def __init__(self, name, games, defeats, victories):
        self.name = name
        self.games = games
        self.defeats = defeats
        self.victories = victories

    def __str__(self):
        return self.name + ";" + self.games + ';' + self.victories + ";" + self.defeats