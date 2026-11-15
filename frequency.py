text = input("Enter plaintext: ")

text = text.upper()

frequency = {}

for char in text:
    if char.isalpha():
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

total = sum(frequency.values())

print("\nLetter Frequency")
print("----------------")

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

    count = frequency.get(letter, 0)

    if total > 0:
        percentage = (count / total) * 100
    else:
        percentage = 0

    print(letter, ":", count, "=", round(percentage, 2), "%")






















    plain_text=input("enter the plain text:")
    plain_text=plain_text.upper()


    frequency={}

    for char in plain_text:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1

    total=sum(frequency.values())

    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        count=frequency.get(letter,0)

        if total>0:
            percentage=(count/total)*100
        else:
            percentage=0

        print(letter," : ",count," = ",percentage,"%")