#!/usr/bin/python
import config
import MySQLdb

def mysql_dash():
        user, passwd, db = config.dash_mysql()
        dbconn = MySQLdb.connect(host='localhost', user=user, passwd=passwd, db=db)
        dbcur = dbconn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        return dbconn, dbcur

def getHosts():
	user, passwd, db = config.dash_mysql()
	dbconn, dbcur = mysql_dash()
	sql = "select dbhost from inventory where status = 1"
	dbcur.execute(sql)
	data = dbcur.fetchall()
	hostlist = []
	for i in range(len(data)):
		host = data[i].values()
		hostlist.append(host[0])
	return hostlist

def getClusters():
	user, passwd, db = config.dash_mysql()
	dbconn, dbcur = mysql_dash()
	sql = "select cluster_name from inventory where cluster_status = 1"
	dbcur.execute(sql)
	data = dbcur.fetchall()
	cluslist = []
	for i in range(len(data)):
		clus = data[i].values()
		cluslist.append(clus[0])
	clusters = list(set(cluslist))
	return clusters
	
	
if __name__ == "__main__":
	hostlist = getHosts()
	clusters = getClusters()
	print hostlist
	print clusters
