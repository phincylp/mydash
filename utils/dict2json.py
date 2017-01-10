#!/usr/bin/python

import json


def genChlddata(host, slave_master):
	host_dict = {}
	host_dict['name'] = host
	host_dict['parent'] = slave_master[host]
	return host_dict

def getdata(slave_master, master_slave):
	if slave_master.values() and master_slave.values():
		data_dict = {}     # host: data
		for i in range(len(slave_master)):
			host = slave_master.keys()[i]
			if slave_master[host] == 'None':
				host_dict={}
				host_dict['parent'] = 'null'
				host_dict['name'] = host
				data_dict[host]=host_dict
			else:
				host_dict=genChlddata(host, slave_master)
				data_dict[host]=host_dict
		for i in range(len(master_slave.keys())):
			master_host = master_slave.keys()[i]
			if len(master_slave.keys()) > 1 :
				if  master_host != 'None':
					slave_list = master_slave[master_host]
					child_data = []
					for i in range(len(slave_list)):
						child_host = slave_list[i]
						childdata = data_dict[child_host]
						child_data.append(childdata)
					master_dict=data_dict[master_host]
					master_dict['children']=child_data
					json_data = json.dumps(master_dict)
			else:
				json_data =  None
				
	else:
		json_data = None
	return json_data
