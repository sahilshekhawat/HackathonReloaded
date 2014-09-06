from django.shortcuts import render
from models import ProcessInfo
import subprocess
import os

opening_for_first_time = True

def home(request):
    info = find_process_info()
    b = ProcessInfo(process_info=info)
    b.save()
    return render(request, 'index.html', {"process_info": info})


def find_process_info():
    process_details = []
    com_processes = []
    processes = os.listdir('/proc')
    for i in range(len(processes)):
        a = str(processes[i])
        process_details.append(processes[i])
        try:
            c = subprocess.check_output("ps -p " + a + " -o etime=", shell=True)
            process_details.append(c.strip())
        except subprocess.CalledProcessError:
            process_details.append('X')
        try:
            f = open('/proc/' + a + '/status', 'r')
            b = f.readline()
            process_details.append(b[6:].strip())
        except IOError:
            process_details.append("X")

        com_processes.append(process_details)
        process_details = []
    return com_processes
