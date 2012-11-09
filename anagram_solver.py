#-------------------------------------------------------------------------------
# Name:        Anagram Solver
# Purpose:
#
# Author:      Rogue
#
# Created:     12-10-2012
# Copyright:   (c) Rogue 2012
#-------------------------------------------------------------------------------

import Tkinter
from time import sleep

words=[]
prev=""

def create_words():
    global words
    a=open("english.dic")
    i=a.readline()
    while i:
        tmp=[]
        for j in i.split():
            tmp+=[j]
        words+=[tmp]
        i=a.readline()
    a.close()

def findword(w,t):
    flag=False
    found=[]
    for i in words:
        if len(i[0])==len(w) and sorted(i[0])==sorted(w):
            for j in i:
                found+=[j]
            flag=True
    if not flag:
        print 'Not found in dictionary!!!'
    else:
        for i in found:
            print i,
    print('\n')


def get_text(t):
    a=''
    while 1:
        sleep(.200)
        try:
            a=t.clipboard_get()
        except:
            pass
        a=a.replace(' ','')
        if '[' in a and ']' in a:
            a=a[a.index('[')+1:a.index(']')]
            break
    return a

def main():
    create_words()
    t=Tkinter.Tk()
    global prev
    while 1:
        sleep(.200)
        a=get_text(t)
        if a != prev:
            prev=a
        else:
            continue
        print a
        findword(a.lower(),t)
    t.destroy()

if __name__ == '__main__':
    main()
