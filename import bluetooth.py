import bluetooth
nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
     print(" %s - %s" % (addr, name))
def connect_to(target_name):
     target_address = None

     nearby_devices = bluetooth.discover_devices()

     for bdaddr in nearby_devices:
        if target_name == bluetooth.lookup_name( bdaddr ):
         target_address = bdaddr
         break

     if target_address is not None:
       print("found target bluetooth device with address ", target_address)
     else:
       print ("could not find target bluetooth device nearby")


