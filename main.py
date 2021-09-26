from transliterate import to_latin, to_cyrillic


text = input("matn kiriting: ")

if text.isascii():                  #agar kiritilgan matn lotin alifbosida (isascii jadvalida) bolsa
    print(to_cyrillic(text))
else:
    print(to_latin(text))
