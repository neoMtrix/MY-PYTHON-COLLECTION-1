# What if you wanted to know the index of an element while going through the list? You could use the range function and then use indexing to access the elements at the index that range returned. You could use a range function and then use indexing to access the elements at the index that range just returned or you could just use the enumerate function.

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))
