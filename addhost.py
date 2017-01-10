#!/usr/bin/python

from utils import template, dbactions, config
import os, cgi, socket, MySQLdb

def addform():
        print ("""
    <br>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <h3 class="text-danger">
                    Add your Host to the dashboard
                </h3>
			<div class="form-group" >
			<form method="post" action="addhost.py">
			<input type="text" name="dbhost" class="form-control" placeholder="Host Name/ IP Address" required>

                        <div class="col-sm-offset-2 col-sm-10" align="left">
                        <br>
                        </div>

			<input type="text" name="cluster_name" class="form-control" placeholder="Cluster Name" required>
	 	
			<br><br>
			<div class="col-sm-offset-2 col-sm-10" align="left">
			</div>
<!--
			<div class="radio" align="left">
				<h4><label><input type="radio" name="optradio" value="ro" checked=""> This host is in User Path</label></h4>
			</div>
                        <div class="radio" align="left">
                                <h4><label><input type="radio" name="optradio" value="rw"> This host is in Order Path</label></h4>
                        </div>
-->

			<span class="input-group-btn"> </span>
			<button type="submit" class="btn btn-success">Submit</button>
			</form>
			</div>

                

            </div>
        </div>
    </div>
    """)

def display_success(dbhost, cluster_name, message):
	
        print ("""
    <br>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <h3 class="text-danger">
                    Host Action Status
                </h3>

                <ul>
                    <li>Add Host was  <font color=green>sucess </font>with below data </li>
                    <li>Hostname : %s </li>
                    <li>Cluster Name : %s</li>
		    <li>Message : %s </li>
                </ul>

                <br/>

            </div>
        </div>
    </div>

        """) % (dbhost, cluster_name, message)

def display_fail(dbhost, cluster_name, message):

        print ("""
    <br>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <h3 class="text-danger">
                    Host Action Status
                </h3>

                <ul>
                    <li>Add Host was <font color=red> fail </font>with below data </li>
                    <li>Hostname : %s </li>
                    <li>Cluster Name : %s</li>
                    <li>Message : %s </li>
                </ul>

                <br/>

            </div>
        </div>
    </div>

        """) % (dbhost, cluster_name, message)

def display_error():
	print ("""

    <br>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <h3 class="text-danger">
                    Oops !! MySQL server could not be accessed
                </h3>

                <ul>
                    <li>Check if the host/mysql server is up and running</li>
                    <li>Check if user has enough permissions</li>
                </ul>

                <br/>

            </div>
        </div>
    </div>


        """)



if __name__ == "__main__":
        template.print_header()
	if os.environ['REQUEST_METHOD'] == 'GET':
	        addform()
	elif os.environ['REQUEST_METHOD'] == 'POST':
		formdata = cgi.FieldStorage()
		dbhost = formdata.getvalue('dbhost')
		cluster_name = formdata.getvalue('cluster_name')
		dbhost = dbhost.strip()
		cluster_name =  cluster_name.strip()
		user, passwd = config.dbhost_connect()
		try:
			dbconn = MySQLdb.connect(host=dbhost, user=user, passwd=passwd, db='mysql')
			connect = True
			dbconn.close()
		except MySQLdb.Error as e:
			connect = None
		if connect == True:
			status, message = dbactions.hostadd(dbhost, cluster_name)
			if status == True:
				display_success(dbhost, cluster_name, message)
			else:
				display_fail(dbhost, cluster_name, message)
		
		else:
			display_error()
        template.print_footer()
