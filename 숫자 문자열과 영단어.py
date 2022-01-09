def solution(s):
    mylist = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in mylist:
        if(s.find(i) != -1):
            s = s.replace(i, str(mylist.index(i)))
    return int(s)