#!/usr/bin/python
# -*- coding: utf-8 -*-


import datetime
import cx_Oracle
import config as app_config
from hanlp_handler import hanlp_handler
class oracle_handler:
    def __init__(self):
        self.oracle_config  = app_config.ORACLE_CONF
        self.conn_oracle =  None
        self.cursor_oracle = None

    def connect(self):
        conn_oracle = cx_Oracle.connect(self.oracle_config['username'], self.oracle_config['password'],
                                        self.oracle_config['URL'], encoding=self.oracle_config['encoding'])

        cursor_oracle = conn_oracle.cursor()
        self.conn_oracle = conn_oracle
        self.cursor_oracle = cursor_oracle
        return conn_oracle, cursor_oracle
    
    def find_Sensitive_columns(self, table_name, row_num):

        sensitive_keys = []
        print("Find out the sensitive columns start")
        if self.conn_oracle == None or self.cursor_oracle == None:
            print("please connect to oracle db first")
            return sensitive_keys
        
        sql_str = 'select * from ' + table_name + ' where rownum<=' + str(row_num)

        print(sql_str)

        res = self.cursor_oracle.execute(sql_str)#'select * from e_baseinfo where rownum<=5')

        title = [i[0] for i in self.cursor_oracle.description]
        #print(title)
        data = res.fetchall()
        check_datas = {}
        
        for row in data:
           for colume , item in zip(title, row):
               #print(colume, ':', item)
               if colume not in check_datas :
                  check_datas[colume] = []
               if item != None:
                  check_datas[colume].append(item)

        hanlp_hd = hanlp_handler('test')
        
        for key in check_datas:
            #print(key)
            #print(check_datas[key])
            if len(check_datas[key]) == 0:
                continue
            if isinstance(check_datas[key][0], datetime.datetime) or isinstance(check_datas[key][0], cx_Oracle.LOB):
                continue
            result = hanlp_hd.Recognize(check_datas[key])
            print(key,':',result)
            if result == 'Sensitive':
               sensitive_keys.append(key)
        return sensitive_keys

    def comment_Sensitive_columns(self, table, key, comment):

        sql_str = "comment on column " + table + "." + key + " is '" + comment + "'"
        print(sql_str)
        print("comment sensitive columns start")

        res = self.cursor_oracle.execute(sql_str)
        print(res)

