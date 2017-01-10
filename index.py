#!/usr/bin/python

from utils import template, getdashdata, baseinfo, showhost, showclus, config
import os, cgi
#base_host=socket.getfqdn()
#base_url="https://%s/mydash" % (base_host)
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

def search_clus():
	print ("""
	
<br>
<div class="container-fluid">
	<div>
		<div class="col-md-4 col-md-offset-1">
			<h3 class="text-info">
				MySQL Clusters
			</h3>
			<div id="container">
				<div class="input-group" style="padding: 0px 0px 4px; width: 500px;"> 
					<form method="post" action="index.py">
						<input type="text" name="dbclus" class="form-control" placeholder="Search..." required list="datalist1">
						<datalist id="datalist1">
	""")
	clusters = getdashdata.getClusters()
	for i in range(len(clusters)):
		print ("""

							<option value="%s">
		""") % (clusters[i])	
	print ("""		
						</datalist>		
						<br><br>
						<span class="input-group-btn"> </span>
						<button class="btn btn-default">Search</button>
					</form>
				</div>
			</div>
		</div>
		<div class="col-md-4 col-md-offset-2">
			<h3 class="text-info">
				MySQL Hosts
			</h3>
			<div id="container">
				<div class="input-group" style="padding: 0px 0px 4px; width: 500px;">
					<form method="post" action="index.py">
						<input type="text" name="dbhost" class="form-control" placeholder="Search..." required list="datalist2">
						<datalist id="datalist2">
	""")
	hosts = getdashdata.getHosts()
	for i in range(len(hosts)):
		print ("""
							<option value="%s">
		""") % (hosts[i])
	print ("""
						</datalist>
						<br><br>
						<span class="input-group-btn"> </span>
						<button class="btn btn-default">Search</button>
					 </form>
				</div>
			</div>
		</div>
	</div>
</div>
<hr></hr>
<!--
<hr style="height:1px;border:none;color:#333;background-color:#C0C0C0  ;"/hr>
================================
-->
		<br>
                <div class="col-md-6 col-md-offset-4">
                        <h3 class="text-info">
                                Connect to Host
                        </h3>
			<br>
			<ul>
				<li>Create databases and users</li>
				<li>See replication status, engine status, server variables</li>
				<li>Access DB console and create you table schema, run queries and more..</li>
			</ul>
                        <div id="container">
                                <div class="input-group" style="padding: 0px 0px 4px; width: 500px;">
                                        <form method="post" action="index.py">
                                                <input type="text" name="connhost" class="form-control" placeholder="hostname/IP" required>
                                                <br><br>
                                                <span class="input-group-btn"> </span>
                                                <button class="btn btn-default">Connect</button>
                                        </form>
                                </div>
                        </div>
                </div>
<!--
================================
-->

	""")

def base_hostconn(connhost):
        print "Content-Type: text/html"
        print
        print ("""

<!DOCTYPE HTML>
<html lang="en-US">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="1;url=%s/host.py?dbhost=%s&action=baseinfo">
        <script type="text/javascript">
            window.location.href = "%s/host.py?dbhost=%s&action=baseinfo"
        </script>
        <title>Page Redirection</title>
    </head>
    <body>
        <!-- Note: don't tell people to `click` the link, just tell them that it is a link. -->
        If you are not redirected automatically, follow the <a href='%s/host.py?dbhost=%s&action=baseinfo'>link to %s</a>
    </body>
</html>

        """) % (base_url, connhost, base_url, connhost, base_url, connhost, connhost)


if __name__ == "__main__":
	if os.environ['REQUEST_METHOD'] == 'GET':
		template.print_header()
		search_clus()	
		template.print_footer()	
	elif os.environ['REQUEST_METHOD'] == 'POST':
		formdata = cgi.FieldStorage()
		dbhost = formdata.getvalue('dbhost')
		dbclus = formdata.getvalue('dbclus')
		connhost = formdata.getvalue('connhost')
		if dbhost:
			dbhost = dbhost.strip()
			template.print_header()
			showhost.show_host(dbhost)
			template.print_footer()
		elif dbclus:
			dbclus = dbclus.strip()
			template.print_header()
			showclus.show_cluslist(dbclus)
			template.print_footer()
		elif connhost:
			connhost = connhost.strip()
			base_hostconn(connhost)
		else:
			template.print_header()
			search_clus()
			template.print_footer()




