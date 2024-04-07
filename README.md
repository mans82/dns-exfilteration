# DNS Exfilteration

*An assignment for Cybersecurity course, given by Dr. Razian, Spring 2024 (1403)*

The DNS protocol is largely viewed as a harmless protocol and is usually allowed through firewalls. This can be used as an opportunity to bypass many security policies and extract sensitive data that is otherwised not allowed outside the network: by embedding them inside DNS packets!

This repository contains a basic implementation of this sort of attack. Two parties are involved in this attack:

+ **The client:** It resides on the target system, extracts the sensitive data, and sends it to the server, by sending DNS queries to it that contain the data. In our implementation, the client script accepts an arbitary file, and sends out the content of the file.

+ **The server:** It receives the DNS queries, extracts the data portion of it, and stores it for later use. Our implementation simply writes whatever is received into a file.

## Running the project

It is recommended to setup Python virtual environment first. Generate using

```bash
python -m venv .pyenv
```

and activate the venv by running

```bash
source .pyenv/bin/activate
```

Install the dependencies.

```bash
pip install -r requirements.txt
```

Now that your environment is ready, run the server script.

```bash
python server.py
```

Then run the client, and pass it the file you want to transfer.

```bash
python client.py secret-file.bin
```

Output should look like this:

```
 ==> Starting payload transfer...
 ==> Transfer compeleted in 4.27 seconds (238 kb/sec)
```
