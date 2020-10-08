def annotations(word1, word2):
    """
    РЕШЕНИЕ №! (костыльное)
    я составляю из первого и второго слова массивы, элементами которых являются буквы этих слов
    после чего я перекидываю элементы одного массива букв в другой массив, и далее,
    с помощью функции set() удаляю повторяющиеся элементы. Если после такой сортировки кол-вол элементов массива
    равно кол-ву элементов наших двух изначальных массивов (list_word1 & list_word2), то можно утверждать, что
    слова являются анаграммами
    """
    list_word1 = list(str(word1).lower())
    list_word2 = list(str(word2).lower())

    len_word1 = len(list_word1)
    len_word2 = len(list_word2)

    for word in list_word2:
        list_word1.append(word)

    a = set(list_word1)

    if len(a) == len_word1 and len(a) == len_word2:
        return True
    else:
        return False


print(annotations(input('Введите слово 1: '), input('Введите слово 2: ')))
