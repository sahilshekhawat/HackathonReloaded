from django.shortcuts import render
from models import ProcessInfo
from django.http import HttpResponse
from django_ajax.decorators import ajax
import subprocess
import os


def home(request):
    #info = find_process_info()
    #b = ProcessInfo(process_info=info)
    #b.save()
    return render(request, 'index.html', {})


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


@ajax
def get_cpu_info(request):
    top = subprocess.check_output("top -bn1", shell=True)
    top = top.split('\n')
    #cpu = subprocess.check_output("top -bn1 | grep 'Cpu'", shell=True)
    cpu = top[2][9:13]
    print cpu
    return HttpResponse(cpu, content_type='application/text')


@ajax
def get_tasks_info(request):
    top = subprocess.check_output("top -bn1", shell=True)
    top = top.split('\n')
    #tasks = subprocess.check_output("top -bn1 | grep 'Tasks'", shell=True)
    tasks = top[1][7:-26].split(',')
    for i in range(len(tasks)):
        tasks[i] = tasks[i].strip()
    return HttpResponse(tasks, content_type='application/text')


@ajax
def get_mem_info(request):
    top = subprocess.check_output("top -bn1", shell=True)
    top = top.split('\n')
    #mem = subprocess.check_output("top -bn1 | grep 'KiB Mem'", shell=True)
    mem = top[3][11:].split(',')
    for i in range(len(mem)):
        mem[i] = (mem[i].strip())
    return HttpResponse(mem, content_type='application/text')


@ajax
def get_swap_info(request):
    top = subprocess.check_output("top -bn1", shell=True)
    top = top.split('\n')
    #mem = subprocess.check_output("top -bn1 | grep 'KiB Swap'", shell=True)
    mem = top[4][11:-4].split(',')
    for i in range(len(mem)):
        mem[i] = (mem[i].strip())
    return HttpResponse(mem, content_type='application/text')

#find_process_info()
