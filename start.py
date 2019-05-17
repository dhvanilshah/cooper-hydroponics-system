from crontab import CronTab

cron = CronTab(user='pi')

sensors = cron.new(command='python3 cooper-hydroponics-system/sensors.py')
sensors.minute.every(2)
sensors.set_comment("sensors")

#light_checker = cron.new(command='python /cooper-hydroponics-system/lights.py')

cron.write()
