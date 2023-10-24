from sha256 import get_sha256_hash

attempts = 0

while True:
    try:
        file = input("Enter file name: ")
        with open(file,"rb") as data:
            hash = get_sha256_hash(data.read().decode("LATIN-1"))
    except FileNotFoundError:
        print(f'Sorry "{file}" doesn\'t exist! Please try again: \n')
    else:
        print(hash)
        break
    finally:
        attempts += 1
        if attempts == 3:
            print("Wrong file name entered three times!\nPlease check the file name and try again.")
            break


#Use imported hashlib module to test the above program
import hashlib

with open(file,"rb") as f:
    bytes = f.read()
    readable_hash = hashlib.sha256(bytes).hexdigest()
    print(readable_hash)