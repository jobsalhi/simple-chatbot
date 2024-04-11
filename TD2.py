#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 11:46:29 2023

@author: jvelcin
Cours d'introduction à l'IA (L2 Informatique, Université Lyon 2)

TD2 : Implémentation d'un robot conversationnel (V1)

"""

import re

# la liste des règles
reglesV1 = [
        ["bonjour1", "salut", "Salut à toi !"],
        ["bonjour2", "bonjour", "Salut humain"],
        ["presentation1", "mon nom est .*", "Enchanté :)"],
        ["presentation2", "je m'appelle *", "Enchanté :)"],
        ["presentation3", "je suis .*", "Enchanté :)"],
        ["bye", "by.*", "Au revoir :/"],
        ["au revoir", "au revoir", "Au revoir :/"]
    ]



c = ""
while (c != "bye" and c != "au revoir" ):
    c = input("> ") # le prompt
    rule_triggered = False
    for r in reglesV1:
        # est-ce que le motif est présent ? cf. TD 1
        pattern = re.compile(r[1])
        res = pattern.finditer(c)
        pos = [m.span() for m in res]
        # si le motif est présent, on affiche la réponse (3ème termes de la règle)
        if len(pos)>0:
            print(f" -> règle {r[0]} déclenchée !")
            print(r[2])
            rule_triggered = True
            break
    if not rule_triggered:
        print(" -> Aucune règle déclenchée.")
        print("Je ne sais pas.")