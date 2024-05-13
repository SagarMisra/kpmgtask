key1=input("Enter key: \n")
# key1 = "a/b/c"
keys=key1.split('/')
obj=input("Enter object: \n")
obj=eval(obj)
# obj = {"a": {"b": {"c": "d"}}}
print (keys)
for k in keys:
  if k in obj:
    obj = obj[k]

print(obj)    

