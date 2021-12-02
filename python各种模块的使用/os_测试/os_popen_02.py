import os

devices_info_str = os.popen("ifconfig")

print(devices_info_str.read())