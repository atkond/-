import subprocess
from subprocess import PIPE
import random


def result(a):
    for i in range(len(a) - 2):
        if a[i] > a[i + 1]:
            return 'false'
    return 'true'


f = input()

b = 1;
b = random.randint(b, 100+b)

for j in range(1, 101):

    if j < 10:
        inp_t = '../input/input00'+str(j)+'.txt'
        inp = open(inp_t, 'w+')
        out = open('../output/output00'+str(j)+'.txt', 'w')
    elif j < 100:
        inp_t = '../input/input0'+str(j)+'.txt'
        inp = open(inp_t, 'w+')
        out = open('../output/output0'+str(j)+'.txt', 'w')
    else:
        inp_t = '../input/input100.txt'
        inp = open(inp_t, 'w+')
        out = open('../output/output100.txt', 'w')

    b += 100
    inp.write(str(b)+'\n')

    for k in range(b):
        n = str(random.randint(1, 100))
        inp.write(n+' ')

    inp.close()

    cmd = subprocess.Popen("../" + f + " " + inp_t, stdout=PIPE)
    print(j)
    cmd_out, cmd_err = cmd.communicate()

    to_file = cmd_out.decode("utf-8")

    checking = [int(item) for item in to_file.split()]
    out.write(str(b)+'\n'+to_file+'\n'+ result(checking))

    out.close()