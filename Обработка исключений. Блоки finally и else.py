# исключения в момент выполнения - здесь требуется обрабатывать исключения
# исключения при компиляции (до исполнения кода) - здесь требуется правильно писать код


try:
    f = open('myfile.txt')
    f.write('Hello')
    # with open('myfile.txt') as f:  # если используем файловый менеджер, то блок finally уже не нужен
    #     f.write('hello')
except FileNotFoundError as z:
    print(z)
except:
    print('Другая ошибка')
# else: .... # выполняется только если выполняется блок try
finally:
    # print('Блок finally выполняется всегда')
    if f:
        f.close()
        print('Файл закрыт')

# если в функции прописываем блок try/except и finally, то finally выполняется до return
