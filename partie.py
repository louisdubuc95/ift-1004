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

    def jouer_partie(self): # **** a completer ****
        """ Joue une partie entre tous les joueurs et détermine le gagnant.
        Le compteur du nombre de partie est incrémenté pour chacun des joueurs.
        Le compteur de victoires est incrémenté pour le joueur gagnant (si la partie n'est pas nulle).
        Le joueur gagnant est affiché à l'écran (ou un message indiquant que la partie est nulle, s'il y a lieu).
        """
        des_joueur_1 = [0] * 5
        des_joueur_2 = [0] * 5
        des_joueur_3 = [0] * 5
        i = 0

#   Crée une variable "ordre_aleatoire" avec les valeurs de la fonction "determiner_ordre" du présent fichier
#   dans le but de créer une liste des noms de manière aléatoire.

        ordre_aleatoire = Partie._determiner_ordre(self)
        if len(self.joueurs) == 1 :
            print("\nL'ordre aléatoire sera  : {0}\n".format(ordre_aleatoire[0]))
        elif len(self.joueurs) == 2 :
            print("\nL'ordre aléatoire sera  : {0}, {1}\n".format(ordre_aleatoire[0],ordre_aleatoire[1]))
        elif len(self.joueurs) == 3 :
            print("\nL'ordre aléatoire sera  : {0}, {1} et {2}\n".format(ordre_aleatoire[0],ordre_aleatoire[1],ordre_aleatoire[2]))

#   Début de la boucle simulant une partie pour chaque joueurs


        while i < len(self.joueurs) :
            i+=1
          #  Joueur.nb_victoires = Joueur.nb_victoires + 1

            if i == 1 :
                print ("C'est au tour de {0}\n".format(ordre_aleatoire[0]))
                c1 = [0, 0, 0, 0, 0]
                Combinaison.des = c1

                c2 = [1, 2, 3, 4, 5]
                Combinaison.relancer_des(self, c2)
                Combinaison.__str__(self)
                nb_lancer = 0
                nb_lancer_1 = 0
                while nb_lancer < 3 :

                    nb_lancer += 1
                    nb_lancer_1 += 1
                    #print("*****")
                    #print(nb_lancer_1)
                    #print("******")
                    if nb_lancer == 3:
                        des_joueur_1 = Combinaison.des
                        terminer_1 = Combinaison.determiner_type_combinaison(self)
                     #   print (terminer_1)

#   Si le joueur décide de modifier son résultat actuel, le programme débute les prochaines lignes de code en
#   prenant en compte les dés sélectionnés pour la relance

                    elif nb_lancer != 3 :

                        entre_utilisateur = input("\nQuel(s) dé(s) voulez-vous rejouer (0 pour aucun), entrez la liste ex.(1,5): ")
                        des_choisi = Partie._convert(self, entre_utilisateur, ',')

                        if des_choisi != [0]:

                            Combinaison.relancer_des(self,des_choisi)
                            Combinaison.__str__(self)

                        elif(des_choisi) == [0]:
                            terminer_1 = Combinaison.determiner_type_combinaison(self)
                          #  print (terminer_1)

                            des_joueur_1 = Combinaison.des
                            nb_lancer=3

#   Cette partie du code sera lancée seulement si l'utilisateur indique qu'il y aura plus qu'un joueur dans la partie
#   elle correspond aux parties des autres joueurs

            elif i == 2 :

                 print("C'est au tour de {0}\n".format(ordre_aleatoire[1]))

                 c1 = [0, 0, 0, 0, 0]
                 Combinaison.des = c1

                 c2 = [1, 2, 3, 4, 5]
                 Combinaison.relancer_des(self, c2)

#   On change les valeurs numériques des dés pour les valeurs des "cartes"

                 Combinaison.__str__(self)

                 nb_lancer_2 = 0

