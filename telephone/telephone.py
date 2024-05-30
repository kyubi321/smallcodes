# importing necessary modules
import time
import random
import threading
from datetime import datetime

# implement a call log  queue using list
call_logs = []
lock = threading.Lock()

# implement a function that takes the current time and append it to the queue
def call():
    with lock:
        v = time.time()
        #print(v)
        call_logs.append(v)
    return call_logs

# implement a function call_ret that returns the last 10 min call logs
def call_ret():

    current_time = time.time()
    with lock:
        count = 0
        for i in call_logs:
            # for checking the prog purpose reduce the time 600 sec to 30 or 10 sec
            if current_time - i <= 10:
                count += 1
                #print("################")
                f = datetime.fromtimestamp(i).strftime('%H:%M:%S')
                print(f)
        print(f" no of calls recieved last 10 min:{count}")

# implement a function to call the call function randomly

def call_calling():
    end_time = time.time() + 1000
    while time.time() < end_time:
        delay = random.uniform(1, 10)
        time.sleep(delay)
        call()

# create a thread to run the call_calling function.
call_thread = threading.Thread(target=call_calling)
call_thread.start()

# create a function to allow user to enter choice and retrieve the records.
def print_call_logs():

    while True:
        choice = input("want to see the call logs(type 'y' ) or  want to exit (type 'e' ) :")
        if choice =="y":
            call_ret()
        else:
            call_thread.join()
            print_thread.join()
            break

# create another thread that runs print_call_logs.
print_thread = threading.Thread(target=print_call_logs)
print_thread.start()

