import psutil
import datetime
from dbsetup.dbsetup import insert_to_db

user = str(psutil.users()[0].name)
cpu = str(psutil.cpu_percent())
mem = str(psutil.virtual_memory().percent)
batt = str(psutil.sensors_battery().percent)
pluggedin = 1 if psutil.sensors_battery().power_plugged else 0
log = str(datetime.datetime.now().date())
boot = str(psutil.boot_time())

insert_to_db(user, cpu, mem, batt, pluggedin, log, boot)
