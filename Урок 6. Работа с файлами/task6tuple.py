

ngf = open('nginxshort.txt','r')
line = ngf.readline()
f = line.partition('-')
print(f)

# L = [('adress', 'type', 'src')]



# T = ('adress', 'type', 'src')

# ip = []
# t = []
# source = []

# for line in open('nginxshort.txt','r'):
#     cleanline = line.strip().split()
#     cl = line.replace("-", " ").replace(' " ', " ").split(" ") 
#     # print(cleanline)
#     print(cl)
    
# h = [(one_line.replace("-", " ").replace(' " ', " ").split()) for one_line in open ('nginxshort.txt','r' )]



# print(h[0])






ngf = open('nginxshort.txt','r')
line = ngf.readline()
nl = line.rstrip()
print(nl)