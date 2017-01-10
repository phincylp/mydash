#!/usr/bin/python

from utils import template, showbase, showdbs, adduser, showengine, showprocess, config, dbconsole
import cgi

formdata = cgi.FieldStorage()
dbhost = formdata.getvalue('dbhost')
action = formdata.getvalue('action')
base_url = config.base_url()
#user = 'opsdshro'
passwd = '0pzR0Pass'
port = '3306'

if __name__ == "__main__":
        template.print_header()
	template.hostdetail(dbhost, base_url, action)
	if action == 'baseinfo':
		showbase.display_base(dbhost)
	if action == 'dbinfo':
		showdbs.showDbs(dbhost)
	if action == 'adduser':
		adduser.addUser(dbhost)
	if action == 'engine':
		showengine.showslave_stat(dbhost)
		showengine.display_vars(dbhost)
		showengine.display_stats(dbhost)
	if  action == 'process':
		showprocess.display_processlist(dbhost)
	if action == 'console':
		hosttype , conntype, role = dbconsole.connnDet(dbhost) 
		user=dbconsole.createTempUser(dbhost, role)
		dbconsole.connectForm(dbhost, hosttype, conntype, port, user, passwd)
	template.print_footer()
