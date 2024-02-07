import numpy as np
a = np.array([-3,-2,-1,0,1,254,255,256,257,258],dtype=np.uint8)
print(a)

#np.clip(a,p,q)
# a < p => p
# a > q => q

b = [-3,-2,-1,0,1,254,255,256,257,258]
print(b)
b = np.clip(b, 0, 255) #음수 뒤로 넘겨서 정리해버림
print(b)