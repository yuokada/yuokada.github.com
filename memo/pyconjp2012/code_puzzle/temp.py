#!/usr/bin/env python2.7
def lets_take_tea_break(m, e, n, c):
    #if pow(m, e) % n == c: return str(m)
    if pow(m, e) % n == c: return str(m)
    return ""

for j in range(1,1000000000):
    print(lets_take_tea_break(*[int(i) for i in (j, 17, 3569, 915)]))



if __name__ == "__main__":
    import sys
    #print("http://cp1.nintendo.co.jp/" + lets_take_tea_break(*[int(i) for i in (sys.argv[1], 17, 3569, 915)]))
