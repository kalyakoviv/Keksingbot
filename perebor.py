# import json
#
# my_json_string = """ {
#     "123": ["23232332", "2222"],
#     "222": ["323232"],
#     "270438582": ["610044723", "213333001", "608328981", "213333001"],
#     "512599868": ["270438582", "974428130"], "974428130": ["512599868"]} """
#
# print(type(my_json_string))
#
# data = json.loads(my_json_string)
# print(type(data))
# print(type(data['123']))


# num = (5, 10, 15)
# for elem in num:
#     print (elem)

# a = (10, 20, 30)
# summa = 0
# for number in a:
#     summa = summa + number
# print(summa)

# for i in range(0,14):
#     print(i)

# cars = ["mazda", "opel", "audi", "honda","cars"]
# for i in range(len(cars)):
#     for :
#         print(cars[i])








# 'apple' in a_dict.values()
# True
# 'onion' in a_dict.values()
# False
# from typing import List

slovar2 = {}

slovar = {
    "123": ["23232332", "2222","123"],
    "222": ["323232"],
    "270438582": ["610044723", "213333001", "608328981", "213333001"],
    "512599868": ["270438582", "974428130"],
    "974428130": ["512599868"]}

for key in slovar.keys():
    for value in slovar[key]:
        if key == value:
            slovar2[key]=value
print(slovar2)
#     print(slovar[key])
# new_dict = {value: key for key, value in slovar.items()}
#     print(new_dict)

# for key, value in slovar.items(): - преобразует в вид 123 -> ['23232332', '2222', '123']
#     print(key, '->', value)

# for item in slovar.items(): преобразует к виду ('123', ['23232332', '2222', '123'])
#     print(item)

# for key in slovar:
#     print(key, '->', slovar[key]) - преобразует в вид 123 -> ['23232332', '2222', '123']

# for i in slovar:
#     if slovar.keys() == slovar.get("123","222","270438582"):
#         print(slovar)

# print(slovar.get("222")) - значение по ключу
# print(slovar.keys()) - все ключи из словаря
# print(slovar["222"])



