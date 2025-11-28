A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
#Join A and B
C = A.union(B)
print(C)

#Find A intersection B
print(A.intersection(B))

#Is A subset of B
print(A.issubset(B))
print(B.issubset(A))

#Join A with B and B with A
print(A.union(B))
print(B.union(A))

#What is the symmetric difference between A and B
print(A.symmetric_difference(B))

#Delete the sets completely
del A
del B
