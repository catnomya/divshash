import divshash as div

# Divshash

'''
This is a program which runs on the divshash algorithm, which has remarkable speed due to minimal modules
This program dosent require any external modules.

The program is secure and can only be dehashed using the hashing algorithm

All functions should work as intended and shouldnt require any module updates

Quick note, the hashing algorithm dosent support symbols, which will be outlined later.
'''

print(div.HashString('Hello World')) # Hashes basic strings using the hashing algorithm
# Output: 10111010101110.1111010100010000100011001_Y.jOOq%G.qsOX 

print(div.DehashString('10111010101110.1111010100010000100011001_Y.jOOq%G.qsOX ')) # DEHASHING THE HASH RETURNED FROM THE EARLIER.
# Output: Hello World

'''
These are the two functions on which the entire program runs.
'''

div.WriteHashToFile('Hello World', 'tutorial.txt')

'''
This function is the same as the HashString function,
except, it stores the output in a text file.

The function works on write mode,
meaning, if the file dosent exist, it creates the file,
and if it does exist, it erases all contents of the file and overrides it.


'''

print(div.HashWithFile('message.txt'))
'''
This function is also the same as the HashString function,
except, this time, it takes input from the text file and returns it as a string
'''

print(div.DehashWithFile('tutorial.txt'))
'''
This function is like the HashWithFile function, except, this time it dehashed a hashed string.
'''

#######################################################################

# Encryption and Decryption
'''
We can use these hashes to encrypt and decrypt files,
And, the divshash module contains built in functions to encrypt and decrypt these files


REALLY IMPORTANT NOTE: If the file is encrypted and then decrypted again, it will not contain any symbols
as, the algorithm dosent have any support for symbols.
'''

# TO ENCRYPT FILES, WE USE THE EncryptFile FUNCTION
# SYNTAX: div.EncryptFile('directory', pin (integer) )

'''
This function rewrites the entire file with the hash, making it completely unreadable, and it cant be opened again without the pin.
'''

# To now decrypt this file, we need the key, and the directory of the file, where:
# SYNTAX: div.DecryptFile('directory', pin(integer) )

# If the pin is incorrect, it will not return anything nor will it change the file state.
# The function will immidiately close if it dosent match the pin.


#######################################################################

