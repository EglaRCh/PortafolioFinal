from datetime import datetime

d = datetime(2020, 11, 4, 14, 53)
print(d.strftime("%y/%m/%d %H:%M:%S"))
print(d.strftime("%d/%B/%d %H:%M:%S %p"))
print(d.strftime("%a/, %y %b %d"))
print(d.strftime("%A/, %y %B %d"))
print('Día de la semana:', (d.isoweekday()))

print('Día del año:', (d.timetuple().tm_yday))
print('Día de la semana:', (d.isocalendar().week))