#!/usr/bin/python

from utils import dbactions, template, config
import cgi, os
import socket
import string
import random

# get data from url and browser
formdata = cgi.FieldStorage()
dbhost = formdata.getvalue('dbhost')
user = formdata.getvalue('user')
dbname =formdata.getvalue('selectminor')
role = formdata.getvalue('optradio')
base_url = config.base_url()




passw = (''.join(random.choice(string.ascii_lowercase) for i in range(6)))

def showSuccess(dbhost, dbname, user, passw, role):
	template.print_header()
	print ("""
    <br>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <h3 class="text-danger">
                    Host Action Status
                </h3>

                <ul>
		    <li>Create User <font color=green>sucess </font>with below data </li>
		    <li>Hostname : %s </li>
		    <li>Database Name : %s</li>
                    <li>User :<b> %s </b></li>
                    <li>Password :<b> %s </b></li>
                    <li>Role :<b> %s </b></li>
                </ul>

                <br/>

            </div>
        </div>
    </div>	

	""") % (dbhost, dbname, user, passw, role)
	template.print_footer()
	
def showFail(dbhost, dbname, status):
        template.print_header()
        print ("""
    <br>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <h3 class="text-danger">
			Host Action Status
                </h3>

                <ul>
                    <li>Create User <font color=red>fail</font> with below data </li>
                    <li>Hostname : %s </li>
                    <li>Database Name : %s</li>
		    <li>Message : %s </li>
                </ul>

                <br/>

            </div>
        </div>
    </div>

        """) % (dbhost, dbname, status)	
	template.print_footer()

if __name__ == "__main__":
	if os.environ['REQUEST_METHOD'] == 'POST': 
		status = dbactions.createUser(dbhost, user, dbname, role, passw)
		if status == True:
			showSuccess(dbhost, dbname, user, passw, role)
		else:
			showFail(dbhost, dbname, status)
	else:
		template.print_header()
		print ("""

    <br>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <h3 class="text-danger">
                        Host Action Status
                </h3>

                <ul>
                    <li> No Action Specified for Host</li>
                </ul>

                <br/>

            </div>
        </div>
    </div>

""")		
