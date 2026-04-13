from time import sleep

import pyads

# connect to plc and open connection
plc = pyads.Connection('5.108.194.44.1.1', pyads.PORT_TC3PLC1)
plc.open()

counter = 0
counter2 = 0
real_val = plc.get_symbol("Main.real_val", auto_update=True)

while counter2 < 100:
    sleep(1)
    i = plc.read_by_name("Main.Test")
    print("i:", i)
    print("Real Value:", real_val.value)
    counter += 1
    if counter >= 20:
        plc.write_by_name("Main.Test", i - 2)
        real_val.value = 5.2
        counter = 0
        counter2 += 1

# write int value by name
plc.write_by_name("Main.Test", 1)

# close connection
plc.close()
