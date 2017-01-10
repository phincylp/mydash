#!/usr/bin/python

import re
import MySQLdb
import sys
import cgi
import config
# Create a MySQL connection to dahsboard database
def mysql_con():
        user, passwd, db = config.dash_mysql()

        conn = MySQLdb.connect(host='localhost', user=user, passwd=passwd, db=db)
        cur=conn.cursor()
        return conn, cur

# Create a mysql connection to the dbhost

def mysql_dbhost(dbhost, dbname):
	user, passwd = config.dbhost_connect()
	dbconn = MySQLdb.connect(host=dbhost, user=user, passwd=passwd, db=dbname)
	dbcur = dbconn.cursor()
	return dbconn, dbcur


def mysql_conn(dbhost):
        user, passwd = config.dbhost_connect()
        dbconn = MySQLdb.connect(host=dbhost, user=user, passwd=passwd, db='mysql')
        dbcur = dbconn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        return dbconn, dbcur


def dataInfo(dbhost):
	dbconn, dbcur = mysql_conn(dbhost)
	datasql = "show databases"
	dbcur.execute(datasql)
	data = dbcur.fetchall()
	database_list = []
	datasize_list = []
	for i in range(len(data)):
		dictio = data[i]
		db = dictio['Database']
		database_list.append(db)
		sizesql = """SELECT table_schema AS "Database name", SUM(data_length + index_length) / 1024 / 1024 AS "Size (MB)"  FROM information_schema.TABLES where table_schema='%s' GROUP BY table_schema""" % (db)
		dbcur.execute(sizesql)
		sizedata = dbcur.fetchall()
		if sizedata:
			sizedict = sizedata[0]
			size = sizedict['Size (MB)']
			if size:
				datasize_list.append(size)
			else:
				size = 0
				datasize_list.append(size)
		else:
			size = 0
			datasize_list.append(size)
	return database_list, datasize_list



def tableInfo(dbhost, dbname):
	user, passwd = config.dbhost_connect()
	dbconn, dbcur = mysql_dbhost(dbhost, 'mysql')
	tabsql= """ SELECT table_name AS "Table",  round(((data_length + index_length) / 1024 ), 2) "Size in KB", ENGINE, TABLE_COLLATION  FROM information_schema.TABLES  WHERE table_schema = "%s"; """  % (dbname)
	dbcur.execute(tabsql)
	tab_tup=dbcur.fetchall()
        tab_list=list(tab_tup)
        table_list=[]
        tabsize_list=[]
	tab_engine=[]
	tab_coll=[]
        for elem in tab_list:
                elem_string=str(elem)
                elem_list=elem_string.split("'")
                tabname=elem_list[1]
                table_list.append(tabname)
                tabsize=elem_list[3]
                tabsize_list.append(tabsize)
		tabengine=elem_list[5]
		tab_engine.append(tabengine)
		tabcol=elem_list[7]
		tab_coll.append(tabcol)
        return table_list, tabsize_list, tab_engine, tab_coll

def tabSchema(dbhost, dbname, tabname):
	dbconn, dbcur = mysql_dbhost(dbhost, dbname)
	schesql= """desc %s """ % (tabname)
	dbcur.execute(schesql)
	sche_tup = dbcur.fetchall()
        num_fields = len(dbcur.description)
        field_names = [i[0] for i in dbcur.description]
	desc_list=[]
	for tup_elem in sche_tup:
		list_tup=list(tup_elem)
		for elem in range(len(list_tup)):
			if list_tup[elem] == None:
				list_tup[elem] = 'Null'
			if list_tup[elem] == '':
				list_tup[elem] ='-'
		desc_list.append(list_tup)
	return field_names, desc_list

if __name__ == "__main__":
        dbhost='retail-cpl-db2.nm.domain.com'
        database_list, datasize_list = dataInfo(dbhost)
	print database_list, datasize_list
