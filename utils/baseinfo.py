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


def basInfo(dbhost):
# Getting version information
	user, passwd = config.dbhost_connect()
	try:
		dbconn = MySQLdb.connect(host=dbhost, user=user, passwd=passwd, db='mysql')
		running = True
		dbconn.close
	except MySQLdb.Error as e:
		running = 'No'
	base_par_list = []
	base_val_list = []
	if running == True:
		base_par_list.append('running')	
		base_val_list.append('True')
		dbconn, dbcur = mysql_conn(dbhost)
		versionsql = """show variables like "%version%" """
		dbcur.execute(versionsql)
		ver_tup = dbcur.fetchall()
		for i in range(len(ver_tup)):
			ver_dict = ver_tup[i]
			val = ver_dict['Value']
			var = ver_dict['Variable_name']
			base_par_list.append(var)
			base_val_list.append(val)
	
		dirsql= """show variables like "%dir%" """
		dbcur.execute(dirsql)
		dir_tup = dbcur.fetchall()
		for i in range(len(dir_tup)):
			dir_dict = dir_tup[i]
			val = dir_dict['Value']
	        	var = dir_dict['Variable_name']
			base_par_list.append(var)
			base_val_list.append(val)
	
		getslavesql = 'show slave status'
	        attempt=0
	        while attempt < 3:
	                try:
	                        dbcur.execute(getslavesql)
	                        getslaveval_tup=dbcur.fetchall()
	                        break
	                except:
	                        attempt += 1
	        if getslaveval_tup:
	                slavedict=getslaveval_tup[0]
	                slave_of=slavedict['Master_Host']
	                lag_by=slavedict['Seconds_Behind_Master']
			slave_sql = slavedict['Slave_SQL_Running']
			slave_io = slavedict['Slave_IO_Running']
	        else:
	                slave_of='None'
	                lag_by='None'
			slave_sql = 'Not Applicable'
			slave_io = 'Not Applicable'
		lag_by=str(lag_by)
	        base_val_list.append(slave_of)
	        base_val_list.append(lag_by)
		base_val_list.append(slave_sql)
		base_val_list.append(slave_io)
		base_par_list.append('Master_Host')
		base_par_list.append('Seconds_Behind_Master')
		base_par_list.append('Slave_SQL_Running')
		base_par_list.append('Slave_IO_Running')
		
		readsql = "show variables like 'read_only'"
		dbcur.execute(readsql)
		read_tup = dbcur.fetchall()
		for i in range(len(read_tup)):
			read_dict = read_tup[i]
			val = read_dict['Value']
			var = read_dict['Variable_name']
			base_par_list.append(var)
			base_val_list.append(val)
		
	        dbconn.close()
        else:
                base_par_list.append('running')
                base_val_list.append('No')
		
	return base_val_list, base_par_list


if __name__ == "__main__":
        dbhost='retail-cpl-db-1.nm.domain.com'
        data, data1 = basInfo(dbhost)
        print data
	print len(data)
	print data1
	print len(data1)
	base_dict = dict(zip(data1, data))
	print base_dict
