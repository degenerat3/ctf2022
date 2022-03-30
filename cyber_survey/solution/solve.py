from scapy.all import *
numbers = []
packets = rdpcap("cap.pcapng")  #open the PCAP
for packet in packets:
    flgs = packet[TCP].flags        # get the flags
    if "P" in flgs:                 # if it's a "push" packet
        print(packet.summary())
        print(packet[TCP].dport)
        num = packet[TCP].dport - 40000 # get the dst port and trim it down a bit
        numbers.append(num)             # track the trimmed number in our array

outstr = ""
for num in numbers: #iterate through all the trimmed numbers we collected
    outstr += chr(num)  # get the unicode character for each one, append to string
print(outstr)   # this is the flag