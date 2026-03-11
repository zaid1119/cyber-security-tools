from scapy.all import sniff, IP, TCP, UDP, ICMP
import datetime

# This function will handle each packet we catch
def packet_callback(packet):
    if packet.haslayer(IP):
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = "OTHER"
        
        if packet.haslayer(TCP): proto = "TCP"
        elif packet.haslayer(UDP): proto = "UDP"
        elif packet.haslayer(ICMP): proto = "ICMP"

        # This prints the output we will use for report screenshots
        print(f"[{time_now}] {proto} | Source: {src_ip} -> Dest: {dst_ip}")

print("="*50)
print("   ONEIX - NETWORK TRAFFIC ANALYZER")
print("="*50)
print("Monitoring network traffic... (Press Ctrl+C to stop)")

# Start sniffing (requires Admin rights)
sniff(prn=packet_callback, store=False)