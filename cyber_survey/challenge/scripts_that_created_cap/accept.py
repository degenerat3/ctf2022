import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 82
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 83
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 123
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 115
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 99
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 52
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 110
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 115
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 95
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 98
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 101
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 116
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 116
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 51
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 114
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 95
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 116
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 104
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 97
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 110
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 95
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 52
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 110
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 95
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 104
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 112
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 95
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 100
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 51
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 115
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 107
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 106
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 101
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 116
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 51
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 55
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 53
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 53
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 40000 + 125
sock.bind(('0.0.0.0', port))
print("listening on " + str(port))
sock.listen(1)
conn, addr = sock.accept()
print("accepted")
data = conn.recv(1024)
print("got data")
conn.close()
sock.shutdown(socket.SHUT_RDWR)

