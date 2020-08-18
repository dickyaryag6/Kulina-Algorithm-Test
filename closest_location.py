import math

class Supplier:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude


class Customer:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude    
    
# -----------------------------------------------------------------------------------

# FUNCTION TO FIND DISTANCE USING GREAT DISTANCE CIRCLE FORMULA
def distance(customer_latitude, customer_longitude, supplier_latitude, supplier_longitude):
    customer_latitude = degree_to_radian(customer_latitude)
    customer_longitude = degree_to_radian(customer_longitude)

    supplier_latitude = degree_to_radian(supplier_longitude)
    supplier_longitude = degree_to_radian(supplier_longitude)

    central_angle = math.acos(math.sin(customer_latitude)) * math.sin(supplier_latitude) + math.cos(customer_latitude) * math.cos(supplier_latitude) * math.cos(supplier_longitude-customer_longitude)

    return (earth_radius * central_angle)


def degree_to_radian(degree):
    return (degree * math.pi / 180.0)


# FUNCTION TO ASSIGN ORDER TO CLOSEST SUPPLIER
def assign_order(customer, list_of_suppliers):
    list_of_suppliers_distances = []
    for supplier in list_of_suppliers:
        list_of_suppliers_distances.append([supplier, distance(customer.latitude, customer.longitude, supplier.latitude, supplier.longitude)])

    # SORT TO GET CLOSEST SUPPLIER
    list_of_suppliers_distances = sorted(list_of_suppliers_distances,key=lambda l:l[1])
    closest_supplier = list_of_suppliers_distances[0][0]
    
    # RETURN SUPPLIER OBJECT
    return closest_supplier


# --------------------------------------------------------------

earth_radius = 6371.0

supplier_A = Supplier("Supplier A", 12.986375, 77.043701)
supplier_B = Supplier("Supplier B", 55.033, 78.27699)
supplier_C = Supplier("Supplier C", 11.8856167, 71.4240911)

list_of_suppliers = [
    supplier_A, #SUPPLIER 1
    supplier_B, #SUPPLIER 2
    supplier_C #SUPPLIER 3
]

customer_A = Customer("Customer A", 12.9611159, 77.6362214)

# ASSIGN ORDER TO CLOSEST SUPPLIER
print(assign_order(customer_A, list_of_suppliers))



