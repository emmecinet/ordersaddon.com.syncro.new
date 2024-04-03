import schedule
import time

import sched
import time

def print_event(name, start, test):
    now = time.time()
    elapsed = int(now - start)
    print('EVENT: {} elapsed={} name={}'.format(
        time.ctime(now), elapsed, name))

if __name__ == '__main__':
    scheduler = sched.scheduler(time.time, time.sleep)
    start = time.time()
    print('START:', time.ctime(start))
    data = "2024 3 28 19:40"                  # <--- CAMBIARE LA DATA E L'ORA CON QUELLA DESIDERATA
    delay = time.mktime(time.strptime(data, '%Y %m %d %H:%M')) - time.time()
    scheduler.enter(delay, 1, print_event, ('second', start, 'ciao'))
    scheduler.run()


exit()

def prova1():
    print("ciao1 " + time.time())

def prova2():
    print("ciao2 " + time.time())

def prova3():
    print("ciao3 " + time.time())

#schedule.every(10).seconds.do(job)
#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
#schedule.every().minute.at(":17").do(job)
#schedule.every(10).seconds.do(Categories, name="Peter")
    
schedule.every().hour.at(":00").do(prova1)
schedule.every().hour.at(":05").do(prova2)
schedule.every().hour.at(":10").do(prova3)

while True:
    schedule.run_pending()
    time.sleep(1)