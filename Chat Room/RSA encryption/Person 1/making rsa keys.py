#####
#Run This program to make a public and private keys
#####
import rsa

public_key,private_key = rsa.newkeys(1024)

with open('publicKey_of_Person1.pem', 'wb') as f:
    f.write(public_key.save_pkcs1('PEM'))

with open('privateKey_of_Person1.pem', 'wb') as f:
    f.write(private_key.save_pkcs1('PEM'))