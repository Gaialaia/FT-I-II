#  Реализовать простую систему хранения данных о суммах продаж булочной. 
# Должно быть два скрипта с интерфейсом командной строки: 
# для записи данных и для вывода на экран записанных данных.
#  При записи передавать из командной строки значение суммы продаж. 
#  Для чтения данных реализовать в командной строке следующую логику:

#     просто запуск скрипта — выводить все записи;
#     запуск скрипта с одним параметром-числом — выводить 
#     все записи с номера, равного этому числу, до конца;
#     запуск скрипта с двумя числами — выводить записи, начиная 
#     с номера, равного первому числу, по номер, равный второму числу, включительно.

# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.

# Данные хранить в файле bakery.csv в кодировке utf-8. 
# Нумерация записей начинается с 1. Примеры запуска скриптов:

# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5   0
# 8914,3    1
# 7879,1     2
# 1573,7       3
# python show_sales.py 3  
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5 0
# 8914,3
# 7879,1

# write data:
bakery_sales = open ('bakery_sales.csv','a')

# sum_sales = float(input("enter sum: "))

# print(sum_sales, file=bakery_sales)

# with open ('bakery_sales.csv','r') as bs:
#     print(bs.read())  #show all entries

# bakery_sales = open ('bakery_sales.csv','r')

searched_sum = int(input("enter sum: "))
# l = 0
# for line in open('bakery_sales.csv','r'):
#     line = bakery_sales.readline()
#     l = l + 1
#     if searched_sum == str(l):
#         print(searched_sum)


# with open ('bakery_sales.csv','r') as bs:
#     for count,line in enumerate(bs):
            
#             if count >= searched_sum:
#                 print(line)
      

 
with open ('bakery_sales.csv','r') as bs:
    for count,line in enumerate(bs):
            
            if count <= searched_sum:
                print(count,line)
        
        
        

        # print(line)










    # line = bakery_sales.readline()
    # if searched_sum[:] in line:
    #     print(line)
    # elif searched_sum[:2] in line:
    #     print(line)