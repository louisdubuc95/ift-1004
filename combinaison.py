from enums import Carte, TypeCombinaison
from random import choice, shuffle


class Combinaison:
    """Représente la combinaison d'un joueur

    Attributes:
        des (list): Liste des dés lancés.
        nb_lancers (int): Le nombre de lancers réalisés.
        types_cartes (list): Les différents types de cartes.
    """
    des = [0,0,0,0,0]
    nb_lancers = 0
    types_de = [
        Carte.AS, Carte.ROI, Carte.DAME, Carte.VALET, Carte.DIX, Carte.NEUF
    ]

    def __init__(self, des): # **** a completer ****
        """Initialise une combinaison"""
        self.des = des


    def relancer_des(self, index_a_relancer): # **** a completer ****
        """Relance les dés spécifiés
        Args:
            index_a_relancer (list): Liste des index des dés à relancer.
        """



        self.index_a_relancer = index_a_relancer

        for i in range(len(self.index_a_relancer)):
             if self.index_a_relancer[i] == 1:
                Combinaison.des[0:1] = Combinaison._lancer_des(self,1)

             elif self.index_a_relancer[i] == 2:
                 Combinaison.des[1:2] = Combinaison._lancer_des(self,1)

             elif self.index_a_relancer[i] == 3:
                Combinaison.des[2:3] = Combinaison._lancer_des(self,1)

             elif self.index_a_relancer[i] == 4:
                Combinaison.des[3:4] = Combinaison._lancer_des(self,1)

             elif self.index_a_relancer[i] == 5:
                Combinaison.des[4:5] = Combinaison._lancer_des(self,1)


    def determiner_type_combinaison(self): # **** a completer ****
        """Détermine le type de la combinaison.

        Return (TypeCombinaison): Le type de la combinaison.
        Nous passons manuellement le type en return .
        """

        codage = [0] * 6
        for i in range(len(Combinaison.des)):
            codage[Combinaison.des[i] - 1] += 1
        print(codage)


        trois = 0
        deux = 0
        for i in range(len(codage)):
            if codage[i] == 5:

                quinton = TypeCombinaison.QUINTON
                print(quinton)
                pts_7 = 7
                return pts_7

            elif codage[i] == 4:
                carre = TypeCombinaison.CARRE
                print (carre)
                pts_6 = 6
                return pts_6

            elif codage[i] == 3:
                trois = trois + 1

            elif codage[i] == 2:
                deux = deux + 1

        if deux == 1 and trois == 1:
            full = TypeCombinaison.FULL
            print(full)
            pts_5 = 5
            return pts_5

        elif trois == 1 and deux != 1:
            brelan = TypeCombinaison.BRELAN
            print(brelan)
            pts_4 = 4

            return pts_4

        elif (codage == [1, 1, 1, 1, 1, 0] or codage == [0, 1, 1, 1, 1, 1]):
            sequence = TypeCombinaison.SEQUENCE
            print(sequence)
            pts_3 = 3
            return pts_3

        elif deux == 2:
            deux_pair = TypeCombinaison.DEUX_PAIRES
            print(deux_pair)
            pts_2 = 2
            return pts_2

        elif deux == 1 and trois != 1:
            pair = TypeCombinaison.UNE_PAIRE
            print (pair)
            pts_1 = 1
            return pts_1

        else:
            autre = TypeCombinaison.AUTRE
            print (autre)
            pts_0 = 0
            return pts_0




    @staticmethod
    def determiner_meilleur_combinaison(combinaisons): # **** a completer ****
        """
        Méthode statique qui détermine la meilleure combinaison (et donc le meilleur joueur) parmi une liste.
        Args:
            combinaisons (list): Liste de combinaisons sous forme de liste de tuples (Joueur, Combinaison)

        Returns (tuple): Un tuple (Joueur, Combinaison) du meilleur joueur et de la meilleur combinaison ou (None, None)
                         en cas d'égalité. Il est à noter que le premier élément du tuple n'est pas nécessairement de
                         type Joueur. Ce peut être un object quelconque (Joueur, entier, string, etc.), selon
                         l'utilisation souhaitée.

        """


        combinaison1 = combinaisons

        if len(combinaison1[0]) == 2 :

            if combinaison1[1][0]>combinaison1[1][1] :
              # print("Joueur {0} gagne".format(combinaisons[0][0]))
                combinaison1 = [combinaison1[0] [0] , combinaison1[1][0]]
                return combinaison1

            elif combinaison1[1][1] > combinaison1[1][0] :
               combinaison1 = [combinaison1[0][1] , combinaison1[1][1]]
               return  combinaison1

            elif   combinaison1[1][1] == combinaison1[1][0] :
                 return " Match nul"

        if len(combinaison1[0]) == 3:


             if combinaison1[1][0] > combinaison1[1][1] and combinaison1[1][0] > combinaison1[1][2]:
               combinaison1 = [combinaison1[0] [0] , combinaison1[1][0]]
               return combinaison1


             elif combinaison1[1][1] > combinaison1[1][0] and combinaison1[1][1] > combinaison1[1][2]:
                 combinaison1 = [combinaison1[0][1], combinaison1[1][1]]
                 return combinaison1

             elif combinaison1[1][2] >combinaison1[1][0] and combinaison1[1][2] > combinaison1[1][1]:
                 combinaison1 = [combinaison1[0][2], combinaison1[1][2]]
                 return combinaison1

             else :
                return "Match null"




    def _lancer_des(self, n): # **** a completer ****
        """Lance n dés.

        Args:
            n (int): Le nombre de dés à lancer.
        """
        self.n = n
        self.resultat = []
        for i in range(self.n):
            self.resultat = self.resultat + [choice([0, 1, 2, 3, 4, 5])]  # variante de randint(1,6)
        return self.resultat


    def __str__(self): # **** a completer ****
        '''
        a vous de voir comment definir et utiliser
        :return: a definir selon vos besoins
        '''


        lancer_1 = []
        lancer  = lancer_1 + Combinaison.des

        for n, i in enumerate(lancer):

            if i == 0:
                lancer[n] = Carte.AS

            elif i == 1:
                lancer[n] = Carte.ROI


            elif i == 2:
               lancer[n] = Carte.DAME

            elif i == 3:
                lancer[n] = Carte.VALET

            elif i == 4:
                lancer[n] = Carte.DIX

            elif i == 5:
                lancer[n] = Carte.NEUF


        print ("Resultats du lancer actuel:\n")
        i = 0
        for a in range(len(lancer)):
            i += 1
            print ("Dé numéro {0} : {1}".format(i,lancer[a]))


        return lancer





