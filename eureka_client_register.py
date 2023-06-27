from http import server
import py_eureka_client.eureka_client as eureka_client

rest_server_host = "http://172.20.80.123"
#rest_server_port = 31101
reg_list = {'daoservers':{'server': '172.20.80.123', 'port':31101}, 'nginx':{'server': '172.20.80.123', 'port':30081}}

for each_key in reg_list.keys():
    eureka_client.init(eureka_server="http://172.20.80.120:9090", app_name=each_key, instance_host=reg_list[each_key]['server'], instance_port=reg_list[each_key]['port'])
