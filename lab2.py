names= ["mati","dawid","kacper","adi"]
print(sorted(names))
names.append("gosia")
print(names)
names.insert(2,"marcin")
print(names)
x = names.pop()
print(x)
names.reverse
new_list = [2]
print(new_list[5:10])




zakupy = { "bulka" : 2.5 , "woda gazowana": 4, "chipsy" : 8}
print(sum(zakupy.values()))
print(zakupy)





'''

#figure = ['prostokąt', 'trapez', 'koło', 'trójkąt', 'deltoid']

#while(True):
 #   input_figure = input('Podaj figurę: ')

   # if input_figure in figure:
   #     data = input('Podaj wymiary(bok, wysokość, średnica): ')
   #     dimensions = data.split(' ')
        
   #     if(input_figure == 'prostokąt' and len(dimensions) == 2):
   #         print(f'Pole prostokąta: {int(dimensions[0]) * int(dimensions[1])}')
        
        elif(input_figure == 'trapez' and len(dimensions) == 2):
            print(f'Pole trapezu: {(int(dimensions[0]) * int(dimensions[1]))/2}')
        
        elif(input_figure == 'koło' and len(dimensions) == 1):
            print(f'Pole koła: {(int(dimensions[0])/2)**2 * 3.14}')
            
        elif(input_figure == 'trójkąt' and len(dimensions) == 2):
            print(f'Pole koła: {int(dimensions[0]) * int(dimensions[1]) / 2}')
            
        elif(input_figure == 'deltoid' and len(dimensions) == 2):
            print(f'Pole deltoidu: {int(dimensions[0]) * int(dimensions[1]) / 2}')
        else:
            print("Bledne parametry")
    else:
        print('Nie ma takiej figury')
'''