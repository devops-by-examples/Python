#########################################################################
# Author: Bhavya Bojanapalli
# This function is to check if a Substring is Present in a Given String
#########################################################################

def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")
            
def main():
    string = "This is python practice"
    sub_str ="python"
    check(string, sub_str)

main()
