#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def creat_horse(nb) :

	horse = []
	for i in range(nb) :
		horse.append({
			"nom": f"Chevaux {i+1}",
			"vitesse": 0,
			"distance":0,
			"disqualifie": False
		})
	return horse

def dice_roll():
	"""Renvoie un nombre de dé aleatoire entre 1 et 6"""
	return random.randint(1,6)

def speed_evolution(speed, roll) :
	"""Retourne la nouvelle vitesse selon le tableau donner"""
	table = {
		0: [0, +1, +1, +1, +2, +2],
		1: [0, 0, +1, +1, +1, +2],
		2: [0, 0, +1, +1, +1, +2],
		3: [-1, 0, 0, +1, +1, +1],
		4: [-1, 0, 0, 0, +1, +1],
		5: [-2, -1, 0, 0, 0, +1],
		6: [-2, -1, 0, 0, 0, "DQ"],
	}
	variation = table[speed][roll-1]
	if variation == "DQ" :
		return None 	# disqualification
	return max(0, speed + variation)

