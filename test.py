def intersection(a, b):
    s1 = set(a)
    s2 = set(b)
    return s1.intersection(s2)

if __name__ == "__main__":
    # Create two lists of your choice.
    a = [10, 12, 31, 44, 56]
    b = [16, 71, 98, 91, 101]
    s3 = intersection(a, b)

    if len(s3) > 0:
        print("True")
    else:
        print("False")
