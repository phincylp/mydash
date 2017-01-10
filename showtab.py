#!/usr/bin/python

from utils import database, template, config
import cgi, socket

formdata = cgi.FieldStorage()
dbhost = formdata.getvalue('dbhost')
db = formdata.getvalue('db')
base_host=socket.getfqdn()
action=''

base_url = config.base_url()


def show_Tab():
	table_list, tabsize_list, tab_engine, tab_coll = database.tableInfo(dbhost,db)
        print ("""
                <table class="table table-striped table-bordered table-hover" data-link="row" cellspacing="0" width="100%" onmouseover="" style="cursor: pointer;">
                        <thead>
                                <tr>
                                        <th>Table Name</th>
                                        <th>Size (Kb)</th>
					<th>Engine</th>
					<th>Collation</th>
                                </tr>

                        </thead>
                        <tbody>
                """)
        for itr in range(len(table_list)):
                print ("""
<!--                                <tr onclick="window.document.location='tabaction.py?dbhost=%s&db=%s&tab=%s&action=base';">
-->
				    <tr>
                                        <td>%s</td>
                                        <td>%s</td>
                                        <td>%s</td>
                                        <td>%s</td>
                                </tr>

        """ % (dbhost, db, table_list[itr], table_list[itr], tabsize_list[itr], tab_engine[itr], tab_coll[itr]))
        print ("""
                        </tbody>

                </table>
        """)

# This is where the program starts
if __name__ == "__main__":
	try:
		template.print_header()
		template.hostdetail(dbhost, base_url, action)
		show_Tab()
		template.print_footer()


	except:
		cgi.print_exception()
