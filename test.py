import enum
# Using enum class create enumerations
class Days(enum.Enum):
   Sun = 1
   Mon = 2
   Tue = 3
# printing all enum members using loop
day = Days.Mon
day = Days(day.value +1) 

print(day)