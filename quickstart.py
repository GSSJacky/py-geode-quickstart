from org.apache.geode import *
import os
from Customer import *


def test_get_region(self):
    regionObject = self.create_repository("Customer")
    print(regionObject)

def test_put(self):
    
    self.myRegion = self.create_repository("Customer").get_region()
    for x in range(1000):      
        name1 = "name" + str(x)
        id1 = x
        tel1="09065110111"
        email1="xxx@abc.com"
        c1 = Customer(id1,name1,tel1,email1)
        self.myRegion.put(x, c1)
    
def list_all_regions(self):
    allregions = self.list_all_regions()
    print(allregions)

def test_adhoc_query(self):
    result = self.adhoc_query("SELECT * FROM /Customer")
    print(result)

def test_delete(self):
    key=379
    self.myRegion = self.create_repository("Customer").get_region()
    deleteresult=self.myRegion.delete(key)
    if deleteresult == True :
        print("Deleted specified entry:." + str(key))    

def test_clearAll(self):
    self.myRegion = self.create_repository("Customer").get_region()
    clearall = self.myRegion.clear()
    if clearall == True :
        print("Cleared region's all entries.")


client = GeodeClient(hostname="localhost", port=7060, user="", password="", debug_mode=True)
#test_get_region(client)
list_all_regions(client)
test_put(client)
test_delete(client)
test_clearAll(client)
test_adhoc_query(client)

