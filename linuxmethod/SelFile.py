from linuxmethod.BasicSSHUtil import BasicSSHUtil

if __name__ == '__main__':
    ins = {
        "43.241.228.147": "E5HYjGcD68PS",
        "101.236.52.68": "Arkge9jhqs3T"
    }

    command = "less /etc/hosts"
    for host in ins.keys():
        util = BasicSSHUtil(host, 22, "root", ins[host])
        with util.work():
            stdin, stdout, stderr = util.ssh.exec_command(
                command)
            results = stdout.read()
            print(host,results)
            resultlist = str(results).replace("b'", "").replace("'", "").strip().split("\n")
            for result in resultlist:
                if len(result) > 0:
                    print(host, result)