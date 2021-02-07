# тут без валидации входных данных, тк это задача непростая в данном контексте.
def my_print (**kwargs):
    my_list = [];
    for key, val in kwargs.items():
        my_list.append(f"{key}: {val}")
    print(', '.join(my_list))

my_dict = {}
field = ('Имя', 'Фамилия', 'Год рождения', 'Город проживания', 'Email', 'Телефон')
for f in field:
    my_dict[f] = input(f"{f}: ")

my_print(**my_dict)
