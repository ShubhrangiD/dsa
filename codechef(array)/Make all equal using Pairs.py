# Make all equal using Pairs
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    freq={}
    for k in a:
        freq[k]=freq.get(k,0)+1
    max_freq=max(freq.values())
    print(len(a)-max_freq)
