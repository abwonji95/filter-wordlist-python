"""
fuction to count number of lines in the wordlist file.
note: when run inside customize_worlist() function it writes empty file.
"""
def count_length(myfile):
    with open(myfile, 'r',encoding="utf8") as fp:
        lines = len(fp.readlines())
        print(lines)
    return lines

"""
function to customize wordlist
"""

def customize_wordlist(my_wordlist,new_wordlist,my_length):
    print("starting now")
    file1 = open(my_wordlist, "r",encoding="utf8")
    file2 = open(new_wordlist, "w",encoding="utf8") 
    lst = [] 
    x=count_length(my_wordlist)
    print(x)
    for i in range(x):
        mystring=file1.readline(i)
        if len(mystring)>=int(my_length):
            lst.append(mystring)
        
    file1.close()
    file2.writelines(lst) 
    file2.close() 
    print("finished writting file")

"""
function to get user inputs i.e wordlist,final worlist name and number characters to filter
"""

def get_file_details():
    print("Enter name of the wordlist:")
    my_wordlist = input()
    print("Enter name of the filtered wordlist:")
    filtered_wordlist = input()
    print("Enter length to customize :")
    my_length = input()

    customize_wordlist(my_wordlist,filtered_wordlist,my_length)

get_file_details()
