# longest palindrome
#
# Usage: palindrome.py ./inputdata.txt
# sample file "inputdata.txt" has palindrome such as palindromic number (optional) other strings
# e.g. 1221 -> return 1221
#      121  -> return 121
#      1213 -> return 121
#      33368088588086    -> return 333
#

import sys

def is_palindromic(words):
    # return palindrome is same as input words
    return words == words[::-1]

def get_left_palindrome(words):
    palindrome = words
    while not is_palindromic(palindrome):
        palindrome = palindrome[:-1]
    return palindrome

def main(argv):
    assert argv

    inputfile_path = argv[0]
    source_data = open(inputfile_path, "r")
    
    # ファイルの1行目を読み込む（空白、改行除く）
    line_of_1st = str.strip(source_data.readline())
    source_data.close()

    print (get_left_palindrome(line_of_1st))

if __name__ == '__main__':
    main(sys.argv[1:])