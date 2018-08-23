from linuxmethod.BasicSSHUtil import BasicSSHUtil

if __name__ == '__main__':

    ins = {
        '43.241.238.239': 'SH33JnxnwUdK',
        '101.236.18.73': 'hFJ7a5bB9u59',
        '103.37.148.60': 'NeK7UhEfbR68',
        '43.241.216.24': 'b23nVVMqY4Nz',
        '101.236.35.150': 'Jdqf8h9fEQZj',
        '43.241.212.92': 'KQK8ttAsSw5s',
        '43.241.213.130': 'uv9v3PTUqwzh',
        '101.236.39.56': 'vk26DqdfVxD9',
        '103.37.145.206': 'MM5xkUPb8exX',
        '101.236.17.112': 'Mru58QT5UZZY',
        '101.236.19.51': 'tx7svahKaF2z',
        '43.241.238.232': 'mPGRpG35AUQy',
        '101.236.52.154': '4mpW56N8crSF',
        '101.236.39.14': 'hyE9KZmahYU2',
        '43.241.232.142': 'c9D64ZEUtbvT',
        '101.236.52.52': 'ktzWs4gRk6ar',
        '43.241.238.124': 'qHfv5qWZ4KsE',
        '101.236.41.240': 'Xs8qB9uEwdws',
        '103.37.145.59': '2RAndXFrz4N9',
        '103.37.149.51': 'ZVXFePJc9U7W',
        '103.37.160.147': '35v83Ye4WB9x',
        '43.241.232.242': 'mPE58NCrAsxr',
        '101.236.16.197': '4AsRWUAjK9Sy',
        '43.241.230.11': 'Q2Wwx2WqwszH',
        '43.241.238.174': 'Qb75XW3WT5h4',
        '43.241.217.90': 'sc7k9yj5WzjG',
        '43.241.216.109': 'QuQdDtw7Yr7t',
        '101.236.17.162': 'yVa3ryx8UCUC',
        '43.241.238.233': 'ryNk4XZua6m6',
        '101.236.46.148': 'kZtSWvx5whv9',
        '101.236.17.138': 'cwHvR4vr4wv6',
        '43.241.234.60': 'dUrv3cb7f3zP',
        '101.236.19.100': 'x6YpaaB8b3yk',
        '101.236.21.133': 'wJx7857VWwKU',
        '43.241.236.69': 'E3kEkSHty3Ca',
        '43.241.238.180': 'a6feRQMVdd5A',
        '43.241.230.77': 'nSSRRT3Z7egs',
        '43.241.219.110': 'yv467CzxVtNF',
        '43.241.234.236': 'AtFb8Jv2CV4M',
        '101.236.40.91': 'QrU9ebjRFa4r',
        '43.241.222.37': 'cbbnKUz9JaV5',
        '43.241.234.85': 'PTAcNFuC73wN',
        '43.241.232.247': 'z853vkherNpT',
        '43.241.217.233': 'YyfmSkT8N3VE',
        '101.236.21.57': 'Hb8zEAsj7xqm',
        '43.241.238.69': '25jDVjBst2mx',
        '101.236.16.101': 'pkTu2Q36NuJa',
        '101.236.32.228': 'a8s4r88K0LUQvOoj',
        '101.236.34.122': 'a8s4r88K0LUQvOoj',
        '101.236.32.17': 'a8s4r88K0LUQvOoj',
        '101.236.53.36': 'a8s4r88K0LUQvOoj',
        '101.236.62.210': 'a8s4r88K0LUQvOoj',
        '101.236.52.15': 'a8s4r88K0LUQvOoj',
        '101.236.51.66': 'a8s4r88K0LUQvOoj',
        '101.236.43.28': 'a8s4r88K0LUQvOoj',
        '101.236.32.204': 'a8s4r88K0LUQvOoj',
        '101.236.61.133': 'a8s4r88K0LUQvOoj',
        '43.241.228.144': 'a8s4r88K0LUQvOoj',
        '101.236.50.40': 'a8s4r88K0LUQvOoj',
        '101.236.32.28': 'a8s4r88K0LUQvOoj',
        '101.236.41.6': 'a8s4r88K0LUQvOoj',
        '101.236.52.153': 'a8s4r88K0LUQvOoj',
        '101.236.59.27': 'a8s4r88K0LUQvOoj',
        '43.241.232.121': 'a8s4r88K0LUQvOoj',
        '101.236.45.30': 'a8s4r88K0LUQvOoj',
        '101.236.58.232': 'a8s4r88K0LUQvOoj',
        '101.236.50.182': 'a8s4r88K0LUQvOoj',
        '101.236.37.90': 'a8s4r88K0LUQvOoj',
        '101.236.57.150': 'a8s4r88K0LUQvOoj',
        '101.236.48.141': 'a8s4r88K0LUQvOoj',
        '101.236.33.72': 'a8s4r88K0LUQvOoj',
        '101.236.55.163': 'a8s4r88K0LUQvOoj',
        '101.236.56.112': 'a8s4r88K0LUQvOoj',
        '101.236.41.38': 'a8s4r88K0LUQvOoj',
        '101.236.55.85': 'a8s4r88K0LUQvOoj',
        '101.236.51.199': 'a8s4r88K0LUQvOoj',
        '101.236.46.60': 'a8s4r88K0LUQvOoj',
        '101.236.22.132': 'a8s4r88K0LUQvOoj',
        '101.236.22.161': 'a8s4r88K0LUQvOoj',
        '101.236.59.242': 'a8s4r88K0LUQvOoj',
        '101.236.54.141': 'a8s4r88K0LUQvOoj',
        '101.236.52.74': 'a8s4r88K0LUQvOoj',
        '43.241.232.108': 'a8s4r88K0LUQvOoj',
        '101.236.48.145': 'a8s4r88K0LUQvOoj',
        '101.236.60.71': 'a8s4r88K0LUQvOoj',
        '101.236.47.163': 'a8s4r88K0LUQvOoj',
        '101.236.58.167': 'a8s4r88K0LUQvOoj',
        '101.236.39.72': 'a8s4r88K0LUQvOoj',
        '43.241.232.110': 'a8s4r88K0LUQvOoj',
        '101.236.59.116': 'a8s4r88K0LUQvOoj',
        '101.236.49.236': 'a8s4r88K0LUQvOoj',
        '101.236.40.36': 'a8s4r88K0LUQvOoj',
        '101.236.46.85': 'a8s4r88K0LUQvOoj',
        '101.236.39.142': 'a8s4r88K0LUQvOoj',
        '101.236.54.237': 'a8s4r88K0LUQvOoj',
        '101.236.44.209': 'a8s4r88K0LUQvOoj',
        '43.241.229.163': 'a8s4r88K0LUQvOoj'
    }

    # find /alidata/server/tomcat7/webapps/Reptile/ -regex \".*\.class\|.*\.jar\" -mtime -1 最近一天更改的class
    # stat /alidata/server/tomcat7/webapps/Reptile/WEB-INF/classes/com/ccservice/t12306/method/CreateOrderMethod.class 某个class的详细信息
    # stat /alidata/server/tomcat7/webapps/Reptile/WEB-INF/classes/com/ccservice/t12306/method/CreateOrderMethod.class 某个class的详细信息
    # class_and_jar = "ls /alidata/server/tomcat7/webapps/Reptile/WEB-INF/classes/com/ccservice/t12306/method/CreateOrderMethod.class"
    serverdisk = 'df -lh'
    for host in ins.keys():
        util = BasicSSHUtil(host, 22, "root", ins[host])
        with util.work():
            stdin, stdout, stderr = util.ssh.exec_command(
                serverdisk)
            results = stdout.read()
            resultlist = str(results).replace("b'", "").replace("'", "").strip().split("\\n")
            for result in resultlist:
                if len(result) > 0 and result.find('dev/vda') > 0:
                    print(host, '磁盘使用情况:', result)
