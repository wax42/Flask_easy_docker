import time

while (1):
   N = 500
   U = list(range(1,N*N))
   U[0] = 1
   U[1] = 1

   for i in range(2,N+1) :
      U[i] = U[i-1] + U[i-2]
      print(U[i])
      time.sleep(0.01)
   i = N
   while (i > 0):
       i -= 1
       print(U[i])
       time.sleep(0.01)
