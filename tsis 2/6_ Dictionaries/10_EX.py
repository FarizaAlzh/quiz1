# EX 1 
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

# EX 2 
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"]= 2020
print(car)

# EX 3 
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

# EX 4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)
# EX 5 
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()