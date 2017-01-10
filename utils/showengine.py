#!/usr/bin/python

import engine, cgi, socket, config

base_url = config.base_url()

def display_engine(dbhost):
	engine_stat = engine.enginStats(dbhost)
	server_vars = engine.serverVars(dbhost)
	server_stats = engine.serverStats(dbhost)
	slave_stat = engine.slaveStatus(dbhost)


def display_process(dbhost):	
	print ("""
    <br>
    <div class="container-fluid">
        <div>
            <div class="col-md-6 col-md-offset-1">
                <h3 class="text-danger">
                    System Process
                </h3>

                <ul>
                    <li>Go to ""</li>
                    <li>Enter yout mysql server hostname in the input box</li>
                    <li>Click on the Go button and we will take care of the rest</li>
                    <li>Add your cluster/ host in your view. The view is a customized front page just for your dbs</li>
                    <li>Check if your host appears in the dashboard in some time </li>
                </ul>

                <br>

            </div>
        </div>
    </div>
    """)
def display_vars(dbhost):

        print ("""
    <br>
	<div class="container-fluid">
        	<div>
			<div class="col-md-6 col-md-offset-1">
                		<h3 class="text-danger">
                   			 MySQL Variables
                		</h3>
				<div id="container">
				<div class="input-group" style="padding: 0px 0px 4px;"> <span class="input-group-addon">Filter</span>
					<input id="filter" type="text" class="form-control" placeholder="Type here...">
				</div>
					<table class="table table-condensed" style="border: 1px solid #DDD;">
						<thead>
							<tr>
								<th>Variable</th>
								<th>Value</th>
							</tr>
						</thead>
						<tbody class="searchable" id="myTable">
				</div>
		""")
	server_vars = engine.serverVars(dbhost)
	variables = server_vars.keys()
	values = server_vars.values()
	for i in range(len(variables)):
		if values[i] == '':
			print ("""
        <tr>
                <td>%s</td>
                <td>%s</td>
        </tr>
			""") % (variables[i], 'No Value')
		else:
			print ("""
		
	<tr>
		<td>%s</td>
		<td>%s</td>
	</tr>
			""") % (variables[i], values[i])
	print ("""
						</tbody>
					</table>
	                	<div class="col-md-8 text-center">
        	                	<ul class="pagination" id="myPager"></ul>
		                </div>
		
			</div>
		""")
	print ("""

		</div>
	</div>
    """)


#######################################
def display_stats(dbhost):

        print ("""
    <br>
        <div class="container-fluid">
                <div>
                        <div class="col-md-6 col-md-offset-1">
                                <h3 class="text-danger">
                                         MySQL System Stats
                                </h3>
                                <div id="container">
                                <div class="input-group" style="padding: 0px 0px 4px;"> <span class="input-group-addon">Filter</span>
                                        <input id="filter1" type="text" class="form-control" placeholder="Type here...">
                                </div>
                                        <table class="table table-condensed" style="border: 1px solid #DDD;">
                                                <thead>
                                                        <tr>
                                                                <th>Variable</th>
                                                                <th>Value</th>
                                                        </tr>
                                                </thead>
                                                <tbody class="searchable" id="myTable2">
                                </div>
                """)
	server_stats = engine.serverStats(dbhost)
        variables = server_stats.keys()
        values = server_stats.values()
        for i in range(len(variables)):
                if values[i] == '':
                        print ("""
        <tr>
                <td>%s</td>
                <td>%s</
