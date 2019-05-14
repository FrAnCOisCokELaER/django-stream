# -*- coding: utf-8 -*-
"""
Created on Wed Dec 5 09:29:34 2018

@author: cokelaef
"""

"""
    Comments Class 
    ----------
    Keep track of request history
"""

class Comment:
    def __init__(self, comment, errorCode, severity):
        self.comment = comment
        self.errorCode = errorCode
        self.severity = severity