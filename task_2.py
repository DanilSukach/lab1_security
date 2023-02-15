def code(text: str):
    alfavit = " ЕОИАСТНРВМЛДЯУПЗБЬК5ПrЛЙОХШ84У"
    dec_alfavit = "ХЬБЧt1АЫ<Д ЩЪЯФИ>57К2ЕrЛЙОМШ84У"
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
                    a.append(alfavit[place])
                else:
                    a.append(i)

    file = open('output1.txt', 'w')
    for element in a:
        file.write(element)
    file.close()

    

if __name__ == "__main__":
    code("test_2.txt")