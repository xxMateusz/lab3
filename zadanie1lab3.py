produkty = input("Podaj produkty odzielone ,")
ceny = input("Podaj ceny odzielone ,")
produktyZBior = set(produkty.split(","))
cenyList= list(ceny.split(","))
my_dict = {}
for item in produktyZBior:
    for value in cenyList:
        my_dict.update({item:value})


print(my_dict)


