#Default FUnctions
def inverse_pow(p,q):
   return round(p ** (1/q))

print(inverse_pow(64, 2))  # 8
print(inverse_pow(1221, 3))  # 11
print(inverse_pow(4294967296, 32))  # 2