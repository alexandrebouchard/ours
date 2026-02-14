# Importer les bibliothèques
from sense_hat import SenseHat
from time import sleep
import random

# Configuer le Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Configurer le capteur de couleurs
sense.color.gain = 60 # Régler la sensibilité du capteur
sense.color.integration_cycles = 64 # L'intervalle auquel la mesure est effectuée

# Ajouter des variables de couleur et une image

# Afficher l'image
v = (17, 192, 46)
b = (17, 69, 192)
r = (192,17,17)

rvb = sense.color 
c = (rvb.red, rvb.green, rvb.blue)


image = [
    c, c, c, c, c, c, c, c, 
    c, c, c, c, c, c, c, c, 
    c, c, c, c, c, c, c, c, 
    c, c, c, c, c, c, v, v, 
    c, c, c, c, c, c, v, v, 
    c, c, c, c, c, c, c, c, 
    c, c, c, c, c, c, c, c, 
    c, c, c, c, c, c, c, c, 
  ]

sense.set_pixels(image)

sleep(1)


image = [
    c, c, c, c, c, c, c, c, 
    c, c, c, c, c, c, c, c, 
    c, c, c, c, c, c, v, v, 
    c, c, c, c, v, v, v, v, 
    c, c, c, c, v, v, v, v, 
    c, c, c, c, c, c, c, v, 
    c, c, c, c, c, c, c, c, 
    c, c, c, c, c, c, c, c, 
  ]

sense.set_pixels(image)

sleep(1)

image = [
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, v, v,
    c, c, c, c, v, v, v, v, 
    c, c, v, v, v, v, b, v,
    c, c, v, v, v, v, v, v, 
    c, c, c, c, c, v, v, v, 
    c, c, c, c, c, c, v, v, 
    c, c, c, c, c, c, c, v,
  ]

sense.set_pixels(image)

sleep(1)

for i in range(0, 3):
    image = [
        c, c, c, c, c, c, c, c,
        c, c, c, c, v, v, c, c,
        c, c, v, v, v, v, v, c, 
        v, v, v, v, b, v, v, v,
        r, r, r, v, v, v, v, v, 
        v, v, v, v, v, v, v, v, 
        c, c, c, c, v, v, v, v, 
        c, c, c, c, c, v, v, v
      ]
    sense.set_pixels(image)
    sleep(1)
    image = [
        c, c, c, c, c, c, c, c,
        c, c, c, c, v, v, c, c,
        c, c, v, v, v, v, v, c, 
        v, v, v, v, b, v, v, v,
        v, v, v, v, v, v, v, v, 
        c, c, c, v, v, v, v, v, 
        c, c, c, c, v, v, v, v, 
        c, c, c, c, c, v, v, v
      ]
    sense.set_pixels(image)
    sleep(1)

for i in range(0, 200):
    b = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    v = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    image = [
        c, c, c, c, c, c, c, c,
        c, c, c, c, v, v, c, c,
        c, c, v, v, v, v, v, c, 
        v, v, v, v, b, v, v, v,
        v, v, v, v, v, v, v, v, 
        c, c, c, v, v, v, v, v, 
        c, c, c, c, v, v, v, v, 
        c, c, c, c, c, v, v, v
      ]
    sense.set_pixels(image)
    sleep(0.1)

