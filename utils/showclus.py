#!/usr/bin/python

from utils import template, getdashdata, baseinfo, showhost, config
import os, cgi, socket

base_url = config.base_url()

def not_found():
        print ("""

    <br>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <h3 class="text-danger">
                    Oops.. No results.. Perhaps you need to add the host/Cluster to <a href="%s/addhost.py" style="text-decoration:none;" > dashboard </a>
                </h3>


                <br/>

            </div>
        </div>
    </div>


""") % (base_url)

def get_classes(base_dict):
        tabclasses = {"up":"bg-success", "read_only":"bg-success", "slaving":"bg-success", "lag" : "bg-success", "version": "bg-success", "os": "bg-success"}
        if base_dict['Master_Host'] == 'None':
                if base_dict['read_only'] == 'ON':
                        tabclasses['read_only'] = 'bg-danger'
        else:
                if not base_dict['read_only'] == 'ON':
                        tabclasses['read_only'] = 'bg-danger'
                if not base_dict['Seconds_Behind_Master'] == '0':
                        tabclasses['lag'] = 'bg-danger'
                        tabclasses['slaving'] = 'bg-danger'
        return tabclasses



def show_clus(dbclus):

        dbconn, dbcur = getdashdata.mysql_dash()
	sql = "select dbhost from inventory where cluster_name='%s'" % (dbclus)
	dbcur.execute(sql)
	data = dbcur.fetchall()
	print ("""
    <style>
        .table>tbody>tr>td, .table>tbody>tr>th {
            line-height: 1;
        }
	.just {margin-top: 220px;
	margin-left: 20px;}
    </style>
            <div  class="clearfix">
                <h3 class="text-info">
                   &nbsp; &nbsp;  Cluster : %s
                </h3>
	    </div>
            <div class="clearfix">
                        <table class="table table-striped table-responsive table-bordered" style="font-size:11px; text-decoration:none;cursor: pointer; width:100%%; position: absolute;">

	 """) % (dbclus)
	hostdata_dict = {}
	os_version = []
	host_list = []
	sql_version = []
	master_list = []
	read_list = []
	lag_list = []
	conn_list = []
	
	for i in range(len(data)):
		dbhost = data[i].values()[0]
		base_val_list, base_par_list = baseinfo.basInfo(dbhost)
		base_dict = dict(zip(base_par_list, base_val_list))
		if base_dict['running']  == 'No':
			base_dict = { "version_compile_os":"Debian", "innodb_version" : "Nill", "running": "No", "Master_Host":"Nil", "Seconds_Behind_Master":"Nil", "read_only": "Nil"}
			classes = {"up":"bg-danger", "read_only":"bg-danger", "slaving":"bg-danger", "lag" : "bg-danger", "version": "bg-danger", "os": "bg-danger"}
		else:
			classes = get_classes(base_dict)

		host_dict = {}
		host_dict['base'] = base_dict
		host_dict['class'] = classes
		hostdata_dict[dbhost] = host_dict
		host_list.append(dbhost)
		os_dict = {}
		os_dict[base_dict['version_compile_os']] = "bg-success"
		os_version.append(os_dict)
		sql_dict = {}
		sql_dict[base_dict['innodb_version']] = "bg-success"
		sql_version.append(sql_dict)
		connect_dict = {}
		connect_dict[base_dict['running']] = classes['up']
		conn_list.append(connect_dict)
		master_dict = {}
		master_dict[base_dict['Master_Host']] = classes ['slaving']
		master_list.append(master_dict)
		lag_dict = {}
		lag_dict[base_dict['Seconds_Behind_Master']] = classes['lag']
		lag_list.append(lag_dict)
		read_dict = {}
		read_dict[base_dict['read_only']] = classes['read_only']
		read_list.append(read_dict)

	print ("""
				<tr>
					<th> Hostname </th>
	""")		
	for i in range(len(host_list)):
		host = host_list[i]
		bg = "bg-success"
		print ("""
					<td class="%s" onclick="location.href='%s/host.py?dbhost=%s&action=baseinfo';"> %s </td>
		""") % (bg, base_url, host, host)
	print ("""
				</tr>
		""")
	print ("""
				<tr>
					<th> OS Running </th> 
	""")
	for i in range(len(os_version)):
		os = os_version[i].keys()[0]
		bg = os_version[i].values()[0]
		print ("""
				<td class="%s" onclick="location.href='%s/host.py?dbhost=%s&action=baseinfo';"> %s </td>
		""") % (bg, base_url, host, os)
        print ("""
                                </tr>
                """)
        print ("""
                                <tr>
                                        <th> MySQL Version </th>
        """)
	for i in range(len(sql_version)):
		sql = sql_version[i].keys()[0]
		bg = sql_version[i].values()[0]
                print ("""
                                <td class="%s" onclick="location.href='%s/host.py?dbhost=%s&action=baseinfo';"> %s </td>
                """) % (bg, base_url, host, sql)
		
        print ("""
                                </tr>
                """)
        print ("""
                                <tr>
                                        <th> Master </th>
        """)
	for i in range(len(master_list)):
		master = master_list[i].keys()[0]
		bg = master_list[i].values()[0]
                print ("""
                                <td class="%s" onclick="location.href='%s/host.py?dbhost=%s&action=baseinfo';"> %s </td>
                """) % (bg, base_url, host, master)
        print ("""
                                </tr>
                """)
        print ("""
                                <tr>
                                        <th> Lag </th>
        """)
	for i in range(len(lag_list)):
		lag = lag_list[i].keys()[0]
		bg = lag_list[i].values()[0]
                print ("""
                                <td class="%s" onclick="location.href='%s/host.py?dbhost=%s&action=baseinfo';"> %s </td>
                """) % (bg, base_url, host, lag)
        print ("""
                                </tr>
                """)

        print ("""
                                <tr>
                                        <th> Read Only </th>
        """)
	for i in range(len(read_list)):
		read = read_list[i].keys()[0]
		bg  = read_list[i].values()[0]
                print ("""
                                <td class="%s" onclick="location.href='%s/host.py?dbhost=%s&action=baseinfo';"> %s </td>
                """) % (bg, base_url, host, read)
        print ("""
                                </tr>
                """)


