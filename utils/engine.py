#!/usr/bin/python

import MySQLdb
import config
# Create a mysql connection to the dbhost

def mysql_dbhost(dbhost):
        user, passwd = config.dbhost_connect()
        dbconn = MySQLdb.connect(host=dbhost, user=user, passwd=passwd, db='mysql')
        dbcur = dbconn.cursor()
        return dbconn, dbcur
def mysql_conn(dbhost):
	user, passwd = config.dbhost_connect()
	dbconn = MySQLdb.connect(host=dbhost, user=user, passwd=passwd, db='mysql')
	dbcur = dbconn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
	return dbconn, dbcur

def enginStats(dbhost):
	dbconn, dbcur = mysql_conn(dbhost)
	sql = "show engine innodb status"
	dbcur.execute(sql)
	data = dbcur.fetchall()
	data = data[0]
	status = data['Status']
	return status
def serverVars(dbhost):
        dbconn, dbcur = mysql_conn(dbhost)
        sql = "show variables"
	varlist = []
	varvals = []
        dbcur.execute(sql)
        data = dbcur.fetchall()
	for i in range(len(data)):
		elem = data[i]
		vals = elem.values()
		varlist.append(vals[1])
		varvals.append(vals[0])
		
	servervars = dict(zip(varlist, varvals))
	return servervars
def serverStats(dbhost):
        dbconn, dbcur = mysql_conn(dbhost)
        sql = "show status"
        varlist = []
        varvals = []
        dbcur.execute(sql)
        data = dbcur.fetchall()
        for i in range(len(data)):
                elem = data[i]
		vals = elem.values()
                varlist.append(vals[1])
                varvals.append(vals[0])

        serverstats = dict(zip(varlist, varvals))
        return serverstats
def slaveStatus(dbhost):
	dbconn, dbcur = mysql_conn(dbhost)
	sql = "show slave status"
	dbcur.execute(sql)
	data = dbcur.fetchall()
	if data:
		data =  data[0]
	else:
		data = None
	return data
def fullProcess(dbhost):	
	dbconn, dbcur = mysql_conn(dbhost)
	sql = "SELECT ROWS_EXAMINED, ROWS_SENT, DB, STATE, HOST, COMMAND, USER, TIME, ID, INFO FROM information_schema.processlist order by TIME DESC"
	dbcur.execute(sql)
	data = dbcur.fetchall()
	return data

if __name__ == "__main__":
        dbhost='flo-warehouse-b2b-db-10.nm.domain.com'
        varss = serverVars(dbhost)
        #print varss
	status = enginStats(dbhost)
	eginstat=status.split('\n')
	#for i in range(len(eginstat)):
	#	print eginstat[i]
	data = serverStats(dbhost)	
#	print data
	slave = slaveStatus(dbhost)
	print slave
#	print type(varss['ssl_crl'])
	data = fullProcess(dbhost)
#	for i in range(len(data)):
#		dictio = data[i]
#		print dictio.keys()
#	print data


