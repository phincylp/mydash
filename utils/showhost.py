#!/usr/bin/python

from utils import template, getdashdata, baseinfo, config
import os, cgi

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
	
def show_host(dbhost):
##


##
        dbconn, dbcur = getdashdata.mysql_dash()
        sql = "select dbhost from inventory where dbhost like '%%%s%%'" % (dbhost)
        dbcur.execute(sql)
        data = dbcur.fetchall()
        dbconn.close()
        hostlist = []
        for i in range(len(data)):
                dictio = data[i]
                dbhost = dictio['dbhost']
                hostlist.append(dbhost)
        if hostlist:
                for i in range(len(hostlist)):
                        dbhost = hostlist[i]
                        base_val_list, base_par_list = baseinfo.basInfo(dbhost)
                        base_dict = dict(zip(base_par_list, base_val_list))
			if base_dict['running']	 == 'No':
				base_dict = { "version_compile_os":"Debian", "innodb_version" : "Nill", "running": "No", "Master_Host":"Nil", "Seconds_Behind_Master":"Nil", "read_only": "Nil"}
				classes = {"up":"bg-danger", "read_only":"bg-danger", "slaving":"bg-danger", "lag" : "bg-danger", "version": "bg-danger", "os": "bg-danger"}
			else:
				classes = get_classes(base_dict)
                        print ("""

    <br>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <h3 class="text-info">
                    Host : %s
                </h3>
                <div>
                        <table class="table table-striped table-responsive table-bordered" style="font-size:11px">
                                <thead>
       <tr onclick="window.document.location='%s/host.py?dbhost=%s&action=baseinfo';" style="text-decoration:none;cursor: pointer;">
            <th>OS Running </th>
            <th>MySQL Version</th>
	    <th>MySQL Running</th>
	    <th>Read Only</th>
            <th>Slave of</th>
            <th>lag</th>
        </tr>
                                </thead>
        """) % (dbhost, base_url, dbhost)
                        print ("""

   <tr onclick="location.href='%s/host.py?dbhost=%s&action=baseinfo';" style="text-decoration:none;cursor: pointer;">
        <td class="%s">%s</td>
	<td class="%s">%s</td>
        <td class="%s">%s</td>
        <td class="%s">%s</td>
        <td class="%s">%s</td>
        <td class="%s">%s</td>
    </tr>
        """) % (base_url, dbhost, classes['os'], base_dict['version_compile_os'], classes['version'], base_dict['innodb_version'], classes['up'], base_dict['running'], classes['read_only'], base_dict['read_only'], classes['slaving'], base_dict['Master_Host'], classes['lag'], base_dict['Seconds_Behind_Master'])
                        print ("""

                        </table>
                </div>

                <br>

            </div>
        </div>
    </div>


                        """)
        else:
                not_found()



