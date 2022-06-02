import shutil
import psutil
from network import *

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free=du.free/du.total*100
    return free > 20
def check_cpu_usage():
    usage=psutil.cpu_percent(1)
    return usage<75
if check_disk_usage("/") and check_cpu_usage() and check_localhost() and check_connectivity():
    print("Everything is ok!(Network and CPU)")
elif not check_disk_usage("/") or not check_cpu_usage() and check_localhost() and check_connectivity():
    print("Network is ok but pc is having hardtime")
elif check_disk_usage("/") or check_cpu_usage() and not check_localhost() or not check_connectivity():
    print("CPU is ok but network is not well")
else:
    print("Nothing is good :(")
