n = int(input("Enter the length of the sequence: ")) # Do not change this line
number_1 = 1
number_2 = 2
number_3 = 3

print(number_1)
print(number_2)
print(number_3)
for x in range(0, n):
    number_4 = number_1 + number_2 + number_3
    print(number_4)
    number_1 = number_2
    number_2 = number_3
    number_3 = number_4


    
    




#Á að prenta fyrstu n tölur í röðinni, endar í n
#Tala n byrjar á 1 fer svo í 2
#Plúsar alltaf seinustu 3 tölur á undan, samt bara 1 tölu og fyrstu 2 þangað til það eru komnar nógu margar tölur
#1, 2, 3, 6, 11, 20, 37, ___, ___, ___, … yoyoyooy