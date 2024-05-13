f = open ('time&temp.txt','r')
times = []
temps = []

for line in open ('time&temp.txt', 'r'):
    str_time,str_temp = line.strip().split()
    hr,mn = str_time.split(':')
    if mn == '00':
        times.append(int(hr))
        temps.append(float(str_temp))
print(f'{times=}, {temps=}')
