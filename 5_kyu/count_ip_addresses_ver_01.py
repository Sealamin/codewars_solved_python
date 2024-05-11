import ipaddress

def ips_between(start, end):
    start_int = int(ipaddress.IPv4Address(start))
    end_int = int(ipaddress.IPv4Address(end))
    return end_int - start_int
