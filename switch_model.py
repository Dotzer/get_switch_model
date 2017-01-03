#!/usr/bin/python
import telnetlib
import sys

qtech_login = [r"Username\(", r"login\:"]
dlink_login = [r"serName\:"]
login = qtech_login + dlink_login
tl_password = [r"assword\(",r"assword\:",r"assWord\:"]
models = [r'2800-28', r'2850-28', r'2910-52', r'2900-24', r'3000-24', r'3000-26', r'2800-10']
prompt = [r'\#', r'\>']

def log_in(manu):
    tn.write('marvin\n')
    tn.expect(tl_password)
    tn.write('marvingfhjkm\n')
    tn.expect(prompt)
    if manu == 'qtech':
        tn.write('show ver\n')
    elif manu == 'dlink':
        tn.write('show switch\n')
    model_v = tn.expect(models, 3)
    return model_v[0]


host = sys.argv[1]
tn = telnetlib.Telnet(host)
login_out = tn.expect(login,3)
if login_out[0] >= 0 and login_out[0] < 2:
    result = log_in('qtech')
elif login_out[0] >1:
    result =  log_in('dlink')
else:
    print 'Unknown'
if not result == -1:
    print models[result]
else:
    print 'Unknown'
tn.close()
