import mlab
from service import Service

mlab.connect()

# #create 

# new_service = Service(
#     name  = " Cuong ",
#     yob = 1996,
#     gender = 1,
#     height = 168,
#     phone = "01234567890",
#     # occupied = False
   
# )

# new_service.save() # luu len collection



## read lay ra het tat ca 

# services = Service.objects()  # objects cha ve kieu du lieu la list  []
# print(services)
 
# for service in services :
#     print(`service.name)
#     print(service.yob)
#     print("--------------")


## read theo dieu kien

# services = Service.objects(gender = 0)
# print(services)

# for service in services :
#     print(service.gender)
    
#     print("--------------")

# services = Service.objects(height__lte = 164) #lte la nho hon
# print(services)

# for service in services :
#     print(service.height)
    
#     print("--------------")


# service = Service.objects.with_id("5bf0e5d9bd42b11794fd6de8")
# print(service)



## UPDATE

service = Service.objects.with_id("5bf0e5d9bd42b11794fd6de8")
# print(service.name)
# print(service.gender)
# print(service.phone)
# print(service.yob)
# print("------------------")


# service.update(set__name = "KIRA")

## DELETE

service.delete()