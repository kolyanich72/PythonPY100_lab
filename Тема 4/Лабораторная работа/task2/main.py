def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
    l1 = "".join(str_.lower().split())

    for i in range(len(l1)):
        if l1[i] not in vocab:
            if l1[i].isalpha():
                vocab[l1[i]] = 1
        else:
            vocab[l1[i]] += 1
#    count_char(vocab)
    return vocab


 # Функция возвращает новый словарь,где количество каждого элемента заменено на процентное отношение ко всем символам
def count_char(vocab_):
    s = sum(vocab_.values())
    voc_new = {}
    for i in vocab_:
        voc_new[i] = round(vocab_[i]/s * 100, 2)
  #  print(s)
  #  print(voc_new)



main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
vocab = {}
print(get_count_char(main_str))
