#!/usr/bin/python
# -*- coding: utf-8 -*-

import config as app_config

from oracle_handler import oracle_handler


test = oracle_handler()

conn, cursor = test.connect()

tables = app_config.ORACLE_CONF['tables']
row_num = app_config.ORACLE_CONF['row_num']
for table in tables:
    print(table)
    keys = test.find_Sensitive_columns(table, row_num)
    print(keys)
    for key in keys:
        test.comment_Sensitive_columns(table, key, app_config.ORACLE_CONF['comment'])



cursor.close()
conn.close()
