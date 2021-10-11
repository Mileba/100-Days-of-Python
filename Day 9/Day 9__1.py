programming_dict = {
    "bug":"An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you easily call over and over again.",
    }



#Adding new items to dictionary

programming_dict["Loop"] = "The action of doing something repeatedly"



#Edit an item in dict
programming_dict["bug"] = "a moth in computer"
#print(programming_dict)

for items in programming_dict:
    #print(items)
    #print(programming_dict[items])
    
#Nesting

capitals = {
    "France":"Paris",
    "Germany":"Berlin",
    }

#Nesting a List in a Dictionary

travel_log = {
    "France":{"cities_visited":["Paris","Lille","Dijon"],
              "total_visit":12},
    "Germany":["Berlin","Hamburg","Stuttgart"],
    }

country_log = [
    "France":{"cities_visited":["Paris","Lille","Dijon"],
              "total_visit":12},
    "Germany":["Berlin","Hamburg","Stuttgart"],
    ]



 