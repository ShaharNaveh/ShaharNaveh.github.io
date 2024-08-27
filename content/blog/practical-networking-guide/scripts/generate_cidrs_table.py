#!/usr/bin/env python
import contextlib
import ipaddress
import pathlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterator

BASE_IP = "0.0.0.0"
SEP = " | "

OUTPUT_FILE = pathlib.Path(__file__).parents[1] / "assets" / "cidrs.md"
CIDRS = range(ipaddress.IPV4LENGTH + 1)


@contextlib.contextmanager
def write_ro_file(path: pathlib.Path) -> "Iterator[pathlib.Path]":
    try:
      path.chmod(0o644)  # Allow write
    except FileNotFoundError:
      # We don't care if file doesn't exists yet
      pass
    yield path
    path.chmod(0o444)  # Set to readonly


def ip_cidr_info(cidr: int) -> dict[str, str]:
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
    res["Network Address"] = network_address
    res["Usable Host IP Range"] = usable_host_ip_range
    res["Broadcast Address"] = broadcast_address
    res["Netmask"] = ip_network.netmask
    res["Total Number of Hosts"] = f"{num_addresses:3,}"
    res["Number of Usable Hosts"] = f"{number_of_usable_hosts:3,}"

    info = {k.strip(): str(v).strip() for k, v in res.items()}
    return info



def cidr_info_md_rows():
  for cidr in CIDRS:
    cidr_info = ip_cidr_info(cidr)
    row = "{sep}{data}{sep}".format(sep=SEP, data = SEP.join(cidr_info.values())).strip()
    yield row


headers = ip_cidr_info(ipaddress.IPV4LENGTH).keys()
table_headers = "{sep}{headers}{sep}".format(sep=SEP, headers=SEP.join(headers)).strip()
table_sep = "{sep}{seperator}".format(
    sep=SEP, seperator=f"---{SEP}" * len(headers)
).strip()
table_rows = "\n".join(cidr_info_md_rows())

table = "\n".join([table_headers, table_sep, table_rows])

with write_ro_file(OUTPUT_FILE) as path:
  path.write_text(table)
