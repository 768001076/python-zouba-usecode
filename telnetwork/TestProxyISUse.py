import telnetlib

telnets = [
"192.168.0.136"
]

for te in telnets:
    try:
        t = telnetlib.Telnet(host=te, port=3389, timeout=5)
        print(te,True)
    except Exception as e:
        print(te,False)
