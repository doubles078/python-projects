import psutil

user = psutil.users()[0].name
cpu = psutil.cpu_percent()
mem = psutil.virtual_memory().percent
batt = psutil.sensors_battery().percent
pluggedin = 1 if psutil.sensors_battery().power_plugged else 0
boot = psutil.boot_time()

print(pluggedin)
