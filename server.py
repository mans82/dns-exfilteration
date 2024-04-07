from dnslib.server import DNSServer, DNSLogger
from dnslib.fixedresolver import FixedResolver

from base64 import b64decode


class FileLogger(DNSLogger):
    def __init__(self, filename):
        super(FileLogger, self).__init__(
            "-recv,-send,+request,-reply,-truncated,-error,-data")
        self.filename = filename

        # create an empty file
        with open(self.filename, 'w') as _:
            pass

    def log_request(self, _, request):
        domain_name = request.q.qname.idna()
        raw_payload = domain_name.split(".")[0]
        decoded_payload = b64decode(raw_payload)

        with open(self.filename, 'ab') as f:
            f.write(decoded_payload)


def main():
    server = DNSServer(FixedResolver(". 60 IN A 5.237.2.3"),
                       logger=FileLogger('/tmp/receiveddata.bin'), port=5053)
    server.start()


if __name__ == '__main__':
    main()
