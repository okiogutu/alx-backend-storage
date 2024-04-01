
#!/usr/bin/env python3

"""interacts with MongoDB"""

from pymongo import MongoClient


def dump_nginx_req_data(nginx_data):
    """Output request data"""
    http_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print(f'{nginx_data.estimated_document_count()} logs')
    print('Methods:')
    for method in http_methods:
        method_counter = nginx_data.count_documents({'method': method})
        print(f'\tmethod {method}: {method_counter}')
    stat_count = nginx_data.count_documents(
        {'method': 'GET', 'path': '/status'})
    print(f'{stat_count} status check')


def get_top_ip_group(ip_group):
    """ Stats about the top ten IP's"""
    print('IPs:')
    fetch_logs = ip_group.aggregate(
        [
            {
                '$group': {'_id': '$ip', 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10,
            },
        ]
    )
    for log in fetch_logs:
        ip = log['_id']
        ip_count = log['totalRequests']
        print(f'\t{ip}: {ip_count}')


def runMain():
    """Run MongoClient"""
    mongodb = MongoClient('mongodb://127.0.0.1:27017')
    dump_nginx_req_data(mongodb.logs.nginx)
    get_top_ip_group(mongodb.logs.nginx)


if __name__ == '__main__':
    runMain()
