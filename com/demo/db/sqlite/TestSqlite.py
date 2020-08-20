#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/8/20 14:25
# @Author: yuzq
# @File  : TestSqlite
import sqlite3

if __name__ == '__main__':
    con = sqlite3.connect('example.db')
    cursor = con.cursor()

    create_table = '''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)'''
    # cursor.execute(create_table)
    insert_table = '''INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)'''
    # cursor.execute(insert_table)
    # con.commit()

    select_table = '''SELECT * FROM stocks WHERE symbol=?;'''
    # 这里传参使用元组
    # cursor.execute(select_table, ('RHAT',))
    # print(cursor.fetchone())

    purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
                 ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
                 ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
                 ]
    insert_tables = '''INSERT INTO stocks VALUES (?,?,?,?,?);'''
    cursor.executemany(insert_tables,purchases)
    con.commit()

    delete_table = '''delete from stocks where symbol = "IBM"'''
    cursor.execute(delete_table)
    con.commit()

    # print(cursor.fetchall())
    update_table = '''UPDATE stocks SET qty = 555 WHERE date = '2006-04-05' AND trans = 'BUY' AND symbol = 'MSFT' AND qty = 444 AND price = 72;'''
    cursor.execute(update_table)
    print(cursor.rowcount)
    con.commit()

    select_tables = '''SELECT * FROM stocks ORDER BY price'''
    cursor.execute(select_tables)
    for item in cursor.fetchall():
        print(item)
    cursor.close()
    con.close()
