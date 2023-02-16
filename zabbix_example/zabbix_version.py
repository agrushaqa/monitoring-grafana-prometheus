import time
from datetime import datetime

from pyzabbix import ZabbixAPI

ZABBIX_SERVER = 'http://localhost:8080'
zapi = ZabbixAPI(ZABBIX_SERVER, user='Admin', password='zabbix')
answer = zapi.do_request('apiinfo.version')
print("Version:", answer['result'])

groupid = 4  # ZABBIX_SERVER
hosts = zapi.host.get(groupids=groupid, output=['hostid', 'name'])
# Список имен хостов
host_names = [host['name'] for host in hosts]
print(host_names)
host_ids = [host['hostid'] for host in hosts]
for host_id in host_ids:
    # параметр search позволяет найти все items,
    # в имени которых есть заданная строка
    items = zapi.do_request('item.get', {'hostids': [host_id],
                                         'output': ['itemid', 'name'],
                                         'search': {'name': 'Idle time'}})
    disk_ids = [item['itemid'] for item in items['result']]
    time_from = time.mktime((2023, 2, 15, 9, 0, 0, 0, 0, 0))
    time_till = time.mktime((2023, 2, 16, 18, 0, 0, 0, 0, 0))
    print("{:<20} | {:<10} | {:<10}".format("itemid", "clock", "value"))
    for disk in disk_ids:
        print()
        for i_record in zapi.history.get(history=0, itemids=disk):
            print("{:<20} | {:<10} | {:<10}".format(
                i_record["itemid"],
                datetime.utcfromtimestamp(int(i_record["clock"])
                                          ).strftime('%Y-%m-%d %H:%M:%S'),
                i_record["value"]))
