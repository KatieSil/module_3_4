def single_root_words(root_word, *other_words) :
    same_words = []
    root_word = root_word.lower()
    for i in other_words :
        i1 = i.lower()
        if i1.count(root_word) == True or root_word.count(i1) == True :
            # print(f'{root_word} - {i}')
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

