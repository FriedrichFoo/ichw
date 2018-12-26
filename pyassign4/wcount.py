#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Friedrich Foo"
__pkuid__  = "1800011746"
__email__  = "1800011746@pku.edu.cn"
"""

import sys
import string
import functools
from urllib.request import urlopen

def wcount(lines,topn =10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    
    # To get the text
    bodylst = lines.split('[Illustration]')  # To delect the Illustration
    txtstr = functools.reduce(lambda x, y : x + y, bodylst) 
    
    # To handle punctuation & capitalization
    punclst = [i for i in string.punctuation]
    punclst.remove("'") 
    punclst.remove('-')  # Considering the logogram
    punclst.append('--') # Considering -- as a dash
    for i in punclst:
        txtstr = txtstr.replace(i,' ')
    alst = txtstr.split()
    txtlst = [i.lower() for i in alst]  # Considering the capitalization
    
    # To get the word list without repetition
    wordlst = []
    for k in txtlst:
        if k not in wordlst:
            wordlst.append(k)
    
    # To get the frequency of each word and sort it
    numlst = [txtlst.count(i) for i in wordlst]
    stalst = list(zip(wordlst,numlst))
    sortlst = sorted(stalst, key=lambda kv:kv[1],reverse = True)
    
    # To give the answer
    mat = "{:10}\t{:6}"
    for num in range(topn):
        print(mat.format(sortlst[num][0],sortlst[num][1]))

if __name__ == '__main__':
    if  len(sys.argv) == 1:
        """ if there is no order, return these guide
        """
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    else:
        # First, get the string from URL
        doc = urlopen(sys.argv[1])
        docstr = doc.read()
        doc.close()
        jstr = docstr.decode('UTF-8')
        if len(sys.argv) == 2:
            """ in this situation, give first 10 words
            """
            wcount(jstr)
        else:
            """ in this situation, give the top n words
            where n is given by users
            """
            wcount(jstr,int(sys.argv[2]))
