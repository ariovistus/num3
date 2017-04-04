import functools

a = [44, 55, 35, 84, 34, 38, 34, 9832, 92, 1028]

sol = []

stage1 = []

for n in a:
    if n % 3 == 0:
        sol.append(n)
    else:
        stage1.append(n)

def str_cmp(s1, s2):
    # im sure there's something somewhere that does this, just can't find it atm
    if s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    else:
        return 0


def nlen(n):
    assert n > 0
    return len(str(n))

def p_ord(n1, n2):
    s1 = str(n1)
    s2 = str(n2)
    if len(s1) > len(s2) and s1.startswith(s2):
        return 1 # s2 should come first
    elif len(s2) > len(s1) and s2.startswith(s1):
        return -1 # s1 should come first
    return str_cmp(s2, s1) # whichever starts larger should come first

def stage2_sort(items):
    p_ord_key = functools.cmp_to_key(p_ord)
    temp = [(nlen(x), p_ord_key(x), x) for x in items]
    return [x for (n, p, x) in sorted(temp, key=lambda npx: (-npx[0], npx[1]))]

### testing time ###

assert nlen(1) == 1
assert nlen(11) == 2
assert nlen(1000) == 4

assert p_ord(10, 9) == 1
assert p_ord(9, 90) == -1
assert p_ord(90, 9) == 1
assert p_ord(9, 10) == -1
assert p_ord(9, 1) == -1


data = [
    {'input': [98, 9], 'result': [9, 98]},
    {'input': [9, 98], 'result': [9, 98]},
    {'input': [9, 8], 'result': [9, 8]},
    {'input': [99, 9, 999], 'result': [9, 99, 999]},
    {'input': [98, 9, 999], 'result': [9, 999, 98]},
    {'input': [10, 9, 999], 'result': [9, 999, 10]},
]

for datum in data:
    test1 = datum['input']

    result1 = sorted(test1, key=functools.cmp_to_key(p_ord))

    assert result1 == datum['result'], "expected %s, got %s" % (datum['result'], result1)


data = [
    {'input': [98, 9], 'result': [98, 9]},
    {'input': [8, 9], 'result': [9, 8]},
    {'input': [10, 9], 'result': [10, 9]},
]

for datum in data:
    test1 = datum['input']

    result1 = stage2_sort(test1)

    assert result1 == datum['result'], "expected %s, got %s" % (datum['result'], result1)

### k think it works ###

stage2 = stage2_sort(stage1)

while len(stage2) >= 4:
    """
    these are the possible cases of the next 4 numbers modulo 3:
    1 1 1
    1 1 2 1 # skip third
    1 1 2 2
    1 2
    2 1
    2 2 1 1
    2 2 1 2 # skip third
    2 2 2
    """
    n1 = stage2[0]
    if sum(stage2[0:2]) % 3 == 0:
        sol.append(stage2.pop(1))
        sol.append(stage2.pop(0))
    elif sum(stage2[0:3]) % 3 == 0:
        sol.append(stage2.pop(2))
        sol.append(stage2.pop(1))
        sol.append(stage2.pop(0))
    elif sum(stage2[0:4]) % 3 == 0:
        sol.append(stage2.pop(3))
        sol.append(stage2.pop(2))
        sol.append(stage2.pop(1))
        sol.append(stage2.pop(0))
    else:
        sol.append(stage2.pop(3))

        sol.append(stage2.pop(1))
        sol.append(stage2.pop(0))


"""
3 numbers or less left, possibilities are:

(empty)# done!
1      # skip all
2      # skip all
1 1    # skip all
1 2    # take all
2 1    # take all
2 2    # skip all
1 1 1  # take all
1 1 2  # skip second
1 2 1  # skip third
1 2 2  # skip third
2 1 1  # skip third
2 1 2  # skip third
2 2 1  # skip second
2 2 2  # take all

"""
if sum(stage2) % 3 == 0:
    sol.extend(stage2)
elif len(stage2) == 3 and sum(stage2[0:2]) % 3 == 0:
    sol.extend(stage2[0:2])
elif len(stage2) == 3 and (stage2[0] + stage2[2]) % 3 == 0:
    sol.append(stage2[0])
    sol.append(stage2[2])
    

sol.sort(key=functools.cmp_to_key(p_ord))

print(sol)
print ("".join([str(x) for x in sol]))
