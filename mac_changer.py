#1/usr/bin/env python

import subprocess
import optparse
import re

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change the MAC address of.")
    parser.add_option("-m", "--mac", dest="address", help="Desired MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.address:
        parser.error("[-] Please specify a new MAC address, --help for more info")
    return options

def change_mac(interface, address):
    print("[+] Changing mac address for interface {0} to {1}".format(interface, address))
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", address])
    subprocess.call(["ifconfig", interface, "up"])

def get_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-]Could not read MAC address.")

options = get_args()
current_mac = get_mac(options.interface)
print("Current MAC: {}".format(str(current_mac)))

change_mac(options.interface, options.address)
new_mac = get_mac(options.interface)
if new_mac == options.address:
    print("[+]Your MAC address has been successfully changed and verified!")
    print("[+]New MAC: {0} --- Old MAC: {1}".format(new_mac, current_mac))
else:
    print("[-]There was an issue in verifying and changing your MAC address.")

