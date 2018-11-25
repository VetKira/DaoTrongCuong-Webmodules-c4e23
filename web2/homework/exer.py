import mlab1
from river import River

mlab1.connect()

# exer2

list_africa = River.objects(continent = "Africa")
print(list_africa.name)



# exer3

list_american = River.objects(continent = "S.America", length_lte = 1000)
print(list_american.name)