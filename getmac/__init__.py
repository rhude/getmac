# Import pyth_arptable, thanks David Francos
from python_arptable import *

__author__ = 'Jeff Rhude'
__email__ = 'jeff@rhude.com'
__version__ = '0.1'

# Just use with "ipaddr", if the arp entry does not exist, returns nothing.
def mac_search(ipaddr):
    for i in ARPTABLE:
        if i['IP address'] == ipaddr:
            hw_address =  i['HW address']
            return hw_address.replace(':',"")



