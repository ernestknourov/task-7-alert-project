import time
from functions import *

"""
Я предполагаю, что пришедшие журналы с логами пополняют текущую таблицу логов, потому что иначе, можно анализировать только 
пришедший файл, и если он например содержит логи за промежуток 10 минут, то какой смысл говорить о ошибках за последний час, 
этот файл нам всё равно не даст полную информацию. Чтобы полностью отлавливать ошибки нужно иметь все логи за эн-ый прошедший 
промежуток времени, так что мне определенно нужны данные и старых логов. Так как в задани дана одна большая таблица, буду 
условно её рассматривать как пополняющуюся таблицу и с течением времени считывать с неё значения за нужный промежуток, 
имитируя то время, что есть в датасете.

Ещё хочу заметить, что условие довольно строгое: в датасете 83% логов - ошибки, а это 1.2 миллиона, то есть,
в среднем 216 ошибок в минуту, что гораздо больше требуемых для оповещения 10. Можно смело утверждать, что в 
каждый осмотр файла будет оповещение. Вследствие этого, я поменял условие на 100 ошибок в течение минуты и 6000
ошибок в течение часа на bundle_id.
"""


def main():
    data = read_logs(config.path_to_logs)
    start_time = time.time()
    print('done!')
    while True:
        # Imitate time count since the time of the first log
        t = 1631318446 + time.time() - start_time
        if t % 10 <= 0.0001:  # checking for all errors every 10 seconds
            print('Time: ', time.ctime(t))
            r1 = rule1(data, t)
            if r1 >= 100:
                print(f"Error: find {r1} error within a minute\n")
            else:
                print(f"Alright: amount of error({r1}) within a minute is less than 100\n")

        if t % 60 <= 0.0001:  # checking for errors on concrete bundle_id every 1 minute
            print('Time: ', time.ctime(t))
            r2 = rule2(data, t)
            if r2 >= 6000:
                print(f"Error: find {r2} on bundle_id within an hour\n")
            else:
                print(f"Alright: amount of error({r2}) on bundle_id  within an hour is less than 6000\n")
    # print("I'm working!")
    # time.sleep(300)

main()
