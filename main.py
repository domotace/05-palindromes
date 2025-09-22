#### Fonction secondaire
import unicodedata
import re
def ispalindrome(p):
#on convertit les majuscules en minuscules    
    p = p.lower()
#on se débarasse des accents
    p = unicodedata.normalize('NFD', p)
    p = ''.join(char for char in p if unicodedata.category(char) != 'Mn')
#on garde seulement les lettres et chiffres
    p = re.sub(r'[^a-zA-Z0-9]', '', p)
#on veut comparer la CDC avec sa version inversée
    return p == p[::-1]
    

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
