animals = ['Dog', 'Cat', 'Rabbit', 'Horse', 'Dolphin']
total = 0
for animal in animals:
    from_D = animal.startswith('D')
    is_long = len(animal) > 5 # 5文字より多ければTrue、そうでなければFalse
    if from_D and is_long: # どちらもTrueの場合
        break # ループ終了
    elif not from_D and is_long: # from_DがFalseかつ、is_longがTrue
        total += animal.find('b')
    else:
        total += len(animal) # animalの文字列をtotalに足し込む
print(total)  # 13


'''【実行例】
totalの値は0
totalの値は3
totalの値は6
totalの値は8
totalの値は13
13
'''