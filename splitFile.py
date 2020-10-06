import codecs
import nltk

finput = codecs.open('E:/00_VP_1752017/InternLab/Doc/alignment/Sans Famille Chapitre2.txt', "r", encoding="utf-8")

fReadV = codecs.open('myDict.txt', "r", encoding="utf-8")
fReadF = codecs.open('E:/00_VP_1752017/InternLab/Dict/FR_Word.txt', "r", encoding="utf-8")
list_Vi_syl = fReadV.read().strip().split()
list_Fr_syl = fReadF.read().strip().split()
# print(list_Fr_syl)
# print(list_Vi_syl)
def intersection(lst1, lst2):
    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return lst3


def check_Vi_Fr(sen):
    sen = sen.lower().replace("!", "").replace("- ", "").replace(".", "").replace(",", "").replace("?", "").replace(":", "")
    tokens = nltk.word_tokenize(sen)
    interV = intersection(tokens, list_Vi_syl)
    interF = intersection(tokens, list_Fr_syl)
    if len(interV) > len(interF):
        return True
    else:
        return False
#doc_id = 1
main_lst = []

for doc in finput:
    docx = doc.strip()
    print(len(docx))
    if len(docx) > 0:
        main_lst.append(docx)
    else:
        # print(len(main_lst))
        fw_vi = codecs.open('split_data/vi.txt', "w", encoding="utf-8")
        fw_fr = codecs.open('split_data/fr.txt', "w", encoding="utf-8")

        for sen in main_lst:
            if check_Vi_Fr(sen):
                fw_vi.write(sen + '\n')
            else:
                fw_fr.write(sen + '\n')

        # doc_id += 1
        main_lst.clear()
        fw_vi.close()
        fw_fr.close()
    # print(docx)
finput.close()
fReadV.close()
fReadF.close()
