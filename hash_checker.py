import hashlib
import sys
from os.path import exists

def validate_input():
    isValid = True
    if not hash_alg in hashlib.algorithms_available:
        print("That hash algorithm is not available. Pick one of these available hash algorthms:")
        print(hashlib.algorithms_available)
        isValid = False
    elif len(checksum) < 1:
        print("Please enter a checksum to compare.")
    elif not exists(inpt_file):
        print("The file doesn't exist. Check the entered path.")
        isValid = False
    
    return isValid


valid = False

while not valid:
    hash_alg = input("Enter the hash algorithm to use (or q to quit): ")
    if hash_alg == 'q':
        sys.exit()
    
    checksum = input("Enter the checksum to compare (or q to quit): ")
    if checksum == 'q':
        sys.exit()
    
    inpt_file = input("Enter the file path (or q to quit): ")
    if inpt_file == 'q':
        sys.exit()
    
    valid = validate_input()

with open (inpt_file, 'rb') as file:
    hasher = hashlib.md5()
    buff = file.read()
    hasher.update(buff)
    hash_value = hasher.hexdigest()
    
    if checksum == hash_value:
        print("The hashes match.")
    else:
        print("The hashes don't match. File integrity may be compromised.")
    
    print('Checksum: {}'.format(checksum))
    print("File hash: {}".format(hash_value))
    
    
    


