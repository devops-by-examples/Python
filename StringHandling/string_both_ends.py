
#########################################################################
# Author: Bhavya Bojanapalli
# This function returns the first 2 and the last 2 chars from a given a string. If the string length is less than 2 it should return empty string
#########################################################################

def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]


def main():
    print(string_both_ends('bhavyaabhi'))
    print(string_both_ends('abhi'))
    print(string_both_ends('b'))
    
main()
