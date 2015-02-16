import jsonrpclib
from creds import ip, port, username, password

def getOctetsViaEapi(username, password, ip, port):

  switch_url = 'https://{}:{}@{}:{}'.format(username, password, ip, port)

  switch_url += '/command-api'

  remote_connect = jsonrpclib.Server(switch_url)

  response = remote_connect.runCmds(1, ['show interfaces'])

  response = response[0]['interfaces']

  print 'Interface counters for {}:'.format(ip)

  for anInt in sorted(response):
    try:
      print '{0} inOctets: {1:10d}   outOctets: {2:10d}'.format(
        anInt.ljust(15),
        response[anInt]['interfaceCounters']['inOctets'],
        response[anInt]['interfaceCounters']['outOctets'])
    except KeyError:
      continue

if __name__ == '__main__':
  getOctetsViaEapi(username, password, ip, port)
  
