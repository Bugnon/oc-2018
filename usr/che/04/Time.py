import time

t=time.time()

secs=int(t)
sec=secs%60
mins=secs//60

print(t)
print(secs, sec, mins)