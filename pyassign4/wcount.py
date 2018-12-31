#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Friedrich Foo"
__pkuid__  = "1800011746"
__email__  = "1800011746@pku.edu.cn"
"""

import sys, string, functools, urllib.error
from urllib.request import urlopen

def record(aline):
    """count words from one line of the whole and record them
    considering Illustration punctuation and capitalization
    Return: an updated dict
    """
    # delect the Illustration
    bodylst = aline.split('[Illustration]')  
    linestr = functools.reduce(lambda x, y : x + y, bodylst) 
    
    # handle punctuation & capitalization
    punclst = [i for i in string.punctuation]
    punclst.remove("'") 
    punclst.remove('-')
    for i in punclst:
        linestr = linestr.replace(i,' ')
        alst = linestr.split()
        txtlst = [i.lower() for i in alst]
        # Considering the capitalization
    
    # record the words found and update worddict
    for j in txtlst:
        if j not in worddict:
            worddict.update({j:1})
        else:
            worddict[j] += 1
    

def wcount(lines, topn = 10):
    """count words from lines of text string, 
    then sort by their counts in reverse order, 
    output the topn (word count), each in one line. 
    """
    global worddict
    worddict = {}
    # record words each line by each
    linestr = lines.readline().decode() 
    while linestr:
        record(linestr)
        linestr = lines.readline().decode()
    
    # sort the worddict to construct a wordlist
    wordlist = sorted(worddict.items(),\
                      key=lambda x:x[1],reverse = True)
    
    # get all words if lenth is less than number
    print(' '*3+'Word'.ljust(30),'Times'.center(10))
    for num in range(min(len(wordlist),topn)):
        print(' '*3+wordlist[num][0].ljust(30),\
              str(wordlist[num][1]).center(10))
    
if __name__ == '__main__':
    if  len(sys.argv) == 1 or len(sys.argv) > 3:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output.'+
              ' If not given, will output top 10 words')
        sys.exit(1)
    else:
        # first, test the URL
        try:
            doc = urlopen(sys.argv[1])
        except urllib.error.URLError:
            print(sys.exc_info()[1])
        except urllib.error.HTTPError:
            print(sys.exc_info()[1])
        except ValueError:
            print(sys.exc_info()[1])
        
        # then, test the number
        else:  
            try:
                sys.argv[2].isdigit()
            except IndexError:
                wcount(doc)
            else:
                if not sys.argv[2].isdigit():
                    print('Invalid number input.'+
                          'Check and reinput number.')
                    sys.exit(1)
                else:
                    wcount(doc, int(sys.argv[2]))
