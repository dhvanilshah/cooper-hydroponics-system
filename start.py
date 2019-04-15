from crontab import CronTab

cron = CronTab(user='pi')

job1 = cron.new(command='python /cooper-hydroponics-system/test.py')

job1.minute.every(1)

for item in cron:  
    print(item)

cron.write()
