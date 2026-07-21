s = "abaaab"



print(s.count("ab"))

def sub_string(string, sub_string):
    start = 0
    count = 0

    while start < len(string):

        start = string.find(sub_string, start)
        if start == -1:
            break
        start += 1
        count += 1
    return count
print(sub_string(s,"aa"))