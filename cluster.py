#!/usr/bin/python

import MySQLdb, cgi, json 
from utils import  engine, config, dict2json, html_topl, showclus
base_url = config.base_url()
formdata = cgi.FieldStorage()
cluster_name = formdata.getvalue('cluster_name')


# connection for dashboard database

def mysql_con():
        user, passwd, db = config.dash_mysql()
        conn = MySQLdb.connect(host='localhost', user=user, passwd=passwd, db=db)
        cur=conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        return conn, cur

def mapGen(dbclus):
	conn, cur = mysql_con()
	slave_master = {}
	master_slave = {}
	sql = "select dbhost  from inventory where cluster_name like '%%%s%%'" % (dbclus)
	try:
		cur.execute(sql)
		data = cur.fetchall()
		status = True
		message = 'Success'
		if data:
			hostlist = []
			for i in range(len(data)):
				dictio = data[i]
				host = dictio['dbhost']
				hostlist.append(host)

			master_list = []
			for i in range(len(hostlist)):
				host = hostlist[i]
				slave_data = engine.slaveStatus(host)
				if not slave_data:
					slave_master[host] = 'None'
				else:
					slave_master[host] = slave_data['Master_Host']
			masters = list(set(slave_master.values()))
			for i in range(len(masters)):
				slave_list = []
				master_host = masters[i]
				for slave, master in slave_master.items():
					if master == master_host:
						slave_list.append(slave)
				master_slave[master_host] = slave_list
			status = True
			message = 'Success'
		else:
			status = None
			message = "No such cluster was found"
			
			
	except MySQLdb.Error as e:
		message = "Search Failed. Try again"
		status = None
	return master_slave, slave_master, status, message, hostlist 


def htmlTop():
	print "Content-Type: text/html"
	print ("""

    <!DOCTYPE <!DOCTYPE html>
    <head>
            <title>MySQL Dashboard</title>
            <meta name="viewport" content="width=device-width, initial-scal=1.0">
            <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">

	    <link rel="stylesheet" type="text/css" href="css/tree.css">
    </head>
    <body>
<div class="container" style="background:#f2f2f2; width:100%%; height:8%%;">
<h4><a href="%s" style="text-decoration:none">MySQL Dashbard</a></h4>
<hr/>
</div>
	<div>
	<h3 class="text-danger"> &nbsp; &nbsp; Showing cluster: %s </h3>
	</div>
        <div class="tree">
	<hr/>
    """) % (base_url, cluster_name)

def print_footer():
    print ("""
<div class="just">
<hr/>
</div>
    </body>
    </html>
    """)



def display_fail(message):

        print ("""
    <br>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <h3 class="text-danger">
                    Oops.. Something is wrong
                </h3>

                <ul>
                    <li>Message : %s </li>
                </ul>

                <br/>

            </div>
        </div>
    </div>

        """) % (message)

def noslave():
        print ("""
    <br>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <h3 class="text-danger">
                    Oops.. Something is wrong
                </h3>

                <ul>
                    Please add minimum one slave in this cluster !!
                </ul>

                <br/>

            </div>
        </div>
    </div>

        """)

if __name__ == "__main__":
#	cluster_name='retail-cpl'
	if (cluster_name):
		master_slave , slave_master, status, message, hostlist = mapGen(cluster_name)
		json_data = dict2json.getdata(slave_master, master_slave)
		if json_data:
			tmpfile = "topology/tmp/" + cluster_name + "." + "json"
			f = open(tmpfile, "w")
			f.write(json_data)
			f.close
			html_topl.htmlTop(cluster_name)
			html_topl.htmlmid(tmpfile)
			showclus.show_clus(cluster_name)
		else:
			htmlTop()
			noslave()
	else:
		message = "Wrong Search !!"
		htmlTop()
		display_fail(message)

	print_footer()

