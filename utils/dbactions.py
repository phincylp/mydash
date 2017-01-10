#!/usr/bin/python
import config, MySQLdb, engine


def mysql_conn(dbhost):
        user, passwd = config.dbhost_connect()
        dbconn = MySQLdb.connect(host=dbhost, user=user, passwd=passwd, db='mysql')
        dbcur = dbconn.cursor()
        return dbconn, dbcur
def mysql_dash():
	user, passwd, db = config.dash_mysql()
	conn = MySQLdb.connect(host='localhost', user=user, passwd=passwd, db=db)
	cur = conn.cursor()
	return conn, cur
def createDB(dbhost, dbname):
	dbconn, dbcur = mysql_conn(dbhost)
	createdbsql = "create database %s" % (dbname)
	createtabsql = "create table %s.dummy (dummy int)" %(dbname)
	attempt = 0
	try:
		dbcur.execute('show slave status')
		result=dbcur.fetchall()
		if not result:
			dbcur.execute(createdbsql)
			dbconn.commit()
			dbcur.execute(createtabsql)
			dbconn.commit()
			dbconn.close()
			return True
		else:
			dbconn.close()
			status="This is slave box. Please try on MASTER"
			return status
	except MySQLdb.Error as e:
		dbconn.close()
		return e

def createUser(dbhost, user, dbname, role, passw):
	if role == 'ro':
		sql = "grant select on %s.* to '%s'@'10.%%' identified by '%s'" % (dbname, user, passw)
	else:
		sql = "grant select, insert, update, delete, create on %s.* to '%s'@'10.%%' identified by '%s'" % (dbname, user, passw)
	dbconn, dbcur = mysql_conn(dbhost)
	try:
		if dbname:
			dbcur.execute('show slave status')
			result=dbcur.fetchall()
			if not result:
				checksql = "select User from mysql.user where User='%s'" % (user)
				dbcur.execute(checksql)
				check = dbcur.fetchall()
				if not check:
					dbcur.execute(sql)
					dbcur.execute('flush privileges')
					dbconn.close()
					return True
				else:
					dbconn.close()
					status = "User Already exists"
					return status
			else:
	                        dbconn.close()
	                        status="This is slave box. Please try on MASTER"
	                        return status
		else:
			dbconn.close()
			status="Database not selected. You need to create a database first"
			return status
	except MySQLdb.Error as e:
		dbconn.close()
		return e
	

def update_inventrory(dbhost, cluster_name, master):
	conn, cur = mysql_dash()
	if not master:
		sql = "insert into inventory (dbhost, cluster_name, master_host, status, cluster_status) VALUES ('%s', '%s', '%s', %d, %d)" % (dbhost, cluster_name, 'None', 1, 1)
	else:
		sql = "insert into inventory (dbhost, cluster_name, master_host, status, cluster_status) VALUES ('%s', '%s', '%s', %d, %d)" % (dbhost, cluster_name, master, 1, 1)

	try:
		cur.execute(sql)
		conn.commit()
		conn.close()
		success = True
		message = 'Success'
	except MySQLdb.Error as e:
		conn.close()
		success = 'No'
		message = e
	return success, message
	
def hostadd(dbhost, cluster_name):
	conn, cur = mysql_dash()
	sql = "select * from inventory where dbhost='%s'" % (dbhost)
	cur.execute(sql)
	data = cur.fetchall()
	if not data:  # Proceed if host is not found in inventory
		slave = engine.slaveStatus(dbhost)
		if not slave:    # This is a master host
			sql = "select * from inventory where cluster_name='%s'" % (cluster_name)
			cur.execute(sql)
			data = cur.fetchall()
			if not data: # proceed only if the cluster name is not already used
				master = None
				success, message = update_inventrory(dbhost, cluster_name, master)
				if success == True:
					status = True
					message = 'Success'
				else:
					status = 'No'
					message = message
			else:
				status = "Fail"
				message = "Cluser Name already in  use"
		else:
			master = slave['Master_Host']
			mastercheck = "select cluster_name from inventory where dbhost='%s'" % (master)
			cur.execute(mastercheck)
			data = cur.fetchall()
			if data:
				if not data[0][0] == cluster_name:
					success = 'No'
					message = 'Master of this host is already in a cluster named : %s' % (data[0][0])
				else:
					success, message = update_inventrory(dbhost, cluster_name, master)
			else:
				success, message = hostadd(master, cluster_name) # considering the fact that nested replication may come up.
#				success, message = update_inventrory(master, cluster_name,
