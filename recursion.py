#exercise 1

def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n-1)
    
#exercise 2

def list_sum(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + list_sum(l[1:])
    
#exercise 3

def bunny_ears(n):
    if n == 0:
        return 0
    else:
        return 2 + bunny_ears(n-1)

#exercise 4

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

#exercise 5

def get_max(l):
    if len(l) == 0:
        return 0
    else:
        return max(l[0], get_max(l[1:]))

print(get_max([11, 22, 3, 41, 15]))
