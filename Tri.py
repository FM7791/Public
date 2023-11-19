#######################################################
# Programme Python pour l'implémentation du Tri à bulle
 
def tri_bulle(tab):
    n = len(tab)
    # Traverser tous les éléments du tableau
    for i in range(n):
        for j in range(0, n-i-1):
            # échanger si l'élément trouvé est plus grand que le suivant
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]


# Programme principale pour tester le code ci-dessus
tab = [98, 22, 15, 32, 2, 74, 63, 70]
 
tri_bulle(tab)
 
print ("Le tableau trié est:")
for i in range(len(tab)):
    print ("%d" %tab[i])
	
######################################################
# Programme Python pour l'implémentation du Tri Fusion
tri_fusion (tableau) :
    Si la longueur est > 1:
      # séparer
      milieu = longueur // 2
      gauche = tableau [0 ... milieu - 1]
      droite = tableau [milieu ... fin]

      # diviser
      tri_fusion(gauche)
      tri_fusion(droite)

      # combiner
      fusion(tableau, gauche, droite)

Algorithme fusion #
fusion (tableau, gauche, droite)
  i, j, k = 0
  tant que i < longueur de gauche et j < longueur de droite
      Si gauche[i] < droite[j] alors
          tableau[k] = gauche[i] et i = i + 1
      Sinon
          tableau[k] = droite[j] et j = j + 1
      k = k + 1

  Pour les éléments restant, les ajouter à fin de tableau