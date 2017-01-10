#!/usr/bin/python

import database

#Databases

def showDbs(dbhost):
	database_list, datasize_list = database.dataInfo(dbhost)
	print ("""<br><h4><b>&nbsp; &nbsp;<font color="#530000">Showing databases on %s </font></b> </h4> <hr>""" % (dbhost))
	print ("""
	<div class="row">
			<span class="glyphicon glyphicon-align-justify" aria-hidden="true"></span>
			<span class="glyphicon glyphicon-align-justify" aria-hidden="true"></span>
                        <div class="btn-group" role="group" align="center">
                                <button type="button" class="btn btn-success" data-toggle="modal" data-target="#createDB">Create Database</button>

<!-- Modal -->
				<div id="createDB" class="modal fade" role="dialog">
				  <div class="modal-dialog">

				    <!-- Modal content-->
				    <div class="modal-content">
				      <div class="modal-header">
				        <button type="button" class="close" data-dismiss="modal">&times;</button>
				        <h4 class="modal-title">Create Database</h4>
				      </div>
				      <div class="modal-body">
				        <p>Enter mysql database name and click on create button </p>
                                         <form method="post" action="createdb.py">
                                          <input type="text" name="dbname" class="form-control col-lg-5" placeholder="Database Name" required>
					  <input type="hidden" name="dbhost" value='%s' class="form-control col-lg-5">
					  <br>
					  <br>
					  <p> This will create a new database in the server </p>
                                          <div class="col-sm-offset-2 col-sm-10" align="left">
                                          <div class="checkbox">
                                          <label>
                                          <input type="checkbox" required/> I agree
                                          </label>
                                          </div>
                                          </div>
                                          <span class="input-group-btn"> </span>
                                          <button class="btn btn-success">Create</button>
                                          </form>
				      </div>
				      <div class="modal-footer">
				        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
				      </div>
				    </div>

				  </div>
				</div>

                        </div>
                        <div class="btn-group" role="group">
                               <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#addUser">Add User</button>
<!-- Modal -->
                                <div id="addUser" class="modal fade" role="dialog">
                                  <div class="modal-dialog">

                                    <!-- Modal content-->
                                    <div class="modal-content">
                                      <div class="modal-header">
                                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                                        <h4 class="modal-title">Add User</h4>
                                      </div>
                                      <div class="modal-body">
                                        <p>Enter new user name and click on add button </p>
                                         <form method="post" action="createuser.py">
                                          <input type="text" name="user" class="form-control col-lg-3" placeholder="User Name" required>
			       		  <input type="hidden" name="dbhost" value='%s' class="form-control col-lg-5">
                                          <br>

<br>
<div class="control-group">
	        <label class="control-label" for="selectminor">DB Name</label>
	        <div class="controls">
                <select id="selectminor" name="selectminor" class="input-xlarge">

        """ % (dbhost, dbhost))

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
                                          </div>
                                          <span class="input-group-btn"> </span>
                                          <button class="btn btn-success">Add User</button>
                                          </form>
                                      </div>
                                      <div class="modal-footer">
                                        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                                      </div>
                                    </div>
                                  </div>
                                </div>


                        </div>




		<hr>
		</div>
</div>
	""")  
	print ("""
		<table class="table table-striped table-bordered table-hover" data-link="row" cellspacing="0" width="100%" onmouseover="" style="cursor: pointer;">
			<thead>
				<tr>
		                	<th>Database Name</th>
			                <th>Size (MB)</th>
				</tr>

			</thead>
                        <tbody>
		""")
	for itr in range(len(database_list)):
		print ("""
				<tr onclick="window.document.location='showtab.py?dbhost=%s&db=%s';">
 					<td>%s</td>
					<td>%s</td>
				</tr>

	""" % (dbhost, database_list[itr], database_list[itr], float(datasize_list[itr])))
	print ("""
                        </tbody>

                </table>
	""")

