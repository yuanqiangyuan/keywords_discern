#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyhanlp import *
import re

Segment = JClass("com.hankcs.hanlp.seg.Segment")
Term = JClass("com.hankcs.hanlp.seg.common.Term")
class hanlp_handler:
    def __init__(self, schema):
        self.schema = schema
        self.segment = HanLP.newSegment().enablePlaceRecognize(True) ###地名识别
        self.segment = HanLP.newSegment().enableNameRecognize(True)  ###人名
        self.segment = HanLP.newSegment().enableOrganizationRecognize(True) ###实体
    
    def Recognize(self, sentences):
        addr_count = 0
        name_count = 0
        entity_count = 0

        for sentence in sentences:
            if sentence == None:
                continue
            term_list = self.segment.seg(str(sentence))
            #print(term_list)
            keys = []
            for term in term_list:
                key_types = str(term).split('/')
                keys.append(key_types[1])
            if 'ns' in keys and 'nt' not in keys:
                #print('这是地址:', sentence)
                addr_count += 1
            if 'nt' in keys :
                #print('这是实体:', sentence)
                entity_count += 1
            if ('nr' in keys or 'nrf' in keys or 'nz' in keys) and 'ns' not in keys:
                #print('这是人名:', sentence)
                name_count += 1

        total = len(sentences)
        addr_rate = (addr_count / total ) * 100 
        name_rate = (name_count / total ) * 100
        entity_rate = (entity_count / total ) * 100

        if int(name_rate) >= 60 :
            return "Sensitive"
        elif int(addr_rate) >= 60 :
            return "Sensitive"
        elif int(entity_rate) >= 60:
            return "Sensitive"
        else:
            return "No"
    
    def Recognize_no_chinese(self, sentences):
        
        email = r"\w{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}"
        mobile = r"^1[3-9]\d{9}$"
        id_card = r"^[1-6]\d{5}[12]\d{3}(0[1-9]|1[12])(0[1-9]|1[0-9]|2[0-9]|3[01])\d{3}(\d|X|x)$"

        

        return "No"
     
