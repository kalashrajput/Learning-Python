#Break statement in loop :
print("--- Break statement ---");
i=1;
while(i<=5):
    if(i==3):
        break
    print(i)
    i=i+1
#Continue statement in loop :
print("--- Continue statement ---");
i=0;
while(i<=5):
    i=i+1
    if(i==3):
        continue
    print(i)
