#!/usr/bin/env python
# psutil is a cross-platform library for getting info on running processes
import psutil

# Get a list of current running process ids
pids = psutil.pids()

PS_HDR = "{0:^15s}  {1:^7s}  {2:^7s}  {3:^13s}  {4:20s}"
PS_FMT = "{0:15s}  {1:7d}  {2:7d}  {3:13.2f}  {4:20s}"

# Print a header
print(PS_HDR.format('USER', 'PID', 'PPID', 'TIME', 'NAME'))

# For each running process
for proc in psutil.process_iter():
    try:
        pinfo = proc.as_dict(attrs=['username', 'pid', 'ppid', 'create_time', 'name', 'exe'])
    except psutil.NoSuchProcess:
        pass
    else:
        user = pinfo['username']
        pid = pinfo['pid']
        ppid = pinfo['ppid']
        ctime = pinfo['create_time']
        name = pinfo['name']
        exe = pinfo['exe']
        print(PS_FMT.format(user, pid, ppid, ctime, name))
