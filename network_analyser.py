import scapy.all as scapy

def sniff_packets(interface):
    scapy.sniff(iface=interface, prn=process_packet, store=False)
def process_packet(packet):
    print(packet.summary())
# Example usage
interface = input("Enter the network interface to sniff: ")
sniff_packets(interface)