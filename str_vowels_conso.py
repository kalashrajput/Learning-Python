#WAP to find number of vowels and consonents in a string.
str=input("Enter a string - ");
vowel=0;
consonent=0;
for i in range(0,len(str)):
    if(str[i]!=""):
        if(str[i]=="a" or str[i]=="e" or str[i]=="i" or str[i]=="o" or str[i]=="u" or str[i]=="A" or str[i]=="E" or str[i]=="I" or str[i]=="O" or str[i]=="U"):
            vowel=vowel+1
        else:
            consonent=consonent+1;
print("Total Vowels are - ",vowel);
print("Total Consonent are - ",consonent);