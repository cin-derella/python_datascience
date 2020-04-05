#  Permutations:M!/(M-N)!   0! = 1
import itertools
mylist1 = list(itertools.permutations([1,2,3,4],3))
print(mylist1)

#  Combinations :M!/(M-N)! * N!   0! = 1
mylist2 = list(itertools.combinations([1,2,3,4],3))
print(mylist2)
