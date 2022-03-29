import socket

flag = "RS{sc4ns_bett3r_than_4n_hp_d3skjet3755}"
dsthost = "192.168.50.128"
ordlist = []
for char in flag:
    ordlist.append(ord(char))

print(ordlist)

out = open('accept.py', 'w+')
out.write("import socket\n\n")
for i, num in enumerate(ordlist):
    stri =f"""sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + {num}
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)\n
"""
    out.write(stri)
out.close()

out2 = open('send.py', 'w+')
out2.write("import socket\nimport time\n\n")
for i, num in enumerate(ordlist):
    for j in range((num-5), num+5):
        port = 40000 + j 
        stri =f"""print("scanning {port}")
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("{dsthost}", {port}))
        s.sendall(b"garbage")
        time.sleep(0.25)
except:
    print("refused")
    pass
    \n"""
        out2.write(stri)