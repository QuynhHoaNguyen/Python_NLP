import codecs
VW = codecs.open('E:/00_VP_1752017/InternLab/Dict/ VN_Word.txt', "r", encoding="utf-8")
dict = []

# xu ly file tu dien
for lineWord in VW:
    # Dua cac tu vao danh sach
    lineL = lineWord.lower().strip()
    lineS = lineL.split()
    #print(lineL)

#     #Tao mot danh sach moi chứa các từ đơn
    for x in lineS:
        if x not in dict:
            dict.append(x)
# print(dict)


#sort elements in arr dict
# dict.sort()
# print(dict)
lendict = len(dict)
dict.pop(lendict - 1)
dict.pop(0)


#convert list to string
str = ' '.join(dict)
print(str)


# #ghi vao file
fdict = open("myDict.txt", "a", encoding="utf-8")
fdict.write(str)
fdict.close()


# #doc file
fdict = open("myDict.txt", "r", encoding="utf-8")
print(fdict.read())
fdict.close()
VW.close()

