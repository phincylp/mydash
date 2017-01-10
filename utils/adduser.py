#!/usr/bin/python

import cgi
import socket
import sys
import database, config

# get data from url and browser
formdata = cgi.FieldStorage()
dbhost = formdata.getvalue('dbhost')
action =formdata.getvalue('action')

base_url = config.base_url()

def addUser(dbhost ):
	database_list, datasize_list = database.dataInfo(dbhost)
	print ("""
	<br>
	<br>
	<center>
        <div class="container" align="center" style="border-style:solid;border-color:#fff;">
                <div class="container-fluid">
			<div class="btn-group" role="group" align="center">

				<form method="post" action="createuser.py">
					<input type="text" name="user" class="form-control col-lg-3" placeholder="User Name" required>
                                        <input type="hidden" name="dbhost" value='%s' class="form-control col-lg-5">
                                        <br>
					<br>
					<div class="control-group">
						<label class="control-label" for="selectminor">DB Name</label>
						<div class="controls">
							<select id="selectminor" name="selectminor" class="input-xlarge">
        """) % (dbhost)

	for val in database_list:
		if val == 'mysql':
			continue
		elif val == 'information_schema':
			continue
                elif val == 'performance_schema':
                        continue
		else:
			print (""" <option value="{0}"> {1} </option> """.format(val, val))
	print ("""
							</select>

						</div>
					</div>
					<br>
                """)

	print ("""

	                	        <div class="radio" align="left">
        	                	        <h4><label><input type="radio" name="optradio" value="ro" checked=""> Read Only user (SELECT)</label></h4>
	                	        </div>
	                        	<div class="radio" align="left">
	                                	<h4><label><input type="radio" name="optradio" value="rw">Read / Write user (SELECT, INSERT, UPDATE, DELETE, CREATE)</label></h4>
		                        </div>

					<div class="col-sm-offset-2 col-sm-10" align="left">
						<div class="checkbox">
							<label>
								<input type="checkbox" required/> I agree that user will be added to the database.
							</label>
					</div>
					<br>
					<span class="input-group-btn"> </span>
					<button class="btn btn-success">Add User</button>
				</form>
			</div>
		</div>
	</div>
	</center>


	""")


