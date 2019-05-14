# -*- coding: utf-8 -*-
"""
Created on Wed Dec 5 09:29:34 2018

@author: cokelaef
"""

"""
    Transaction Class 
    ----------
    Keep track of request history
"""

class Transaction:

    def __init__(self, datetime, duration, FPInput, FPOutputs, comments, username, serviceName, serviceVersion):
        self.datetime = datetime
        self.duration = duration
        self.FPInput = FPInput
        self.FPOutputs = FPOutputs
        self.comments = comments
        self.username = username
        self.serviceName = serviceName
        self.serviceVersion = serviceVersion