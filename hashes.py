import hashlib

data="VIT, AP"

hash_object=hashlib.md5(data.encode())  # Replace md5 with with other algo names like sha1 so that we can obtain hashes of various algos

#hexdigest is a method in python  programming to obtain
#a hexadecimal representation of the hash value

hash_hexdigest=hash_object.hexdigest()

print("Original Data: ",data)
print("sha-256 hash: ", hash_hexdigest)