# with open ("/home/gaia/nginx_logs",'r') as file1:
#     file1.readline()
#     print(file1)


# file2 = open ("/home/gaia/nginx_logs",'r')
# print(file2.readline())


# lines = (line for line in file2)
# print(list(lines))




#ngf = open('nginxshort.txt','w')
#ngf.seek(0)
#ngxstr = '''93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
# 93.180.71.3 - - [17/May/2015:08:05:23 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
# 80.91.33.133 - - [17/May/2015:08:05:24 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)"
# 217.168.17.5 - - [17/May/2015:08:05:34 +0000] "GET /downloads/product_1 HTTP/1.1" 200 490 "-" "Debian APT-HTTP/1.3 (0.8.10.3)"
# 217.168.17.5 - - [17/May/2015:08:05:09 +0000] "GET /downloads/product_2 HTTP/1.1" 200 490 "-" "Debian APT-HTTP/1.3 (0.8.10.3)"
# 93.180.71.3 - - [17/May/2015:08:05:57 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
# 217.168.17.5 - - [17/May/2015:08:05:02 +0000] "GET /downloads/product_2 HTTP/1.1" 404 337 "-" "Debian APT-HTTP/1.3 (0.8.10.3)"
# 217.168.17.5 - - [17/May/2015:08:05:42 +0000] "GET /downloads/product_1 HTTP/1.1" 404 332 "-" "Debian APT-HTTP/1.3 (0.8.10.3)"
# 80.91.33.133 - - [17/May/2015:08:05:01 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)"
# 93.180.71.3 - - [17/May/2015:08:05:27 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
# 217.168.17.5 - - [17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"
# 188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"
# 80.91.33.133 - - [17/May/2015:08:05:14 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.16)"
# 46.4.66.76 - - [17/May/2015:08:05:45 +0000] "GET /downloads/product_1 HTTP/1.1" 404 318 "-" "Debian APT-HTTP/1.3 (1.0.1ubuntu2)"
# 93.180.71.3 - - [17/May/2015:08:05:26 +0000] "GET /downloads/product_1 HTTP/1.1" 404 324 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
# 91.234.194.89 - - [17/May/2015:08:05:22 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"
# 80.91.33.133 - - [17/May/2015:08:05:07 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)"
# 37.26.93.214 - - [17/May/2015:08:05:38 +0000] "GET /downloads/product_2 HTTP/1.1" 404 319 "-" "Go 1.1 package http"
# 188.138.60.101 - - [17/May/2015:08:05:25 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"
# '''

# ngf.write(ngxstr)
# ngf.close()


ngf = open('nginxshort.txt','r')
# ln = 1

# line = ngf.readline()
# while line != " ":
#     line = line.rstrip()
#     ln = ln +1 
#     line = ngf.readline()
# ngf.close()




# for line in open('nginxshort.txt','r'):
#     line = ngf.readline()
#     line = line.rstrip()
#     y = line.replace("-", " ").replace(' " ', " ").split(" ") 
  
#     dataline.append(y[0])
#     dataline.append(y[7])
#     dataline.append(y[8])
#     ln = ln + 1
# print(dataline)
    
    
    
# ngf = open('nginxshort.txt','r')
# line = ngf.readline()
# line = line.rstrip()
# y = line.replace("-", " ").replace(' " ', " ").split(" ") 
# ln = ln + 1
# dataline.append(y[0])
# dataline.append(y[7])
# dataline.append(y[8])
# # ln = ln + 1

# print(dataline,ln)

ln = 0
for line in open ('nginxshort.txt','r'):
    line = ngf.readline()
    line = line.rstrip()
    y = line.replace("-", " ").replace(' " ', " ").split(" ") 
    
    dataline = []  
    dataline.append(y[0])
    dataline.append(y[7])
    dataline.append(y[8])
    
   
    ln = ln + 1
    while ln <= 5:
        print(dataline)
        break




    
# G = (y for y in dataline )

    
# next(G)
    
    
    
    
    
    
    
    
    
    
    
    
    # print("%d: %s" % (ln,line))







# print(y)
# print(len(y))








# for line in ngf:
#     line = line.split(",")
#     print(line)




