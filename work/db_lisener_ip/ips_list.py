# encoding: utf-8
# Author: LW


ips_list_str = "10.69.11.58,10.69.11.100,10.69.11.70,10.69.10.205,10.69.10.64,10.69.10.61,10.69.10.60,10.69.10.112,10.69.10.159,10.69.14.102,10.69.15.52,10.69.15.54,10.69.15.56,10.69.11.65,10.69.10.81,10.69.10.63,10.69.11.51,10.69.13.52,10.69.10.65,10.69.13.166,10.69.13.154,10.69.18.1,10.69.18.3,10.69.18.5,10.69.18.7,10.69.18.9,10.69.18.11,10.69.18.13,10.69.18.15,10.69.18.17,10.69.18.19,10.69.18.21,10.69.18.23,10.69.13.169,10.69.13.183,10.69.13.173,10.69.10.62,10.69.80.26,10.69.80.27,10.69.80.12,10.69.80.11,10.69.82.24,10.69.82.25,10.69.80.20,10.69.10.117,10.69.17.21,10.69.82.34,10.69.82.35,10.69.17.34,10.69.17.35,192.168.0.36,192.168.0.37,10.69.10.99,10.69.10.153,10.69.80.66,10.69.80.67,10.69.10.66,10.69.10.67,10.69.10.68,10.69.10.237,10.69.11.66,10.69.11.67,10.69.10.235,10.69.10.69,10.69.80.80,10.69.10.215,10.69.80.91,10.69.80.92,10.69.80.93,10.69.80.94,10.69.110.11,10.69.110.12,10.69.210.11,10.69.82.99"


ips_list = ips_list_str.split(',')

for ip in ips_list:
    print(ip)