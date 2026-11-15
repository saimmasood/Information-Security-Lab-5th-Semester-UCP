

s=[0,1,2,3,4,5,6,7,8]
key=[4,7,2]
t=[]

plainText=[1,2,8,10,45]

for i in range(0,len(s)):
    t.append(key[i%len(key)])


print("S array:",s)
print("T arraay with repeating key values:",t)


# permutations 
j=0
for i in range(0,len(s)):
    j=(j+s[i]+t[i])%len(s)
    temp =s[i]
    s[i]=s[j]
    s[j]=temp

print("S array after initial permutations:",s)

kStream=[]
j=0
i=0
for x in range (0,len(plainText)):
    i=(i+1)%len(s)
    j=(j+s[i])%len(s)
    temp =s[i]
    s[i]=s[j]
    s[j]=temp
    kStream.append(s[(s[i]+s[j])%len(s)])


print("S array after creating keyStream:",s)
print("Key Stream:",kStream)

cipherText=[]
for i in range(0,len(plainText)):
    cipherText.append(plainText[i]^kStream[i])

print()
print("Plain Text:",plainText)
print("Final cipher text:",cipherText)

    


