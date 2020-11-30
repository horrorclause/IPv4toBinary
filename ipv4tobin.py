#!python3

"""Convert an IPv4 Address to Binary"""

ipAdd = input("What is the IP address?: ")
ipSplit = ipAdd.split('.')
binary = []
brokenDown = []

for i in range(len(ipSplit)):
    binary.append(str(bin(int(ipSplit[i]))[2:].zfill(8))) # Takes split octet, conv to int, conv to bin() removes "0b"
                                                          # and fills with 0 up to 8 spaces with .zfill(8)
    brokenDown.append(ipSplit[i] + ' : ' + binary[i])     # Adds orig Octet w/Binary conv to list for breakdown per octet
    #print(ipSplit[i], ' : ', binary[i])           # Uncomment to view loop values

joinedBinary = ''.join(binary) # Need to display preceding zeros when converted to int()

print("\nHere is your conversion:\n")
print("{} : {}".format(ipAdd, joinedBinary))
print('*-*-*-*-*-*-*-*-*')

for i in range(len(brokenDown)):
    print(brokenDown[i])
print('\n')
