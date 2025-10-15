#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def creer_chevaux(nb) :

	chevaux = []
	for i in range(nb) :
		chevaux.append({
			"nom": f"Chevaux {i+1}",
			"vitesse": 0,
			"distance":0,
			"disqualifie": False
		})
	return chevaux

