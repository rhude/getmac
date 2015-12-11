# getmac
Small function to get a mac from an IP. Uses python_arptable.

This will remove ":" from the mac address.

Example:
from getmac import *
print mac_search("192.168.1.2")
