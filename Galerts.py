# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:18:43 2017

@author: 1537259
"""
import sys
sys.path.append("lib/galerts.py")

import galerts

gam = galerts.GAlertsManager('umeshdhanwal', '')

query = 'Cake Man Cornelius'
type = galerts.TYPE_COMPREHENSIVE
gam.create(query, type)
list(gam.alerts)
alert.feedurl

