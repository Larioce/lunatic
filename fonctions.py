def afficherMessage():
    print("++++++++++++")
    print("Veuillez patientez")
    print("++++++++++++")

afficherMessage()
#dsknhksdhj
a = 2
while a < 8:
    a = a+1
    print(a)
def calculerPi():
    pi = 0.0
    compteur = 1
    while compteur < 100000:
        if (compteur // 2) % 2 == 1:
            pi = pi - 1.0 / float(compteur)
        else:
            pi = pi + 1.0 / float(compteur)
        compteur = compteur + 2
    pi = pi * 4.0
    return pi
print ("+++++++++++++++")
print ("Voici la valeur PI")
print ("++++++++++++++++")

pi = calculerPi()
print (pi)
def convertirEnSecondes(heures, minutes, secondes):
    total = heures * 3600
    total = total + minutes * 60
    total = total + secondes
    return total
print("Début")
sec = convertirEnSecondes(5, 25, 10)
print (sec)
from math import sin,cos,pi,sqrt
x = sqrt(25) * pi * cos(pi / 2)
print(x)
#si on fais import math, on devra faire
#x = math.sqrt(25) * math.pi * math.cos(math.pi/2)
#try:
#x = int(raw_input("Veuillez entrer un nombre"))
#except ValueError:
#print("On avait dit un nombre!")
#nouvelle installation de manjaro
