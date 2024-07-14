#работа со словарем
my_dict={'Mihail': 2014, 'Yaroslav': 2008, 'Valeriy': 1985, 'Taniana': 1989}
print(my_dict)
print(my_dict.get('Mihail'))
print(my_dict.get('Lidiya'))
my_dict.update({'Gregory': 2023, 'Miroslava': 2019})
iskl=my_dict.pop('Taniana')
print(iskl)
print(my_dict)

#работа с множеством
my_set=set_={16, 12, 'world', 'ocean', (1,2,3), 12, 16, 'world', 'ocean', (1,2,3)}
print(set_)
my_set.add('lion')
my_set.add('crash')
my_set.discard(16)
print(my_set)

