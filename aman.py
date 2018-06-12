def mutate_string(string, position, character):
    l=[]
    l=list(string)
    l[position]=character
    str=str(l)
    print(str)
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)