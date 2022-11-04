import random
import time
import sys
import pickle
import os.path

def saut():
    time.sleep(0.5)
    print()
    time.sleep(0.5)

def mcmd():
    saut()
    print("MAUVAISE COMMANDE")
    saut()

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