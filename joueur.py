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
        self.nb_victoires = 0
        self.nb_parties_jouees = 0




    def jouer_tour(self, limite_lancers): # **** a completer ****
        """
        Joue le tour d'un joueur.
        Args:
            limite_lancers (int): Le nombre de lancers maximums.

        Returns (Combinaison): La combinaison obtenue

        """
        self.limite_lancers = limite_lancers
        self.nb_parties_jouees = self.nb_parties_jouees + 1
        return Combinaison.des
        """
        i = 0
        Joueur.nb_victoire(1)
        while i < self.limite_lancers :

         print("c'est au tour du joueur : {0}".format(ordre_aleatoire[0]))
         c1 = [0, 0, 0, 0, 0]
         Combinaison.des = c1

         c2 = [1, 2, 3, 4, 5]
         Combinaison.relancer_des(self, c2)
         Combinaison.__str__(self)
         nb_lancer = 0
         nb_lancer_1 = 0
         while nb_lancer < 3:

            nb_lancer += 1
            nb_lancer_1 += 1
            # print("*****")
            # print(nb_lancer_1)
            # print("******")
            if nb_lancer == 3:
                des_joueur_1 = Combinaison.des
                terminer_1 = Combinaison.determiner_type_combinaison(self)
                #   print (terminer_1)

            elif nb_lancer != 3:

                entre_utilisateur = input(
                    "Quel(s) dé(s) voulez-vous rejouer (0 pour aucun), entrez la liste ex.(1,5): ")
                des_choisi = Combinaison._convert(self, entre_utilisateur, ',')

                if des_choisi != [0]:
                    nb_lancer_1 += 1
                    Combinaison.relancer_des(self, des_choisi)
                    Combinaison.__str__(self)

                elif (des_choisi) == [0]:
                    terminer = Combinaison.determiner_type_combinaison(self)
                    print (terminer)
                    des_joueur_1 = Combinaison.des
                    nb_lancer = 3
                    """
    def _convert(self,nombre, virgule):
            """
            Cette definition traduit l'entré de l'utilisateur en liste pour que le programmme puisse s'executer.
            :param : l'entré de l'utilisateur (ex : "1,2,3") et ce que nous voulons enlever de l'entrer (ex : ",")
            :return : Une liste des pramètre entré par l'utilisateur (ex : [1,2,3]
            """

            results = nombre.split(virgule)
            results1 = list(map(int, results))
            return results1



    def __str__(self): # **** a completer ****
        """
        Converti le joueur en une chaîne de caractères le représentant (le nom du joueur).
        Returns (str): La chaîne de caractères représentant le joueur.

        """
        return self.nom