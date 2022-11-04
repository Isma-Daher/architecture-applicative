###IMPORTATIONS###
import random
import time
import sys
import pickle
import os.path

###VARIABLES ET DICOS###
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

###DEFINITIONS###
def saut():
    time.sleep(0.5)
    print()
    time.sleep(0.5)

def mcmd():
    saut()
    print("MAUVAISE COMMANDE")
    saut()

def sauver(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o):
    global var_sauv
    var_sauv = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o]
    fich_sauv = open("fich_sauv", "wb")
    pickle.dump(var_sauv, fich_sauv)
    fich_sauv.close()

def charger():
    global var_sauv, argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_
    fichier = "fich_sauv"
    if os.path.isfile(fichier):
        fich_sauv = open(fichier, 'rb')
        var_sauv = pickle.load(fich_sauv)
        fich_sauv.close()
        argent = var_sauv[0]
        points = var_sauv[1]
        e_resol = var_sauv[2]
        e_ab = var_sauv[3]
        ct = var_sauv[4]
        espace = var_sauv[5]
        e = var_sauv[6]
        nb_e = var_sauv[7]
        indice_fournis = var_sauv[8]
        max_indices = var_sauv[9]
        améliorations = var_sauv[10]
        niv_ = var_sauv[11]
        essais_ = var_sauv[12]
        pt = var_sauv[13]
        ar_ = var_sauv[14]
    else:
        print("Le fichier de sauvegarde '%s' n'existe pas" % fichier)
        
def tirer_enigme():
    global e
    global niv_
    global essais_
    global pt_
    global ar_

    if len(nb_e) == 0:
        saut()
        saut()
        print("BRAVO A VOUS !!!! VOUS AVEZ RESOLU TOUTES LES ENIGMES, VOUS AVEZ FINI LE JEU !!!!")
        print("/reset pour recommencer une partie en réinitialisant toutes les données. Sinon /leave")
        print("pour quitter définitivement")
        saut()
        choice = input()
        if choice == '/leave':
            sys.exit()
        elif choice == '/reset':
            commande.reset()
        elif choice not in ('/reset', '/leave'):
            mcmd()
            tirer_enigme()
    else:
        e = random.choice(nb_e)
        saut()
        print("...")
        saut()
        print("Tirage de l'enigme en cours...")
        saut()
        print("...")
        saut()
        print(enigmes['e%s' % e])
        nb_e.remove(e)
        if e in (2, 4, 6, 9, 11):
            niv_ = 1
            essais_ = 3
            pt_ = 1
            ar_ = random.randint(6, 18)
            sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
            repondre(niv_, essais_, pt_, ar_)
        elif e in (3, 5, 8, 10, 13):
            niv_ = 2
            essais_ = 2
            pt_ = 2
            ar_ = random.randint(18, 30)
            sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
            repondre(niv_, essais_, pt_, ar_)
        elif e in (1, 7, 12, 14):
            niv_ = 3
            essais_ = 2
            pt_ = 3
            ar_ = random.randint(30, 42)
            sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
            repondre(niv_, essais_, pt_, ar_)

def repondre(niv, essais, pt, ar):
    global points
    global e_resol
    global ct
    global e_ab
    global indice_fournis
    global argent
    rep = input()
    if rep in rep_enigme['rep e%s' % e] or rep == 'triche':
        saut()
        print("Bonne réponse !!!!")
        ct = 0
        points = points + pt
        argent += ar
        e_resol = e_resol + 1
        print("+ %s point !!" % pt)
        print("+ %s$ !!" % ar)
        sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
        commande.help()
    elif rep == '/abandon':
        saut()
        e_ab = e_ab + 1
        print("Très bien...")
        saut()
        print("points : %s" % points)
        nb_e.append(e)
        sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
        commande.help()
    elif rep == '/indice':
        if indice_fournis in (0, 1):
            saut()
            print(idi['i %s' % e])
            if idi['i %s' % e] == "Cette énigme est une énigme de niveau %s, par conséquent il n'y a pas d'indice disponible" % niv:
                pass
            else:
                indice_fournis += 1
        elif indice_fournis == max_indices:
            saut()
            print("Vous avez déjà eu tous vos indices !!")
        repondre(niv_, essais_, pt_, ar_)
    elif rep == '/niveau':
        saut()
        print("enigme de niveau %s" % niv)
        repondre(niv_, essais_, pt_, ar_)
    elif '/' in rep:
        mcmd()
        repondre(niv_, essais_, pt_, ar_)
    else:
        while rep != rep_enigme['rep e%s' % e]:
            ct = ct + 1
            saut()
            print("Mauvaise réponse !")
            saut()
            rep = input()
            if rep in rep_enigme['rep e%s' % e]:
                saut()
                print("Bonne réponse !!!!")
                if ct > essais:
                    print("%s réponses ou plus ont été écrites donc vous ne gagnez pas de points à cette énigme-ci..." % essais)
                    commande.help()
                else:
                    points = points + pt
                    argent += ar
                e_resol = e_resol + 1
                ct = 0
                print("+ %s point !!" % pt)
                print("+ %s$ !!" % ar)
                sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
                commande.help()
            elif rep == '/abandon':
                saut()
                e_ab = e_ab + 1
                ct = 0
                print("Très bien...")
                saut()
                print("points : %s" % points)
                sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
                commande.help()
            elif rep == '/indice':
                if indice_fournis in (0, 1):
                    saut()
                    print(idi['i %s' % e])
                    if idi['i %s' % e] == "Cette énigme est une énigme de niveau %s, par conséquent il n'y a pas d'indice disponible" % niv:
                        pass
                    else:
                        indice_fournis += 1
                elif indice_fournis == max_indices:
                    saut()
                    print("Vous avez déjà eu tous vos indices !!")
                repondre(niv_, essais_, pt_, ar_)
            elif rep == '/niveau':
                saut()
                print("enigme de niveau %s" % niv)
                repondre(niv_, essais_, pt_, ar_)
            elif '/' in rep:
                mcmd()
                repondre(niv_, essais_, pt_, ar_)