#***************************
# vous n etes pas obligés de garder ces tests - ils sont là pour vous aider a comprendre les methodes
# vous pouvez les modifier a votre guise
#***************************

if __name__ == "__main__":
    combinaison = Combinaison()

    # Test de init
    assert len(combinaison.des) == 5
    assert combinaison.nb_lancers == 1

    # Test de relancer_des
    combinaison.relancer_des([])
    assert combinaison.nb_lancers == 1
    anciens_des = list(combinaison.des)
    combinaison.relancer_des([3, 4])
    assert combinaison.nb_lancers == 2
    assert combinaison.des[0:2] == anciens_des[0:2]

    # Test de _lancer_des
    assert len(combinaison._lancer_des(5)) == 5
    assert len(combinaison._lancer_des(0)) == 0
    des = combinaison._lancer_des(5)
    for elem in des:
        assert isinstance(elem, Carte)

    # Test de str()
    combinaison.des = combinaison.types_de[0:5]
    assert "Dés:     1  2  3  4  5" in str(combinaison)
    assert "Valeur:  A  R  D  V  X" in str(combinaison)

    # Tests unitaires de determiner_type

    combinaisons = [
             # Combinaisons avec As
            ([Carte.AS, Carte.AS, Carte.AS, Carte.AS, Carte.AS],
             TypeCombinaison.QUINTON),
             ([Carte.ROI, Carte.AS, Carte.VALET, Carte.DIX, Carte.NEUF],
              TypeCombinaison.SEQUENCE),
             ([Carte.VALET] * 4 + [Carte.AS], TypeCombinaison.QUINTON),
             ([Carte.VALET] * 3 + [Carte.AS, Carte.ROI], TypeCombinaison.CARRE),
             ([Carte.VALET] * 2 + [Carte.ROI, Carte.AS, Carte.ROI],
              TypeCombinaison.FULL),
             ([Carte.VALET] * 2 + [Carte.ROI, Carte.AS, Carte.DAME],
              TypeCombinaison.BRELAN),
             ([Carte.ROI, Carte.DAME, Carte.AS, Carte.DIX, Carte.NEUF],
              TypeCombinaison.SEQUENCE),
             # Combinaisons sans As
             ([Carte.VALET] * 5, TypeCombinaison.QUINTON),
             ([Carte.VALET] * 4 + [Carte.ROI], TypeCombinaison.CARRE),
             ([Carte.VALET] * 3 + [Carte.ROI] * 2, TypeCombinaison.FULL),
             ([Carte.VALET] * 3 + [Carte.ROI, Carte.DAME], TypeCombinaison.BRELAN),
             ([Carte.AS, Carte.ROI, Carte.DAME, Carte.VALET, Carte.DIX],
              TypeCombinaison.SEQUENCE),
             ([Carte.ROI, Carte.DAME, Carte.VALET, Carte.DIX, Carte.NEUF],
              TypeCombinaison.SEQUENCE),
             ([Carte.ROI, Carte.ROI, Carte.VALET, Carte.VALET, Carte.NEUF],
              TypeCombinaison.DEUX_PAIRES),
             ([Carte.ROI, Carte.ROI, Carte.DIX, Carte.VALET, Carte.NEUF],
              TypeCombinaison.UNE_PAIRE)
             ]

    for des, vrai_type in combinaisons:
        shuffle(des)
        combinaison.des = des
        type = combinaison.determiner_type_combinaison()
        assert type == vrai_type
