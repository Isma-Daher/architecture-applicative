import random
import time
import sys
import pickle
import os.path

var_sauv = None
argent = 0
points = 0
e_resol = 0
e_ab = 0
ct = 0
espace = ' ' * 35
e = 0
nb_e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
indice_fournis = 0
max_indices = 2
améliorations = 0

niv_ = 0
essais_ = 0
pt = 0
ar_ = 0

en = ["Si cela cache, ce n'est que pour mieux révéler.\nCela bloque autant que cela permet de passer.\nLa réponse est dans la question.\nQue suis-je ?",
     "Je suis le commencement de l’effroi,\nLa fin de la durée et de l’espace,\nLe commencement de toutes extrémités,\nEt la fin de chaque contrée.\nQui suis-je ?",
     "Celui qui le fabrique le vend,\nCelui qui l'achète ne s'en sert pas,\nCelui qui s'en sert ne le sais pas.\nQu'est-ce ?",
     "Je serai hier, j'étais demain.",
      "Je suis si fragile que lorsque l'on prononce mon nom, je meurs.",
      "Je suis tout au bout de ta main,\nJe commence la nuit et je finis demain.",
      "Je me vide en me remplissant,\nEt je me remplis en me vidant,\nQue suis-je?",
      "Les feignant me vénèrent, mais je suis leur pire énemie.\nLes travailleurs me craignent mais je pourrais les soulager.\nQue suis-je ?",
      "Plus j'ai de gardien, moins je suis en sécurité\nMoins j'ai de gardien, plus je suis en sécurité.\nQue suis-je ?",
      "Une boite sans charnière, sans clé, sans couvercle.\nPourtant à l'intérieur est caché un trésor doré.",
      "Lors d'une guerre, un chevalier fut transpercé, il en mourrut,\nun deuxiéme guerrier fut décapité et les deux écuiers eurent la tête tranchée.\nCombien y a-t-il eu de morts ?",
      "Lumières qui fuient la lumière.",
      "Vivant sans souffle,\nFroid comme la mort,\nJamais assoiffé, toujours buvant,\nEn cotte de mailles, jamais cliquetant.",
      "Sans pieds, Sans mains, Sans ailes,\nje monte au ciel.",
      "Tellement magique qu'il vient à vous tous les soirs,\nIl vous emmène partout sans vous déplacer.\nPour le voir, vous devez d'abord fermer les yeux."]
repn = [("une enigme", "une énigme"),
       ("le e", " la lettre e", " le E"),
       "un cercueil",
       "aujourd'hui",
        "le silence",
        ("le n", "la lettre n", "le N"),
        "un sablier",
        "l'ennui",
        "un secret",
        "un oeuf",
        ("2", "deux"),
        ("les etoiles", "les étoiles"),
        "un poisson",
        ('une âme', 'une ame', 'la fumée', 'de la fumée'),
        ('le rêve', 'un rêve')]
indices = ["Cette énigme est une énigme de niveau 3, par conséquent il n'y a pas d'indice disponible",
           "la réponse comporte 4 caractère, déterminant et espace compris",
           "c'est matériel",
           "c'est un moment",
           "c'est immatériel",
           "la réponse comporte 4 caractère, déterminant et espace compris",
           "Cette énigme est une énigme de niveau 3, par conséquent il n'y a pas d'indice disponible",
           "long de 5 caractère (déterminant et espace(s) eventuel(s) non compris), ça commence par un 'e'",
           "c'est immatériel",
           "ne pas prendre les mots au pied de la lettre",
           "faire attention aux sens de 'eurent'",
           "Cette énigme est une énigme de niveau 3, par conséquent il n'y a pas d'indice disponible",
           "le poid du son",
           "Cette énigme est une énigme de niveau 3, par conséquent il n'y a pas d'indice",
           ""]
           
enigmes = {
    'e1' : en[0],
    'e2' : en[1],
    'e3' : en[2],
    'e4' : en[3],
    'e5' : en[4],
    'e6' : en[5],
    'e7' : en[6],
    'e8' : en[7],
    'e9' : en[8],
    'e10' : en[9],
    'e11' : en[10],
    'e12' : en[11],
    'e13' : en[12]
    }
rep_enigme = {
    'rep e1' : repn[0],
    'rep e2' : repn[1],
    'rep e3' : repn[2],
    'rep e4' : repn[3],
    'rep e5' : repn[4],
    'rep e6' : repn[5],
    'rep e7' : repn[6],
    'rep e8' : repn[7],
    'rep e9' : repn[8],
    'rep e10' : repn[9],
    'rep e11' : repn[10],
    'rep e12' : repn[11],
    'rep e13' : repn[12]
    }
idi = {
    'i 1' : indices[0],
    'i 2' : indices[1],
    'i 3' : indices[2],
    'i 4' : indices[3],
    'i 5' : indices[4],
    'i 6' : indices[5],
    'i 7' : indices[6],
    'i 8' : indices[7],
    'i 9' : indices[8],
    'i 10' : indices[9],
    'i 11' : indices[10],
    'i 12' : indices[11],
    'i 13' : indices[12]
    }

###Functions###