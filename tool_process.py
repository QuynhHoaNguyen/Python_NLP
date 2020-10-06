import codecs
import nltk.tokenize
import os

FJoin = os.path.join


def option_input(type_process, type_input, finput):
    if type_input == "file":
        file(type_process, finput)
    elif type_input == "dir":
        folder(type_process, finput)
    elif type_input == "string":
        text(type_process, finput)
    else:
        print("Invalid option")


def file(type_process, path):
    input_file = codecs.open(path, "r", encoding="utf-8")
    Rfile = input_file.read()
    process(type_process, Rfile)
    # input_file.close()
    # return input_file


def GetFiles(path):
    """Output: file_list là danh sách tất cả các file trong path và trong tất cả các
       thư mục con bên trong nó. dir_list là danh sách tất cả các thư mục con
       của nó. Các output đều chứa đường dẫn đầy đủ."""

    file_list, dir_list = [], []
    for dir, subdirs, files in os.walk(path):
        file_list.extend([FJoin(dir, f) for f in files])
        dir_list.extend([FJoin(dir, d) for d in subdirs])
    return file_list, dir_list


def folder(type_process, path):
    files, dirs = GetFiles(os.path.expanduser(path))
    count_file = 0
    count_dir = 0
    for ifile in files:
        count_file = count_file + 1
        print("file ", count_file, ": ")
        print(ifile)
        input_file = codecs.open(ifile, "r", encoding="utf-8")
        Rfile = input_file.read()
        process(type_process, Rfile)
        # input_file.close()

    for dir in dirs:
        count_dir = count_dir + 1
        print("dir ", count_dir, ": ")
        print(dir)


def text(type_process, i_text):
    process(type_process, i_text)


# ----------------------------------------------------
def process(type_process, arg):
    # type_process: tiền xử lý : pp | tách từ : ws | tách câu : ss
    if type_process == "ss":
        processing_sent_split(arg)
    elif type_process == "ws":
        processing_word_split(arg)
    elif type_process == "pp":
        pre_processing(arg)
    else:
        print("Invalid option")


def processing_sent_split(arg):
    print(nltk.sent_tokenize(arg))


def processing_word_split(arg):
    print(nltk.word_tokenize(arg))


def pre_processing(arg):
    newline = "".join(
        u for u in arg if u not in ("?", ".", ";", ",", ":", "!", "...", "-", "+", ")", "(", "_", "<", ">"))
    line = newline.lower().strip()
    print(line)


# def oui_output(type_input, i_input, i_output):
#     if type_input == "file":
#         fin = codecs.open(i_input, "r", encoding="utf-8")
#         fw = codecs.open(i_output, "w", encoding="utf-8")
#         for sent in fin:
#             fw.write(sent + '\n')
#     else:
#         return


# def non_output(type_process, type_input, i_input):
#     if type_input == "file":
#         fin = codecs.open(i_input, "r", encoding="utf-8")
#         if type_process == "pp":
#             fw = codecs.open(i_input + ".pp", "w", encoding="utf-8")
#             for sent in fin:
#                 fw.write(sent + '\n')
#     else:
#         return


def run(type_process, type_input, i_input):
    option_input(type_process, type_input, i_input)


# def run_file(type_process, type_input, i_input, i_output):
#     # type_process: tiền xử lý : pp | tách từ : ws | tách câu : ss
#     # type_input: dir file string
#     # input: link file/folder or text
#     # ouput: link file/folder or text
#     option_input(type_process, type_input, i_input)
#     if i_output is None:
#         non_output(type_process, type_input, i_input)  # them ouput theo đường dẫn
#     else:
#         oui_output(type_input, i_input, i_output)  # them ouput cùng thư mục input
