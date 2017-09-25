# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:18:43 2017

@author: 1537259
"""

import galerts

gam = galerts.GAlertsManager('umeshdhanwal@gmail.com', 'diamondcouch14')

query = 'Cake Man Cornelius'
type = galerts.TYPE_COMPREHENSIVE
gam.create(query, type)
list(gam.alerts)
alert.feedurl