#                                """) % (classes['up'], dbhost, classes['os'], base_dict['version_compile_os'], classes['up'], base_dict['running'], classes['read_only'], base_dict['read_only'], classes['slaving'], base_dict['Master_Host'], classes['lag'], base_dict['Seconds_Behind_Master'])

	print ("""
                        </table>

</div>


        """) 
        dbconn.close()



################This is for main search page






def show_cluslist(dbclus):

        dbconn, dbcur = getdashdata.mysql_dash()
        sql = "select distinct cluster_name  from inventory where cluster_name like '%%%s%%'" % (dbclus)
        dbcur.execute(sql)
        data = dbcur.fetchall()
        clustlist = []
        for i in range(len(data)):
                dictio = data[i]
                clust = dictio['cluster_name']
                clustlist.append(clust)
        if clustlist:
                for i in range(len(clustlist)):
                        dbclus = clustlist[i]


                        sql = "select dbhost from inventory where cluster_name='%s'" % (dbclus)
                        dbcur.execute(sql)
                        data = dbcur.fetchall()
                        print ("""
    <style>
        .table>tbody>tr>td, .table>tbody>tr>th {
            line-height: 1;
        }
    </style>
    <br>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-4" class="clearfix">
                <h3 class="text-info">
                    Cluster : %s
                </h3>
                <div>
                        <table class="table table-striped table-responsive table-bordered" style="font-size:11px; text-decoration:none;cursor: pointer;" onclick="location.href='%s/cluster.py?cluster_name=%s';">
                                <thead>
                                        <tr>
                                                <th> Cluster: %s </th>
						<th>OS Running </th>
						<th>MySQL Running</th>
						<th>Read Only</th>
						<th>Slave of</th>
						<th>Lag</th>
                                        </tr>
                                </thead>

                                <tbody>
                        """) % (dbclus, base_url, dbclus, dbclus)
                        for i in range(len(data)):
                                dbhost = data[i].values()[0]
				base_val_list, base_par_list = baseinfo.basInfo(dbhost)
				base_dict = dict(zip(base_par_list, base_val_list))
				if base_dict['running']  == 'No':
					base_dict = { "version_compile_os":"Debian", "innodb_version" : "Nill", "running": "No", "Master_Host":"Nil", "Seconds_Behind_Master":"Nil", "read_only": "Nil"}
					classes = {"up":"bg-danger", "read_only":"bg-danger", "slaving":"bg-danger", "lag" : "bg-danger", "version": "bg-danger", "os": "bg-danger"}
				else:
					classes = get_classes(base_dict)
                                print ("""
					<tr>

						<td class="%s">%s</td>
						<td class="%s">%s</td>
						<td class="%s">%s</td>
						<td class="%s">%s</td>
						<td class="%s">%s</td>
						<td class="%s">%s</td>

					</tr>
                                """) % (classes['up'], dbhost, classes['os'], base_dict['version_compile_os'], classes['up'], base_dict['running'], classes['read_only'], base_dict['read_only'], classes['slaving'], base_dict['Master_Host'], classes['lag'], base_dict['Seconds_Behind_Master'])
                        print ("""
                                </tbody>
                        </table>
                </div>
        </div>
     </div>
</div>

        """)
        else:
                not_found()
        dbconn.close()




