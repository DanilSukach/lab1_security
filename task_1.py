
def code(text: str):
    alfavit = "АБВГДЕЖЗИЙКЛМОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    dec_alfavit = "ГДЕЖЗИЙКЛМОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВ"
    itog = []

    with open(text, encoding="utf=8") as f:
        for j in f:
            for i in j:
                i = i.upper()
                place = alfavit.find(i)
                if i in alfavit:
                    itog.append(dec_alfavit[place])
                else:
                    itog.append(i)

    file = open('output.txt', 'w')
    for element in itog:
        file.write(element)
    file.close()

    file = open('alfavit.txt', 'w')
    for element in alfavit:
        file.write(element)
    file.write("\n")
    for element in dec_alfavit:
        file.write(element)
    file.close()


if __name__ == "__main__":
    code("test.txt")
