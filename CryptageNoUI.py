from hashlib import sha256

fichier = input("Fichier à chiffrer : ")
sortie = input("Nommez le fichier final chiffré: ")
cle = input("Entrez la clé de chiffrement : ")

cles = sha256(cle.encode('utf-8')).digest()

with open(fichier,'rb') as f_fichier:
    with open(sortie,'wb') as f_sortie:
        i = 0
        while f_fichier.peek():
            c = ord(f_fichier.read(1))
            j = i % len(cles)
            b = bytes([c^cles[j]])
            f_sortie.write(b)
            i = i + 1