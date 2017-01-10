#!/usr/bin/python

from utils import dbactions, template, config
import cgi, os
import socket

# get data from url and browser
formdata = cgi.FieldStorage()
dbhost = formdata.getvalue('dbhost')
dbname =formdata.getvalue('dbname')
base_url = config.base_url()

def showSuccess(dbhost, dbname):
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
		    <li>Create database <font color=green>sucess </font>with below data </li>
		    <li>Hostname : %s </li>
		    <li>Database Name : %s</li>
                </ul>

                <br/>

            </div>
        </div>
    </div>	

	""") % (dbhost, dbname)
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
                    <li>Create database <font color=red>fail</font> with below data </li>
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
		status = dbactions.createDB(dbhost, dbname)
		if status == True:
			showSuccess(dbhost, dbname)
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
