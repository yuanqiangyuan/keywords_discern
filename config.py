#!/usr/bin/python
# -*- coding: utf-8 -*-

ORACLE_CONF = {
"URL": "172.24.58.5:1521/orcl",#主机ip地址:端口/实例名,
"username":"data_pusher",
"password":"push_szsh",
"encoding":"UTF-8",
"tables":['e_baseinfo','e_li_black','e_inv_person'],
"comment":"Sensitive",
"row_num":50
}