#########################################################################
# Author: Bhavya Bojanapalli
# This function replaces space delimiter with - hyphen.
#########################################################################

def find_longest_word(string):
    return "-".join( string.split())
    
def main():
    out = find_longest_word("This is a string")
    print(out)
    
main()
