#!/usr/bin/python

import config, template, database, engine
import cgi

formdata = cgi.FieldStorage()
dbhost = formdata.getvalue('dbhost')
base_url = config.base_url()
#user = 'opsdshro'
passwd = '0pzR0Pass'
port = '3306'

def createTempUser(dbhost, role):
	dbconn, dbcur = database.mysql_dbhost(dbhost, 'mysql')
	database_list, datasize_list = database.dataInfo(dbhost)
	if  role == 'ro':
		user='opsdsh_ro'
		for db in  database_list:
			if db == 'mysql':
				continue
			elif db == 'information_schema':
				continue
			elif db == 'performance_schema':
				continue
			else:			
				sql = "grant select on `%s`.* to %s@'10.%%' identified by '%s'" % (db, user, passwd)
				dbcur.execute(sql)
	if  role == 'rw':
		user='opsdsh_rw'
		for db in  database_list:
			if db == 'mysql':
				continue
			elif db == 'information_schema':
				continue
			elif db == 'performance_schema':
				continue
			else:
				sql = "grant select, drop, insert, update, delete, alter, create on `%s`.* to '%s'@'10.%%' identified by '%s'" % (db, user, passwd)
				dbcur.execute(sql)
	dbconn.close()
	return user

def connnDet(dbhost):
	data = engine.slaveStatus(dbhost)
	if data:
		hosttype = 'Slave'
		conntype = 'Read Only'
		role = 'ro'
	else:	
		hosttype = 'Master'
		conntype = 'Read/Write'
		role = 'rw'
	return hosttype , conntype, role

def connectForm(dbhost, hosttype, conntype, port, user, passwd):
	print ("""

    <br>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <h3 class="text-info">
                    Connect to DB Console
                </h3>
			<br>
			<table class="table table-condensed" style="border: 1px solid #DDD;">
				<thead>
				</thead>
				<tbody>
					<tr>
						<td> Host</td>
						<td> Type </td>
						<td> Connection </td>
					</tr>
					<tr>
						<td> %s </td>
						<td> %s </td>
						<td> %s </td>
					</tr>
				</tbody>
			</table>
        	        <br>
			<form method="post" action="phpmyadmin/scripts/signon.php">
				<input type="hidden" name="host" value='%s' class="form-control col-lg-5">
				<input type="hidden" name="port" value='%s' class="form-control col-lg-5">
				<input type="hidden" name="user" value='%s' class="form-control col-lg-5">
				<input type="hidden" name="password" value='%s' class="form-control col-lg-5">
				<span class="input-group-btn"> </span>
					<button type="submit" class="btn btn-success">Connect Now</button>
		
			</form>
			

            </div>
        </div>
    </div>

	""") % (dbhost, hosttype, conntype, dbhost, port, user, passwd)
	
				




if __name__ == "__main__":
	hosttype , conntype, role = connnDet(dbhost)
	user=createTempUser(dbhost, role)
	connectForm(dbhost, hosttype, conntype, port, user, passwd)
