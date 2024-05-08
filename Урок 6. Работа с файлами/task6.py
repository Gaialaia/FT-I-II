# with open ("/home/gaia/nginx_logs",'r') as file1:
#     file1.readline()
#     print(file1)


file2 = open ("/home/gaia/nginx_logs",'r')
print(file2.readline())


lines = (line for line in file2)
# print(list(lines))

print(type(lines))


ngf = open ("nginxshort.txt",'r')

print(ngf.readline())

# l1 = []
# l2 = []
# l3 = []

# for line in open(ngf):
#     str_addr, str_type, str_resource = line.strip().split()

#     l1.append(str_addr)
#     l2.append(str_type)
#     l3.append(str_resource)

# print(f'{l1=}, {l2=}. {l3=}')


