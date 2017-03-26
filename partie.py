from joueur import Joueur
from combinaison import Combinaison
from random import shuffle


class Partie:
    """Représente une partie du jeu de Poker d'As

    Attributes:
        joueurs (list): La liste des joueurs.
    """

    def __init__(self, joueurs): # **** a completer ****
        """Initialise une partie avec la liste de joueurs

        Args:
            joueurs (list): La liste des joueurs.
        """
        self.joueurs = joueurs  #C'est une liste de joeur


        print("SWAG")
        print(len(self.joueurs))



    def jouer_partie(self): # **** a completer ****
        """ Joue une partie entre tous les joueurs et détermine le gagnant.
        Le compteur du nombre de partie est incrémenté pour chacun des joueurs.
        Le compteur de victoires est incrémenté pour le joueur gagnant (si la partie n'est pas nulle).
        Le joueur gagnant est affiché à l'écran (ou un message indiquant que la partie est nulle, s'il y a lieu).
        """

        c1  = [0,0,0,0,0]
        Combinaison.des = c1

        c2 = [1,2,3,4,5]
        Combinaison.relancer_des(self,c2)

        i =0

        ordre_aleatoire = Partie._determiner_ordre(self)

        while i < len(self.joueurs) :
            i+=1


            if i == 1 :
                print ("c'est au tour du joueur : {0}\n".format(ordre_aleatoire[0:1]))
                Combinaison.__str__(self)
                nb_lancer = 0
                while nb_lancer < 3 :
                    nb_lancer += 1
                    if nb_lancer != 3 :
                        entre_utilisateur = input("\nQuel(s) dé(s) voulez-vous rejouer (0 pour aucun), entrez la liste ex.(1,5): ")
                        des_choisi = Partie._convert(self, entre_utilisateur, ',')

                        if des_choisi != [0]:
                            Combinaison.relancer_des(self,des_choisi)
                            Combinaison.__str__(self)

                        elif(des_choisi) == [0]:
                            nb_lancer=3


            elif i == 2 :
                 print("c'est au tour du joueur : {0}".format(ordre_aleatoire[1:2]))

                 Combinaison.__str__(self)
                 nb_lancer = 0
                 while nb_lancer < 3:
                    nb_lancer += 1
                    if nb_lancer != 3:
                          entre_utilisateur = input(
                             "\nQuel(s) dé(s) voulez-vous rejouer (0 pour aucun), entrez la liste ex.(1,5): ")
                          des_choisi = Partie._convert(self, entre_utilisateur, ',')

                          if des_choisi != [0]:
                            Combinaison.relancer_des(self, des_choisi)
                            Combinaison.__str__(self)

                          elif (des_choisi) == [0]:
                            nb_lancer = 3

            elif i == 3 :
                 print("c'est au tour du joueur : {0}".format(ordre_aleatoire[2:3]))

                 Combinaison.__str__(self)
                 nb_lancer = 0
                 while nb_lancer < 3:
                    nb_lancer += 1
                    if nb_lancer != 3:
                        entre_utilisateur = input(
                            "\nQuel(s) dé(s) voulez-vous rejouer (0 pour aucun), entrez la liste ex.(1,5): ")
                        des_choisi = Partie._convert(self, entre_utilisateur, ',')

                        if des_choisi != [0]:
                            Combinaison.relancer_des(self, des_choisi)
                            Combinaison.__str__(self)

                        elif (des_choisi) == [0]:
                          nb_lancer = 3


        #TEMPORAIRE

        print()
        print(Partie._determiner_ordre(self))
        print()





    def _determiner_ordre(self): # **** a completer ****
        """Détermine l'ordre dans lequel les joueurs vont jouer.
        Return (list): La liste des index des joueurs indiquant l'ordre.

        Exemple:
            [2, 1, 0] indique que joueur 3 joue, suivi du joueur 2, puis du
            joueur 1.
        """
        if len(self.joueurs) == 1:
            self.ordre_1 = [0]
            shuffle(self.ordre_1)
            self.ordre_aleatoire = [self.joueurs[i] for i in self.ordre_1]
            return self.ordre_aleatoire
        if len(self.joueurs) == 2:
            self.ordre_1 = [0,1]
            shuffle(self.ordre_1)
            self.ordre_aleatoire = [self.joueurs[i] for i in self.ordre_1]
            return  self.ordre_aleatoire
        elif len(self.joueurs) == 3:
            self.ordre_1 = [0,1,2]
            shuffle(self.ordre_1)
            self.ordre_aleatoire = [self.joueurs[i] for i in self.ordre_1]
            return self.ordre_aleatoire


    def _convert(self,nombre, virgule):
            """
            Cette definition traduit l'entré de l'utilisateur en liste pour que le programmme puisse s'executer.
            :param : l'entré de l'utilisateur (ex : "1,2,3") et ce que nous voulons enlever de l'entrer (ex : ",")
            :return : Une liste des pramètre entré par l'utilisateur (ex : [1,2,3]
            """

            results = nombre.split(virgule)
            results1 = list(map(int, results))
            return results1




#***************************
# vous n etes pas obligés de garder ces tests - ils sont là pour vous aider a comprendre les methodes
# vous pouvez les modifier a votre guise
#***************************
# adklfs;alkgjfas;lkgj;lsakdgj;laskgj;askldfjl;ksadf;lksajdf
if __name__ == "__main__":
    joueurs = [Joueur("a"), Joueur("b"), Joueur("c")]

    partie = Partie(joueurs)

    # Teste que tous les joueurs vont jouer une et une seule fois
    ordre = partie._determiner_ordre()
    assert len(ordre) == 3
    assert 0 in ordre
    assert 1 in ordre
    assert 2 in ordre


