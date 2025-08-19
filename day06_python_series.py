c='iraj'
d="hello {} iraj bom {}"
e="hello {1} iraj bom {0}"

# print(len(c))
# print(max(c))
# print(min(c))
# print(sorted(c))
# print(sorted(c,reverse=True))

# print(c.capitalize())
# print(c.title())
# print(c.lower())
# print(c.upper())
# print(c.swapcase())
print(c.count('a'))
# use find bcs if any string is not present it will return -1 but index will crash the code 
print(c.find('k'))
print(c.index('i'))
print(c.endswith('j'))
print(c.startswith('i'))
print(d.format('world','dia'))
print(e.format('world','dia'))
print(e.split())
print(" ".join(['iraj','iraj']))
print(c.replace('a','e'))
print(c.strip())
