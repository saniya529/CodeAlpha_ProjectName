
from scapy.all import sniff, IP, TCP, UDP

packet_count = 0

def analyze_packet(packet):
    global packet_count
    packet_count += 1

    if IP in packet:
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        else:
            protocol = "Other"

        print("\n----------------------------")
        print("Packet Number:", packet_count)
        print("Source IP:", source_ip)
        print("Destination IP:", destination_ip)
        print("Protocol:", protocol)
        print("Packet Size:", len(packet), "bytes")
        print("----------------------------")


print("BASIC NETWORK SNIFFER")
print("Capturing 10 packets...")

try:

    sniff(
        filter="ip",
        prn=analyze_packet,
        count=10,
        store=False
    )

except Exception as error:
    print("Error:", error)

print("Network Sniffer Stopped.")
