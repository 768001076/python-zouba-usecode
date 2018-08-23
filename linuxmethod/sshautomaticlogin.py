#ssh 自动登录
import sys, time, os
try:
  import pexpect
except ImportError:
  print("You must install pexpect module")
  sys.exit(1)
host = ("root@101.236.48.201","VGxR523R4Nup")
server = pexpect.spawn('ssh %s' % host[0])
server.expect('.*ssword:')
server.sendline(host[1])
server.interact()