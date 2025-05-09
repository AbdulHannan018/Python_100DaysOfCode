states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts",
                     "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina",
                     "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
                     "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa",
                     "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska",
                     "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
                     "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america[0])  # 1st item
print(states_of_america[-1])  # last item
print(states_of_america[len(states_of_america)-1])  # last item
print(states_of_america[0:5])  # upper limit not included | or | 0+5 = 5 -> 5 results produced | or | 5-0 = 5 results
print(len(states_of_america))
print(states_of_america[45:len(states_of_america)])  # 45th is actually 46th coz index starts from 0
print(states_of_america[44:len(states_of_america)])  # 44th is actually 45th coz index starts from 0
print(states_of_america[47:len(states_of_america)])  # 50 - 47 = 3 results

# Update item in a list
states_of_america[1] = "Pencilvania"
print(states_of_america[0:3])

# Adding an item to a list
states_of_america.append("Canada")
print(states_of_america[-1])

states_of_america.extend()
states_of_america.insert()
states_of_america.remove()
states_of_america.pop()
states_of_america.clear()
states_of_america.count()
states_of_america.sort()
states_of_america.reverse()
states_of_america.copy()
states_of_america.index()

