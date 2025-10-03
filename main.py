"exercice fichiers"
#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires
def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode='r', encoding='utf8') as f:
        #f : liste des lignes du fichier
        # on parcourt f ligne par ligne
        for ligne in f :
            t = ligne.split(";")
            list_int = []
            # liste de str devient int
            for chaine in t :
                list_int.append(int(chaine))
            l.append(list_int)
    return l

def get_list_k(data, k):
    """l = []"""
    return data[k]

def get_first(l):
    "retourne le premier elmt de la liste"
    return l[0]

def get_last(l):
    "retourne le dernier elmt de la liste"
    return l[-1]

def get_max(l):
    "retourne le max de la liste"
    return max(l)

def get_min(l):
    "retourne le min de la liste"
    return min(l)

def get_sum(l):
    "retourne la somme de tous les elements de la liste"
    return sum(l)

#### Fonction principale

def main():
    "permet d'afficher le prog"
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))

if __name__ == "__main__":
    main()
