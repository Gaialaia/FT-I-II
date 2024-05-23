
#task_3:

names = open ('users.csv','r')
hobbies = open('hobby.csv','r')
# nh = {names.readline():hobbies.readline()}


nh = {}
# print(nh)

# solution with many dicts
for line in open ('users.csv','r'):
    for line in open ('hobby.csv','r'):
        names_and_hobbies = {k:v for (k,v) in zip([names.readline().replace('\n', '')],\
                            [hobbies.readline().replace('\n', '')])}
        
        print(names_and_hobbies)
    