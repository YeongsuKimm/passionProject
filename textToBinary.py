#dec to bin
def decToBin(dec):
    binary = "";
    while(dec != 0):
        binary = str(dec%2) + binary;
        dec = int(dec/2);
    return binary;

#bin to dec
def binToDec(bin):
    dec = 0;
    bin = str(bin);
    for i in range(len(bin)):
        dec += int(bin[i])*(2**(len(bin)-1-i));
    return dec;

txt = input("Enter a sentence here: ");

lst = [];

for i in range(len(txt)):
    lst.append(ord(txt[i]));

binLst = [];

for i in lst:
    binLst.append(int(decToBin(int(i))))
    
print(binLst)

for i in binLst:
    print(chr(binToDec(i)), end="");
print()

print(lst)