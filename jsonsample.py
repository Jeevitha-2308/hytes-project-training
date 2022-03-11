import json
a=open('shoes.txt','r',encoding="utf-8")
b=a.read()
a.close()

# Convert string to Python dict
python_obj = json.loads(b)
##we can access key-value pair but indent cannot be used
print(python_obj["properties"][ "CD4_DEMOGRAPHIC_DISPLAY_KEYS"])   
print(type(python_obj))
print("\n")

# Convert Python dict to JSON
json_object = json.dumps(python_obj,indent=4)
##we cannot access key-value pair from dumps
print(json_object) 
print(type(json_object))

