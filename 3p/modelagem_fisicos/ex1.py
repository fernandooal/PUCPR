import time

start = time.time()

print('x' * 100_000_000)

end = time.time()
print(end-start)