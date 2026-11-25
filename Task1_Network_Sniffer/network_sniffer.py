from scapy.all import sniff, IP, TCP, UDP, Raw, ICMP, IGMP

packet_count = 0


def analyze_packet(packet):
    global packet_count
    packet_count += 1

    if IP in packet:
        ip_layer = packet[IP]

        # Protocol identification
        if TCP in packet:
            protocol = "TCP"
            transport = packet[TCP]

        elif UDP in packet:
            protocol = "UDP"
            transport = packet[UDP]

        elif ICMP in packet:
            protocol = "ICMP"
            transport = None

        elif IGMP in packet:
            protocol = "IGMP"
            transport = None

        else:
            protocol = "Other"
            transport = None

        # Port information
        if transport:
            source_port = transport.sport
            destination_port = transport.dport
        else:
            source_port = "N/A"
            destination_port = "N/A"

        # Payload analysis
        if Raw in packet:
            payload_size = len(packet[Raw].load)
            payload_status = "Payload Available"
        else:
            payload_size = 0
            payload_status = "No Raw Payload"

        # Packet analysis
        print("\n========== PACKET ANALYSIS ==========")
        print("Packet Number:", packet_count)
        print("Source IP:", ip_layer.src)
        print("Destination IP:", ip_layer.dst)
        print("Protocol:", protocol)
        print("Packet Size:", len(packet), "bytes")
        print("IP Version:", ip_layer.version)
        print("TTL:", ip_layer.ttl)
        print("Source Port:", source_port)
        print("Destination Port:", destination_port)
        print("Packet Layers:", packet.summary())
        print("Payload Status:", payload_status)
        print("Payload Size:", payload_size, "bytes")
        print("=====================================")


print("BASIC NETWORK SNIFFER")
print("Capturing 10 packets...")
print("Monitoring authorized network traffic only.")

try:
    sniff(
        filter="ip",
        prn=analyze_packet,
        count=10,
        store=False
    )

except Exception as error:
    print("Capture Error:", error)

print("\nNetwork Sniffer Stopped.")
print("Total Packets Analyzed:", packet_count)