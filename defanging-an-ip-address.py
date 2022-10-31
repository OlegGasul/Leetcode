def defangIPaddr(address: str) -> str:
    return '[.]'.join(address.split('.'))

print(defangIPaddr("1.1.1.1"))
print(defangIPaddr("255.100.50.0"))