#   Boucle permettant de limiter les théoriques joueurs 2 et 3 d'effectuer plus de lancers que le premier joueur

                 while nb_lancer_2 < nb_lancer_1:
                    nb_lancer_2 += 1
                    if nb_lancer_2 == nb_lancer_1:
                        des_joueur_2 = Combinaison.des
                        terminer_2 = Combinaison.determiner_type_combinaison(self)
                       # print (terminer_2)

                    elif nb_lancer_2 != nb_lancer_1:
                          entre_utilisateur = input(
                             "\nQuel(s) dé(s) voulez-vous rejouer (0 pour aucun), entrez la liste ex.(1,5): ")
                          des_choisi = Partie._convert(self, entre_utilisateur, ',')

                          if des_choisi != [0]:
                            Combinaison.relancer_des(self, des_choisi)
                            Combinaison.__str__(self)

#   Condition impliquant la fin du tour du joueur selon l'atteinte du nombre maximum de lancers

                          elif (des_choisi) == [0]:
                            terminer_2 = Combinaison.determiner_type_combinaison(self)
                          #  print (terminer_2)
                            des_joueur_2 = Combinaison.des
                            nb_lancer_2 = nb_lancer_1

            elif i == 3 :
                 print("C'est au tour de {0}\n".format(ordre_aleatoire[2]))

                 c1 = [0, 0, 0, 0, 0]
                 Combinaison.des = c1

                 c2 = [1, 2, 3, 4, 5]
                 Combinaison.relancer_des(self, c2)

                 Combinaison.__str__(self)
                 nb_lancer_3 = 0
                 while nb_lancer_3 < nb_lancer_1:
                    nb_lancer_3 += 1
                    if nb_lancer_3 == nb_lancer_1:
                        des_joueur_3 = Combinaison.des
                        terminer_3 = Combinaison.determiner_type_combinaison(self)
                      #  print (terminer_3)
                    elif nb_lancer_3 != 3:
                        entre_utilisateur = input(
                            "\nQuel(s) dé(s) voulez-vous rejouer (0 pour aucun), entrez la liste ex.(1,5): ")
                        des_choisi = Partie._convert(self, entre_utilisateur, ',')

                        if des_choisi != [0]:
                            Combinaison.relancer_des(self, des_choisi)
                            Combinaison.__str__(self)

                        elif (des_choisi) == [0]:
                            terminer_3 = Combinaison.determiner_type_combinaison(self)
                        #    print (terminer_3)
                            des_joueur_3 = Combinaison.des
                            nb_lancer_3 = nb_lancer_1




        if len(self.joueurs) == 2 :
            joueurs_combinaison = [[ordre_aleatoire[0], ordre_aleatoire[1]], [terminer_1, terminer_2]]
            c1 = Combinaison.determiner_meilleur_combinaison(joueurs_combinaison)
            rep = Partie.convertir_combi(self,c1[1])
            if c1[0] != "Match null":
                print("Joueur {0} gagne avec la combinaison {1}".format(c1[0],rep))
            elif c1[0] == "Match null":
                print ("Match null")

        elif len(self.joueurs) == 3:
            joueurs_combinaison =[[ordre_aleatoire[0], ordre_aleatoire[1], ordre_aleatoire[2]], [terminer_1, terminer_2,terminer_3]]
            c1 = Combinaison.determiner_meilleur_combinaison(joueurs_combinaison)
            rep = Partie.convertir_combi(self,c1[1])
            if c1[0] != "Match null":
                print("Joueur {0} gagne avec la combinaison {1}".format(c1[0],rep))
            elif c1[0] == "Match null":
                print ("Match null")


    def _determiner_ordre(self): # **** a completer ****
        """Détermine l'ordre dans lequel les joueurs vont jouer.
        Return (list): La liste des index des joueurs indiquant l'ordre.

        Exemple:
            [2, 1, 0] indique que joueur 3 joue, suivi du joueur 2, puis du
            joueur 1.
        """
#   On parcours la liste des joueurs selon leur nombre (1, 2 ou 3)
#   et l'on crée une nouvelle liste aléatoire contenant leurs noms

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

    def convertir_combi (self,x):
        """
        definition local dans la classe
        :param x:
        :return:
        """
        if x == 0:
            return "Autre"
        elif x == 1:
            return "Une paire"
        elif x == 2:
            return "Deux pair"
        elif x == 3:
            return "Séquence"
        elif x == 4:
            return "Brelan"
        elif x == 5:
            return "Full"
        elif x == 6:
            return "Carré"
        elif x == 7:
            return "Quinton"


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


