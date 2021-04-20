#!/usr/bin/python
# -*- coding: utf8 -*-

class Exchange(object):
    _singleton = None
    def __init__(self, obj, adaptedMths):
        self.obj = obj
        self.__dict__.update(adaptedMths)
        self.adapter = []
        
    def setAdapter(self):
        """
        something...
        """
        if self.obj not in self.adapter:
            self.adapter.append(self.obj)
        return self.adapter

    def __getattr__(self, attr):
        """
        something...
        """
        return getattr(self.obj, attr)

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(Exchange, cls).__new__(cls)  
        return cls._singleton


