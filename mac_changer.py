#1/usr/bin/env python

import subprocess
import optparse

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

options = get_args()
change_mac(options.interface, options.address)
