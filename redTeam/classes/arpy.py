import scapy.all as s

list_IP = list()

### Getting the whole subnet IP address
def arpy(snet):
    arp = s.ARP(pdst=snet)
    bcast = "ff:ff:ff:ff:ff:ff"
    broadcast = s.Ether(dst=bcast)

    request_broadcast = broadcast / arp
    clients = s.srp(request_broadcast, timeout =1, verbose=0)[0]
    for element in clients:
        list_IP.append(element[1].psrc)
    return list_IP
        