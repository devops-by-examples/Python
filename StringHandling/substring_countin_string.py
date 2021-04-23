#########################################################################
# Author: Bhavya Bojanapalli
# This function returns the substring count in the given list of strings.
#########################################################################

def check(s1,s2):
    match={}
    for i in s1:
         if(i.count(s2)>0):
            match[i] = i.count(s2)
    return match          


def main():
    s1=["john","david","johnho"]
    s2="john"
    match=check(s1,s2) 
    print(match)
  
main()
