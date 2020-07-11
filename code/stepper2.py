import RPi.GPIO as GPIO
from time import sleep
#il faut utiliser 3 port gpio
#Pour les jumpers : 1,2,3 OFF et 4,5,6 ON
#Port enable qui alimente le moteur
ENA=40
#Port Direction qui donne la direction clockwise ou anticlockwise
DIR=38
#Port pulse controle la vitesse du moteur par impulsion
PUL=36
GPIO.setmode(GPIO.BOARD)
#on les programmes on mode sortie
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(PUL, GPIO.OUT)
#on alimente le moteur avec le port enable
GPIO.output(ENA,GPIO.HIGH)
#on définie les différentes vitesses qu'on va utilisé
maxspeed=0.00005
mediumspeed=0.0002
minspeed=0.0005
#fonction pour tourner le moteur contre les aiguilles du montre
def anticlockwise(x1,s):
    #on a mis x1*18 parceque 18 désigne une seule degré
    for i in range(x1*18):
            #on donne la direction anticlockwise
            GPIO.output(DIR,GPIO.LOW)
            #on donne une pulse au moteur avec la vitesse s donnée
            GPIO.output(PUL,GPIO.HIGH)
            sleep(s)
            GPIO.output(PUL,GPIO.LOW)
            sleep(s)
    sleep(1)
#fonction pour tourner le moteur le sens des aiguilles du montre    
def clockwise(x2,s):
    for i in range(x2*18):
            #on donne la direction clockwise
            GPIO.output(DIR,GPIO.HIGH)
            GPIO.output(PUL,GPIO.HIGH)
            sleep(s)
            GPIO.output(PUL,GPIO.LOW)
            sleep(s)    
    sleep(1)
#fonction qui donne la main à l'utilisateur pour choisir la vitesse 
def speed(i):
    if i==0 :
        return maxspeed
    elif i==1 :
        return mediumspeed
    else :
        return minspeed
try:
    while True:
        #voici le main du program , on prend les valeurs désiré par l'utilisateur puis on les donnes comme arguments pour les fonctions définies
        print("enter the turn mode : 0 for anticlockwise / 1 for clockwise")
        mode=int(input())
        print("choose speed : 0 for high speed / 1 for medium speed / 2 for low speed :")
        a=int(input())
        s=speed(a)
        if(mode==0):
            print("enter the angle : ")
            x=int(input())
            anticlockwise(x,s)
        else:
            print("enter the angle : ")
            x=int(input())
            clockwise(x,s)
            
except KeyboardInterrupt:
        GPIO.output(PUL,GPIO.LOW)
        GPIO.cleanup()
            