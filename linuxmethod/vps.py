from linuxmethod.BasicSSHUtil import BasicSSHUtil

if __name__ == '__main__':
    vps = {
        "183.131.246.178:20008": "124cab5c",
        "61.130.181.232:20254": "75430923",
        "61.160.208.186:20004": "4eadfd92",
        "61.160.208.186:20008": "4eadfd92",
        "61.160.208.186:20024": "4eadfd92",
        "61.160.208.186:20026": "4eadfd92"
    }
    command = 'ifconfig'
    for vpsip_port in vps.keys():
        info = vpsip_port.split(":")
        util = BasicSSHUtil(info[0], int(info[1]), "root", vps[vpsip_port])
        try:
            with util.work():
                stdin, stdout, stderr = util.ssh.exec_command(
                    command)
                results = stdout.read()
                resultlist = str(results.decode('utf-8')).replace("b'", "").replace("'", "").strip().split("\n")
                for result in resultlist:
                    if 'P-t-P' in result:
                        print(vpsip_port, result[result.find('inet addr:') + 10:result.find('P-t-P') - 2])
        except Exception as e:
            print(vpsip_port, e)
