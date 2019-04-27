#%%
from z3 import *
lisa = Bool('lisa') #tiger is in rm1
jim = Bool('jim')
bob = Bool('Bob')
mary = Bool('mary')

lisa1 = Bool('lisa1') #lisa is rank of 1
jim1 = Bool('jim1')
bob1 = Bool('Bob1')
mary1 = Bool('mary1')
lisa2 = Bool('lisa2') #lisa is rank of 2
jim2 = Bool('jim2')
bob2 = Bool('Bob2')
mary2 = Bool('mary2')
lisa3 = Bool('lisa3') #lisa is rank of 3
jim3 = Bool('jim3')
bob3 = Bool('Bob3')
mary3 = Bool('mary3')
lisa4 = Bool('lisa4') #lisa is rank of 4
jim4 = Bool('jim4')
bob4 = Bool('Bob4')
mary4 = Bool('mary4')

#each person can only occur one rank
rl1 = And(Implies(lisa1, Not(Or(lisa2, lisa3, lisa4))), Implies(lisa2, Not(Or(lisa1, lisa3, lisa4))), Implies(lisa3, Not(Or(lisa2, lisa1, lisa4))), Implies(lisa4, Not(Or(lisa2, lisa3, lisa1))))
rl2 = And(Implies(jim1, Not(Or(jim2, jim3, jim4))), Implies(jim2, Not(Or(jim1, jim3, jim4))), Implies(jim3, Not(Or(jim2, jim1, jim4))), Implies(jim4, Not(Or(jim2, jim3, jim1))))
rl3 = And(Implies(bob1, Not(Or(bob2, bob3, bob4))), Implies(bob2, Not(Or(bob1, bob3, bob4))), Implies(bob3, Not(Or(bob2, bob1, bob4))), Implies(bob4, Not(Or(bob2, bob3, bob1))))
rl4 = And(Implies(mary1, Not(Or(mary2, mary3, mary4))), Implies(mary2, Not(Or(mary1, mary3, mary4))), Implies(mary3, Not(Or(mary2, mary1, mary4))), Implies(mary4, Not(Or(mary2, mary3, mary1))))

#each rank can only occur one person
rl5 = And(Implies(lisa1, Not(Or(jim1, bob1, mary1))), Implies(jim1, Not(Or(lisa1, bob1, mary1))), Implies(bob1, Not(Or(lisa1, jim1, mary1))), Implies(mary1, Not(Or(lisa1, jim1, bob1))))
rl6 = And(Implies(lisa2, Not(Or(jim2, bob2, mary2))), Implies(jim2, Not(Or(lisa2, bob2, mary2))), Implies(bob2, Not(Or(lisa2, jim2, mary2))), Implies(mary2, Not(Or(lisa2, jim2, bob2))))
rl7 = And(Implies(lisa3, Not(Or(jim3, bob3, mary3))), Implies(jim3, Not(Or(lisa3, bob3, mary3))), Implies(bob3, Not(Or(lisa3, jim3, mary3))), Implies(mary3, Not(Or(lisa3, jim3, bob3))))
rl8 = And(Implies(lisa4, Not(Or(jim4, bob4, mary4))), Implies(jim4, Not(Or(lisa4, bob4, mary4))), Implies(bob4, Not(Or(lisa4, jim4, mary4))), Implies(mary4, Not(Or(lisa4, jim4, bob4))))

f1 = Not(Or(And(lisa1, bob2), And(lisa2, bob3), And(lisa3, bob4), And(bob1, lisa2), And(bob2, lisa3), And(bob3, lisa4)))
f2 = Or(And(jim1, Xor(lisa2, mary2)), And(jim2, Xor(lisa3, mary3)), And(jim3, Xor(lisa4, mary4)))
f3 = Or(And(bob1, jim2), And(bob2, jim3), And(bob3, jim4))
#f4 is consider in f2
f5 = Xor(lisa1, mary1)
s = Solver()
s.add(rl1, rl2, rl3, rl4, rl5, rl6, rl7, rl8, f1, f2, f3, f5)
print(s.check())
print(s.model())
#mary = 1
#bob = 2
#jim = 3
#lisa = 4

#or

#mary = 4
#bob = 2
#jim = 3
#lisa = 1
