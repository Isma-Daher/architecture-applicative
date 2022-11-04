import random
import time
import sys
import pickle
import os.path

import definitions
import commandes

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
            commandes.commande.reset()
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
        commandes.commande.help()
    elif rep == '/abandon':
        saut()
        e_ab = e_ab + 1
        print("Très bien...")
        saut()
        print("points : %s" % points)
        nb_e.append(e)
        sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
        commandes.commande.help()
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
                    commandes.commande.help()
                else:
                    points = points + pt
                    argent += ar
                e_resol = e_resol + 1
                ct = 0
                print("+ %s point !!" % pt)
                print("+ %s$ !!" % ar)
                sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
                commandes.commande.help()
            elif rep == '/abandon':
                saut()
                e_ab = e_ab + 1
                ct = 0
                print("Très bien...")
                saut()
                print("points : %s" % points)
                sauver(argent, points, e_resol, e_ab, ct, espace, e, nb_e, indice_fournis, max_indices, améliorations, niv_, essais_, pt, ar_)
                commandes.commande.help()
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