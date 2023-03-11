import hashlib
import time 
def f():
    t1=time.time()
    time.sleep(1)
    t2=time.time()
    res = str(t2-t1)
    return res[res.find('.')+4:]
# text = 'Hello!'
seed1 = f()
seed2 = f()
print(seed1)
print(seed2)
# m = hashlib.sha256(text.encode('UTF-8'))
# print(m.hexdigest())
u = hashlib.sha256(seed1.encode('UTF-8'))
p = hashlib.sha256(seed2.encode('UTF-8'))
# print(u.hexdigest())
# print(p.hexdigest())
u = u.hexdigest()
p = p.hexdigest()

def g(seed,hash,length)->str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    x=int(seed[:2])
    x//=64
    def h():
        start=0
        for i in range(64):
            if alphabet.find(hash[i])>=0:
                start=i
                break
        if alphabet.find(hash[start])<0:
            print('something went wrong')
            return
        return (hash[start:start+length]) 
    if x>32:
        # for i in range(x,64):
        #     if alphabet.find(hash[i-length])>=0:
        #         x=i
        #         break
        # if alphabet.find(hash[x-length])==-1:
        #     print('something went wrong')
        #     return
        if alphabet.find(hash[x-length])>-1:
            return (hash[x-length:x])
        else:
            return h()
    else:
        # for i in range(0,x+1):
        #     if alphabet.find(hash[i])>=0:
        #         x=i
        #         break
        # if alphabet.find(hash[x])<0:
        #     print('something went wrong')
        #     return 
        if alphabet.find(hash[x])>=0:
            return (hash[x:x+length])
        else:
            return h()

u = g(seed1,u,20)
p = g(seed2,p,16)
if u==None or p==None:
    print('end')
else:
    if len(u)!=20 or len(p)!=16:
        print('length not very good')
    print(f'u={u}')
    print(f'p={p}')