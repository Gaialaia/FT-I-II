names = open ('users.csv','r')

hobbies = open('hobby.csv','r')


nh = {}

for line in open ('users.csv','r'):
    line = names.readline()
    cc = line.replace('\n', ' ').replace('\r', ' ')
    cc.split()
print(cc)

 
nh.fromkeys(names.readline(), hobbies.readline())


with open ('users.csv','r') as f:
    line = f.readline()
    line.find('П')
    print(line)





# file = open('nginxshort.txt','r')
# line = file.readline()
# while line:
#     print(line)
#     line= file.readline()
# file.close()






# x = open('x.txt','x')
# import os
# os.remove('x.txt')




# txt = "Hello World"

# # x= txt.count("w")
# # print(x)

# x = txt.partition('W')
# print(x)


ngf = open('nginxshort.txt','r')
for line in open ('nginxshort.txt','r'):
    line = ngf.readline()
    line = line.rstrip()
    line.replace("-", " ").replace(' " ', " ").replace( '"GET', 'GET').split(" ") 

    

nginx = '''93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
'''


nginx.replace("-", " ").replace(' " ', " ").replace( '"GET', 'GET').split(" ") 
n2 = nginx.join(',')


print(n2)

s = " a p p , l, e "
z = s.replace(" ", "")

print(z)