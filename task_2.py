def code(file: str) -> None:
    dec_alfavit = " ОИЕТНСАКЯРМЛПВДЬУЧЙЗЖЭЫГЦ,ФБЮХЩШ"
    alfavit = "cАХ8МrЛО2bКЕДБР74t<1ФУ5 >Ч?ИПaЙЬЫ"
    count = {}
    text = []
    with open(file, encoding="utf=8") as f:
        for j in f:
            for i in j:
                if i in count:
                    count[i] += 1
                else:
                    count[i] = 1
    print(sorted(count.items(), key=lambda x: x[1], reverse=True))

    with open(file, encoding="utf=8") as f:
        for j in f:
            for i in j:
                place = alfavit.find(i)
                if i in alfavit:
                    text.append(dec_alfavit[place])
                else:
                    text.append(i)

    new_file = open('output_2.txt', 'w')
    for element in text:
        new_file.write(element)
    new_file.close()

    new_file = open('alfavit_2.txt', 'w')
    new_file.write("Ключ: ")
    for element in dec_alfavit:
        new_file.write(element)
    new_file.write("\n")
    new_file.write("      ")
    for element in alfavit:
        new_file.write(element)
    new_file.close()


if __name__ == "__main__":
    code("test_2.txt")
