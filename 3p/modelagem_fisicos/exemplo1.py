#código não otimizado: some dados de 0 - 10_000_000
# import time

# start = time.time()
# a = 0

# for i in range(0,10_000_000+1):
#     a += i
    
# print('valor: ' + str(a))
# print(f"Levou: {time.time()-start} s")

# valor: 50000005000000.0
# Levou: 0.6052708625793457s

#código otimizado: some dados de 0 - 10_000_000

import time

start = time.time()

primeiro = 1
ultimo = 10_000_000

sn = (ultimo/2) * (primeiro + ultimo)

print('valor: ' + str(sn))
print(f"levou: {time.time()-start} s")

# valor: 50000005000000.0
# levou: 3.1948089599609375e-05s

