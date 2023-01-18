import time


def time_execution(func):
    def _wrapper(*args, **kwargs):
        t_start = time.perf_counter()
        func(*args, **kwargs)
        all_time = time.perf_counter() - t_start
        print(f'Время выполнения функции: {all_time} c')
    return _wrapper

@time_execution
def function_print():
    print("Слово тест тысяча раз\n" * 1000)

function_print()

#Вывод
Слово тест тысяча раз

Время выполнения функции: 0.8783277809998253 c
