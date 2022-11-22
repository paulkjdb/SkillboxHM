#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['momy', 'dad', 'brother', 'uncle', 'aunt', 'grandfather']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['momy', 165], ['dad', 188], ['brother', 170 ], ['uncle', 175], ['aunt', 160],['grandfather', 185],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

m = momy_height = my_family_height[0][1]
d = dad_heignt = my_family_height[1][1]
b = brother_height = my_family_height[2][1]
u = uncle_height = my_family_height[3][1]
a = aunt_height = my_family_height[4][1]
g = grandfather_height = my_family_height[5][1]

all_height = a+d+b+u+a+g
print ('Рост отца:' + str(dad_heignt))

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

print('Общий рост моей семьи:' + str(all_height))

