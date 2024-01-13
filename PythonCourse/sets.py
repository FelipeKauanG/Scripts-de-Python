#set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}
#utensils.add("napkin")
#utensils.remove("fork")
#dishes.update(utensils)
#dinner_table = utensils.union(dishes)

#for x in dishes:
#    print(x)
#print(dishes.difference(utensils))
print(utensils.intersection(dishes))
