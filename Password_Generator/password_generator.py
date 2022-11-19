import random
import string

# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ  string.ascii_letters
# 0123456789                                            string.digits
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~                      string.punctuation

total = string.ascii_letters + string.digits + string.punctuation
length = int(input("Enter lenght password: "))
password = "".join(random.sample(total, length))
print(password)
