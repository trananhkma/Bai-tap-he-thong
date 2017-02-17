import commands

with open('output1.txt', 'w') as f:
    f.write(commands.getstatusoutput('grep -rn LOG | grep ".py" | grep -v Binary | grep -v ".tox"')[1])

with open('output1.txt') as f:
    with open('output2.txt', 'a+') as ff:
        LINE = ''
        for line in f:
            if 'LOG = log' not in line:
                LINE = ''
                continue
            if LINE:
                ff.write(LINE)
            LINE = line
