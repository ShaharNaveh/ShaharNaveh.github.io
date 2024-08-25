#!/usr/bin/env python
import csv
import ipaddress
import pathlib

OUTPUT_FILE = pathlib.Path(__file__).parents[1] / "assets" / "cidrs.csv"
BASE_IP = "0.0.0.0"
CIDRS = range(ipaddress.IPV4LENGTH + 1)


def ip_cidr_info(cidr: int) -> dict[str, str | int]:
    ip_network = ipaddress.ip_network(f"{BASE_IP}/{cidr}")

    network_address = ip_network.network_address
    broadcast_address = ip_network.broadcast_address
    num_addresses = ip_network.num_addresses

    usable_host_ip_range = "NA"
    number_of_usable_hosts = 0
    if num_addresses > 2:
        # We have different addresses for network, hosts, broadcast
        first_host = network_address + 1
        last_host = broadcast_address - 1
        usable_host_ip_range = f"{first_host} - {last_host}"
        number_of_usable_hosts = num_addresses - 2

    res = {}
    res["CIDR"] = f"/{cidr}"
    res["Network Address"] = str(network_address)
    res["Usable Host IP Range"] = usable_host_ip_range
    res["Broadcast Address"] = str(broadcast_address)
    res["Netmask"] = str(ip_network.netmask)
    res["Total Number of Hosts"] = f"{num_addresses:3,}".strip()
    res["Number of Usable Hosts"] = f"{number_of_usable_hosts:3,}".strip()
    return res

fieldnames = ip_cidr_info(ipaddress.IPV4LENGTH).keys()

OUTPUT_FILE.chmod(0o644) # Allow write

with OUTPUT_FILE.open(mode="w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for cidr in CIDRS:
        row = ip_cidr_info(cidr)
        writer.writerow(row)

OUTPUT_FILE.chmod(0o444) # Set to readonly
