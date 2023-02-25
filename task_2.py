def code(text: str):
    aaaaalfavit = " ОИЕТНСАКЯРМЛПВДЬУЧЙЗЖЭЫГЦ,ФБЮХЩШ"
    dec_alfavit = "cАХ8МrЛО2bКЕДБР74t<1ФУ5 >Ч?ИПaЙЬЫ"
    itog = {}
    a=[]
    with open(text, encoding="utf=8") as f:
        for j in f:
            for i in j:
                if i  in itog:
                    itog[i] += 1
                else:
                    itog[i] = 1
    print(sorted(itog.items(), key=lambda x:x[1], reverse=True)) 
    
    with open(text, encoding="utf=8") as f:
        for j in f:
            for i in j:
                place = dec_alfavit.find(i)
                if i in dec_alfavit:
                    a.append(aaaaalfavit[place])
                else:
                    a.append(i)

    file = open('output_2.txt', 'w')
    for element in a:
        file.write(element)
    file.close()
    
    file = open('alfavit_2.txt', 'w')
    file.write("Ключ: ")
    for element in aaaaalfavit:
        file.write(element)
    file.write("\n")
    file.write("      ")
    for element in dec_alfavit:
        file.write(element)
    file.close()


    

if __name__ == "__main__":
    code("t.txt")