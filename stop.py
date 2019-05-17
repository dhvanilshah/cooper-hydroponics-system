from crontab import CronTab
from modules.lights import lights_off

cron = CronTab(user='pi')

cron.remove_all(comment='sensors')
#cron.remove_all(comment="lights-start")
#cron.remove_all(comment="lights-stop")
#
#lights_off()

cron.write()