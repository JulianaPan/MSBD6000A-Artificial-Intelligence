#%%
from z3 import *
t1 = Bool('t1') #tiger is in rm1
t2 = Bool('t2')
t3 = Bool('t3')
l1 = Bool('l1') #lady is in rm1
l2 = Bool('l2')
l3 = Bool('l3')
s1 = t1
s2 = l2
s3 = t2
rm1 = Xor(l1, t1)
rm2 = Xor(l2, t2)
rm3 = Xor(l3, t3)
rl1 = Or(And(l1, t2, t3), And(t1, l2, t3), And(t1, t2, l3))
rl2 = Or(And(Not(s1), Not(s2), Not(s3)), And(s1, Not(s2), Not(s3)), And(Not(s1), s2, Not(s3)), And(Not(s1), Not(s2), s3))

# rl1 = Xor(l1, l2, l3)
# rl2 = Xor(And(Not(s1), Not(s2), Not(s3)), Xor(s1, s2, s3))

print(solve(rm1, rm2, rm3, rl1, rl2))
#l1 is correct
s = Solver()
total = And(rm1, rm2, rm3, rl1, rl2)
s.add(Implies(total, l1))
s.add(total)
s.add(not(total))
print(s.check())

#So the lady is in room1
