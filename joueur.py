from combinaison import Combinaison


class Joueur:
    """Classe représentant un joueur.

    Attributes:
        nom (str): Le nom du joueur
        nb_victoires (int): Le nombre de parties remportées.
        nb_parties_jouees (int): Le nombre de parties jouées.
    """
    def __init__(self, nom): # **** a completer ****
        """
        Initialise un nouveau joueur avec son nom.

        Args:
            nom (str): Le nom du joueur.
        """
        self.nom = nom
        print (type(self.nom))
        print (self.nom)
        self.nb_victoire = 0
        self. nb_parties_jouees = 0


    def jouer_tour(self, limite_lancers): # **** a completer ****
        """
        Joue le tour d'un joueur.
        Args:
            limite_lancers (int): Le nombre de lancers maximums.

        Returns (Combinaison): La combinaison obtenue

        """

        return self.limite_lancers

    def __str__(self): # **** a completer ****
        """
        Converti le joueur en une chaîne de caractères le représentant (le nom du joueur).
        Returns (str): La chaîne de caractères représentant le joueur.

        """
        c1 = "c'est au tour du joueur {0}".format(nom)
        return c1