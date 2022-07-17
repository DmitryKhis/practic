import math

def is_palindrome(word):
    '''
    Проверяет является ли слово полиндромом

    Parameters
    ----------
    word : string

    Returns
    -------
    bool
        True если полиндром,
        False если нет.

    '''
    return word == word[::-1]
    
def is_power(a, b):
    '''
    Проверяет является ли 'a' результатом возведения в степень числа 'b'

    Parameters
    ----------
    a : integer
    b : integer

    Returns
    -------
    bool
        True если является степенью
        False если нет

    '''
    if a == b or a == 1:
        return True
    elif a % b == 0:
        return is_power(a // b, b)
    else: return False
    
def greatest_common_divisor(a, b):
    '''
    Находит наибольший общий делитель

    Parameters
    ----------
    a : ineger
    b : integer

    Returns
    -------
    integer
        Наибольший общий делитель

    '''
    if b == 0:
        return a
    elif a % b != 0:
        return greatest_common_divisor(b, a % b)
    else: return b
    
def mysqrt(a):
    '''
    Находит квадратный корень числа методом Ньютона
    с точностью epsilon

    Parameters
    ----------
    a : integer

    Returns
    -------
    y : integer
        корень квадратный

    '''
    epsilon = 0.000000001
    x = a / 2
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return y

def test_square_root():
    '''
    Тестовая функция для сравнения mysqrt и math.sqrt

    Returns
    -------
    None.

    '''
    # ToDo добавить форматирование выравнивание по столбцам
    print('a' + '  mysqrt  ' + '    math.sqrt  ' + '  diff')
    print('-  ------      ---------    ----')
    for i in range(1,10):
        test_mysqrt = str(mysqrt(i))
        test_sqrt = str(math.sqrt(i))
        diff = math.sqrt(i) - mysqrt(i)
        print(str(float(i)) + '  ' + test_mysqrt + '      ' + test_sqrt
              + '    ' + str(diff))

def length_more(file_name, length = 20):
    '''
    Из файла file_name ищет слова с заданной длиной length

    Parameters
    ----------
    file_name : string
        Путь к файлу
    length : integer, optional
        The default is 20.

    Returns
    -------
    word : str
        Выводит все найденые слова

    '''
    with open(file_name) as file_input:
        for line in file_input:
            word = line.strip()
            if len(word) > length:
                return word          

def double_letter(word):
    '''
    Задача по нахождению слова с 3 подряд сдвоенными буквами

    Parameters
    ----------
    word : string

    Returns
    -------
    bool
        True если в слове есть 3 сдвоенные буквы подряд
        False если нет

    '''
    i, count = 0, 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            i += 2
            count += 1
            if count == 3:
                return True
            else:
                continue
        elif word[i] != word[i+1] and count > 0:
            count = 0
            i += 1
            continue
        i += 1
    return False

def car_talk_task(num):

    '''
    Задача: найти такое 6-ти значное число у которого,
    последние 4 цифры полиндром,
    при +1 последние 5 цифр полиндром,
    при +2 средние 4 цифры полиндром,
    при +3 все цифры полиндром.

    Parameters
    ----------
    num : int

    Returns
    -------
    bool
        Проверяет подходит ли num под условие задачи

    '''
    return (is_palindrome(str(num)[2:]) and 
            is_palindrome(str(num+1)[1:]) and 
            is_palindrome(str(num+2)[1:-1]) and
            is_palindrome(str(num+3)))

def mystery_of_age():
    for num in range(100):
        if num < 10:
            num = int(str.zfill(str(num),2))
        if is_palindrome(str(num)):
            print(num)

if __name__ == '__main__':
    mystery_of_age()
            
                
        

    
    

        
       
    
        
        