class commande():
    def help():
        global nb_e
        saut()
        cmd = input("Tapez /help pour connaitre toutes les commande de jeu.\n(Vous pouvez taper directement la commande voulue au lieu\nde passer par /help si vous connaissez la commande souhaitée) : ")
        if cmd == '/help':
            saut()
            print("/enigme : tirer une énigme au hasard\n/stat : voir ses statistiques\n/leave : quitter la partie(attention, si vous quitter, rien ne sera enregistré !)\n/rules : voir les règles du jeu\n/shop : acéder au magasin")
            print("/reset : réinitialiser le jeu")
            commande.help()
        elif cmd == '/stat':
            commande.info()
        elif cmd == '/leave':
            commande.leave()
        elif cmd == '/enigme':
            tirer_enigme()
        elif cmd == '/rules':
            commande.rules()
        elif cmd == '/config':
            commande.config_niveau()
        elif cmd == '/shop':
            commande.shop()
        elif cmd == '/reset':
            commande.reset()
        else:
            cm = False
            while cm == False:
                mcmd()
                cmd = input()
                if cmd == '/help':
                    saut()
                    print("/enigme : tirer une énigme au hasard\n/stat : voir ses statistiques\n/leave : quitter la partie(attention, si vous quitter, rien ne sera enregistré !)\n/rules : voir les règles du jeu")
                    cm = True
                    commande.help()
                if cmd == '/stat':
                    cm = True
                    commande.info()
                elif cmd == '/leave':
                    cm = True
                    commande.leave()
                elif cmd == '/enigme':
                    cm = True
                    tirer_enigme()
                elif cmd == '/rules':
                    cm = True
                    commande.rules()
                elif cmd == '/config':
                    cm = True
                    commande.config_niveau()
                elif cmd == '/shop':
                    cm = True
                    commande.shop()
                elif cmd == '/reset':
                    cm = True
                    commande.reset()
                        
    def info():
        global max_indices
        global améliorations
        saut()
        if points >= 10 and points < 20:
            améliorations += 1
            if améliorations == 1:
                print("BRAVO !! Vous avez atteint les 10 points ou plus !\nVous débloquez 1 indice suplémentaire !!")
                max_indices += 1
        elif points >= 20:
            améliorations += 1

            if améliorations == 2:
                print("BRAVO !! Vous avez atteint les 20 points ou plus !\nVous débloquez 2 indice suplémentaire !!")
                max_indices += 2
            elif améliorations == 1:
                print("BRAVO !! Vous avez atteint les 10 points ou plus !\nVous débloquez 1 indice suplémentaire !!")
                max_indices += 1
                saut()
                améliorations += 1
                print("BRAVO !! Vous avez atteint les 20 points ou plus !\nVous débloquez 2 indice suplémentaire !!")
                max_indices += 2
        print("Vos statistiques :\n\npoints : %s\nnb d'énigme résolues : %s\nenigmes abandonnées : %s\nvotre argent : %s$\nindices disponibles : %s\nindices utilisés : %s" % (points, e_resol, e_ab, argent, (max_indices - indice_fournis), indice_fournis))
        saut()
        sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
        commande.help()
    def leave():
        saut()
        sur = input("Êtes-vous sur (oui/non) ? ")
        if sur == 'oui':
            saut()
            print("Très bien...")
            sys.exit()
        elif sur == 'non':
            saut()
            print("Ok")
            commande.help()
        else:
            mcmd()
            commande.leave()
    def rules():
        saut()
        rules = open("D:/python/enigme/rules.txt", encoding="utf8")
        R = rules.read()
        print(R)
        saut()
        p = input("vous pouvez faire /config ou 'pass' pour retrouner à l'accueil : ")
        if p == '/config':
            commande.config_niveau()
        elif p == 'pass' or "'pass'":
            saut()
            print("Très bien...")
            commande.help()
        else:
            while p != '/config' or 'pass' or "'pass'":
                mcmd()
                p = input("vous pouvez faire /config ou 'pass' pour retrouner à l'accueil : ")
                if p == '/config':
                    commande.config_niveau()
                elif p == 'pass' or "'pass'":
                    commande.help()
    def config_niveau():
        saut()
        print("Caractérisiques des niveaux : \n\nniveau 1 : 1 indice possible\n           3 essais avant l'anulation du comptage des points de l'enigme\n           rapporte 1 point\n           rapporte entre 6 et 18$\nniveau 2 : 1 indice possible\n           2 essais possibles avant l'anunulation du comptage des points\n           rapporte 2 points\n           rapporte entre 18 et 30$\nniveau 3 : aucun indices possibles\n           2 essais avant l'anulation du comptage des points\n           rapporte 3 points\n           rapporte entre 30 et 42$.")
        commande.help()

    def shop():
        global max_indices
        global argent
        saut()
        SHOP = open("d:/python/enigme/shop.txt", encoding="utf8")
        shop = SHOP.read()
        print(shop)
        saut()
        print("argent : %s" % argent)
        saut()
        print("Tapez ici le numéro de l'article que vous voulez acheter, sinon 'pass' pour fermer le shop :")
        choix = input()
        if choix in ('pass', "'pass'"):
            saut()
            print("Très bien ")
            print("Revenez vite !")
            saut()
            commande.help()
        elif choix in ("1", "1)"):
            if argent >= 70:
                saut()
                max_indices += 1
                argent -= 70
                print("Super !")
                print("Merci, revenez vite !")
                saut()
                print("argent : %s" % argent)
                saut()
                sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
                commande.help()
            else:
                saut()
                print("Vous n'avez pas assez d'argent :(")
                commande.help()
        elif choix in ("2", "2)"):
            if argent >= 135:
                saut()
                max_indices += 2
                argent -= 135
                print("Super !")
                print("Merci, revenez vite !")
                saut()
                print("argent : %s" % argent)
                saut()
                sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
                commande.help()
            else:
                saut()
                print("Vous n'avez pas assez d'argent :(")
                commande.help()
        elif choix in ('3', '3)'):
            if argent >= 195:
                saut()
                max_indices += 3
                argent -= 195
                print("Super !")
                print("Merci, revenez vite !")
                saut()
                print("argent : %s" % argent)
                saut()
                sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
                commande.help()
            else:
                saut()
                print("Vous n'avez pas assez d'argent :(")
                commande.help()
        elif choix in ('4', '4)'):
            if argent >= 50:
                saut()
                print("Alors...")
                saut()
                print("...")
                saut()
                print("Vous n'avez pas le droit à un indice et vous n'avez qu'un essais !!")
                saut()
                print("Quelle est la couleur du cheval blanc d'henri IV ??")
                rep = input()
                if rep == 'blanc':
                    saut()
                    print("BRAVO !!! C'était difficile non ?")
                    argent_argent = random.randint(10, 20) * 3
                    saut()
                    print("+ %s$ !" % argent_argent)
                    print("+ 6 points !")
                    argent += argent_argent
                    points += 6
                    sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
                    commande.help()
                else:
                    saut()
                    print("raté ! c'était facile pourtant !")
                    commande.help()
            else:
                saut()
                print("Vous n'avez pas assez d'argent :(")
                commande.help()
        elif choix in ('5', '5)'):
            if argent >= 30:
                saut()
                print("Voulez-vous vraiment savoir l'information ultra-confidentielle?")
                saut()
                print("En fait comme vous avez deja payé je vais la dire... :)")
                saut()
                saut()
                print("LES CHAUSSETTES DE L'ARCHIDUCHESSE SONT SECHES !! PAS ARCHISECHES !!!!")
                commande.help()
            else:
                saut()
                print("Vous n'avez pas assez d'argent :(")
                commande.help()
        else:
            mcmd()
            commande.shop()
    def reset():
        global var_sauv, argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_
        argent = 0
        points = 0
        e_resol = 0
        e_ab = 0
        ct = 0
        e = 0
        indice_fournis = 0
        améliorations = 0
        niv_ = 0
        essais_ = 0
        pt_ = 0
        ar_ = 0
        nb_e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        max_indices = 2
        saut()
        saut()
        time.sleep(1)
        str = "Réinitialisation terminée !!"
        x = str.center(153, "-")
        print(x)
        saut()
        saut()
        sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
        commande.help()

###BOUCLE PRINIPALE###

print()
print()
s = "BIENVENUE DANS UN JEU D'ENIGMES !!!"
xx = s.center(153, '=')
print(xx)
saut()
charger()
saut()
commande.help()
