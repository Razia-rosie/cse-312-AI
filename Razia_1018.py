name=input("Enter full name: ") # MY NAME: RAZIA KHANOM
no_name=name.replace(" ","") # get rid of any spaces in the name

# Printing My name
print("Full Name: ",name)

# Vowel And Consonant Count
vowel="aeiouAEIOU"
vwl=0
con=0
for l in no_name:
    if l in vowel:
        vwl=vwl+1
    else:
        con=con+1
print(f"Vowels: {vwl}, Consonants: {con}")

# Asci Value Count
asci_value = []
for l in name:
    asci_value.append(ord(l))
print(f"ASCII Values : {asci_value}")

#Reverse Name
rev_name=""
for char in name:
    rev_name=char+rev_name
print(f"Reversed Name: {rev_name}")

#Cheking Pelindrom
if name==rev_name:
    print("Is Palindrom: True")
else:
    print("Is Palindrom: False")

# Unique Letters In My Name
unq_let=sorted(list(set(no_name))) #first stored in a set then convert it to a list then sort it
print(f"Unique Letters (sorted): {unq_let}")

# First Non Repeting letters
c=''
for l in no_name:
    if no_name.count(l)==1:
        c=l
        break
print(f"First Non-Repeating Character: {c}")