"""
def reverse_words(s):
    a = list(s.split())
    a.reverse()
    st =' '.join(a)
    return st

reverse_words(str(input()))


def filter_list(lst):
    new_list = []
    for i in range(len(lst)):
        if type(lst[i]) != str:
            new_list.append(int(lst[i]))
    print(new_list)
    return new_list

filter_list(input().split())

def add_binary(a,b):
    x = bin(a+b)
    return (x[2:len(x)])

add_binary(1, 1)


def get_sum(a,b):
    summ = 0
    for i in range(min(a,b), max(a,b)+1, 1):
        summ+=i
    return  summ

get_sum(0, -1)

"""
'''
Take 2 strings s1 and s2 including only letters from ato z. 
Return a new sorted string, 
the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.
'''
'''
def longest(a1, a2):
    for i in range(max(len(a1),len(a2))):

longest(input(), input())
'''

'''
def is_leap_year(x):
    return (x % 400 == 0) or (x % 4 == 0 and (x % 100 != 0))


is_leap_year(int(input()))
'''

'''
Дано n-значное целое число N. Определить: входят ли в него цифры 3 и 7.

def is_3_7_in_it(N):
    цprint('3' in str(N) and '7' in str(N))
is_3_7_in_it(int(input()))
'''

# Допишите функцию check_user так, чтобы она по логину пользователя
# проверяла, существует он или нет,
# после чего с помощью вложенного условия проверяла
# правильность пароля этого пользователя.
# Функция должна возвращать только True или False.
# Чтобы вернуть True, напишите "return True";
# чтобы вернуть False, напишите "return False".

'''
user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}
a = str(input())
print(a==a[::-1])
'''



"""
n = 1
while True:
    n += 1
    if n ** 2 > 1000:
        break

print('число', n-1)
"""

'''
list_ = [-5, 2, 4, 8, 12, -7, 5]
# Объявим переменную, в которой будем хранить индекс отрицательного элемента
index_negative = None

for i, value in enumerate(list_):
    if list_[i] < 0:
        print("Отрицательное число: ", value)
        index_negative = i  # перезаписываем значение индекса
        print("Новый индекс отрицательного числа: ", index_negative)
    else:
        print("Положительное число: ", value)
    print("---")
print("Конец цикла")
print()
print("Ответ: индекс последнего отрицательного элемента = ", index_negative)

'''




'''
text = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо -- песнь заводит,
Налево -- сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

text = text.lower()
text = text.replace(" ", "")
text = text.replace("\n", "")
print(text)

count = {}  # для подсчета символов и их количества
for char in text:
   if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
       count[char] += 1
   else:
       count[char] = 1

for char, cnt in count.items():
   print(f"Символ {char} встречается {cnt} раз")
'''


'''
def print_ladder(n):
    for i in range(1, n+1):
        print('*'* i)
    print()
print_ladder(int(input()))
'''

'''
a = float(input())
n = int(input())
s = sum([a**i for i in range(n+1)])
print(s)
'''

'''
n = int(input())
i=2
while n%i!=0:
    i+=1
print(i)
'''

'''
x = int(input())
y = int(input())
i = 1
while x<y:
    x *= 1.1
    i+=1
print(x)
print(i)

'''
'''
хз - не работает пока
st = '523456789'
elems = list(map(int, input().split()))
print(elems)
for index, value in enumerate(st):
    if index in elems:
        print(int(index)-1, int(value), sep='\t')
'''

'''
st = '11000010  11101011  11100000  11100100  11101000  11101100  11101000  11110000'
st = st.replace('  ', '')
print(st)
elems = list(map(int, input().split()))
elems_ready = ''
for j in range(len(elems)):
    print(st[elems[j]-1])
    elems_ready+=st[elems[j]-1]
print(elems_ready)
'''

'''

'''

countries_temperature = [
    ['Thai', [1, 2, 3, 4]],
    ['Russia', [5, 6, 7, 8]]
]
for country in countries_temperature:
    avg_temp = sum(country[1])/len(country[1])
    print(f'Средняя температура в {country[0]} - {avg_temp :.2f}F')


people = {1: {'name':'oleg', 'age':'29'},
          {2: {'name':'ne_oleg', 'age':'21'}}}

avg_age = 0
