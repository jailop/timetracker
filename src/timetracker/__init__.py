"""
A command line tool to track time used to completed tasks
"""

from datetime import datetime
import signal
import time
import os

def record_track(task_description, start, end):
    path = os.path.join(os.path.expanduser('~'), '.config', 'timetracker')
    if not os.path.exists(path):
        os.mkdir(path)
    fname = os.path.join(path, 'log.csv')
    duration = end - start
    if not os.path.exists(fname):
        with open(fname, 'w') as fout:
            fout.write('start,end,duration,description\n')
    with open(fname, 'a') as fout:
        fout.write(f'{start},{end},{duration.total_seconds()},{task_description}\n')
    print(task_description, start, end)

def track(task_description):
    start = datetime.now()
    try:
        while True:
            current = datetime.now()
            print(current - start, end='\r')
            time.sleep(1)
    except KeyboardInterrupt as err:
        end = datetime.now()
        print()
        record_track(task_description, start, end)

def start_tracking():
    task_description = input()
    track(task_description)

if __name__ == '__main__':
    start_tracking()
