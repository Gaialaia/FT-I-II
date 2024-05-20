#task_1:

# ngf = open('/home/gaia/nginx_logs','r', encoding="utf-8")
# ln = 0
# for line in open ('/home/gaia/nginx_logs','r'):
#     line = ngf.readline()
#     line = line.rstrip()
#     y = line.replace("-", " ").replace(' " ', " ").replace( '"GET', 'GET').split(" ") 
  
#     dataline = []  
#     dataline.append(y[0])
#     dataline.append(y[7])
#     dataline.append(y[8])
    
   
#     ln = ln + 1
#     while ln <= 7:
#         print(dataline)
#         break



# with open ('/home/gaia/nginx_logs','r', encoding="utf-8") as file:
#     rq = []
#     for line in file:
#         remote_addr = line[:line.find(' ')]
#         request_type = line[line.find('"')+ 1:line.find('"') + 4]
#         requested_resource = line[line.find ('/d'): line.find('HTTP') - 1]
#         tuple_requests = (remote_addr, request_type, requested_resource)
#         rq.append(tuple_requests)
#         print(tuple_requests)


#task_2:
with open ('/home/gaia/nginx_logs','r', encoding="utf-8") as file:
    remote_addr_list = [line[:line.find(" ")] for line in file]

addr_max = max(set(remote_addr_list),key=remote_addr_list.count)
print( "spammer: ", addr_max, "entries: ",remote_addr_list.count(addr_max))









    
# G = (y for y in dataline )

    
# next(G)
    
    
    
    
    
    
    
    
    
    
    
    
    # print("%d: %s" % (ln,line))







# print(y)
# print(len(y))








# for line in ngf:
#     line = line.split(",")
#     print(line)




