#!/usr/bin/python
import baseinfo, config
import cgi
base_url = config.base_url()


# Base info
def display_base(dbhost):
	base_val_list, base_par_list = baseinfo.basInfo(dbhost)
	base_dict = dict(zip(base_par_list, base_val_list))
	OS=base_dict['version_compile_os']
	ARCH=base_dict['version_compile_machine']
	sqlver=base_dict['innodb_version']
	sqldist=base_dict['version_comment']
	datadir=base_dict['datadir']
	tmpdir=base_dict['tmpdir']
	slave_of=base_dict['Master_Host']
	lag_by=base_dict['Seconds_Behind_Master']
	read_only = base_dict['read_only']
	slave_sql = base_dict['Slave_SQL_Running']
	slave_io = base_dict['Slave_IO_Running']
	print ("""
		<br>
		<br>
		<br>
                <table class="table">
                        <tr>
                                <td>&nbsp; &nbsp;OS Running </td>
                                <td>%s</td>

                        </tr>
                        <tr>
                                <td>&nbsp; &nbsp;Architecture</td>
                                <td>%s</td>

                        </tr>
                        <tr>
                                <td>&nbsp; &nbsp;MySQL Version</td>
                                <td>%s</td>

                        </tr>
                        <tr>
                                <td> &nbsp; &nbsp;MySQL Distribution</td>
                                <td>%s</td>

                        </tr>
                        <tr>
                                <td>&nbsp; &nbsp;Data Directory</td>
                                <td>%s</td>

                        </tr>
                        <tr>
                                <td>&nbsp; &nbsp;Temp directory</td>
                                <td>%s</td>

                        </tr>
                        <tr>
                                <td> &nbsp; &nbsp;Slave of</td>
                                <td><a onclick="location.href='%s/host.py?dbhost=%s&action=baseinfo';" style="text-decoration:none;cursor: pointer;"> %s</a></td>

                        </tr>
                        <tr>
                                <td>&nbsp; &nbsp;Slave Lag</td>
                                <td>%s</td>

                        </tr>
                        <tr>
                                <td>&nbsp; &nbsp;Slave_SQL_Running</td>
                                <td>%s</td>

                        </tr>
                        <tr>
                                <td>&nbsp; &nbsp;Slave_IO_Running</td>
                                <td>%s</td>

                        </tr>
                        <tr>
                                <td>&nbsp; &nbsp;Read Only</td>
                                <td>%s</td>

                        </tr>

                </table>



	  """ % (OS, ARCH, sqlver, sqldist, datadir, tmpdir, base_url, slave_of, slave_of, lag_by, slave_sql, slave_io, read_only))
