from pymongo import MongoClient
#from pprint import pprint
from faker import Faker 
import time
import json				 
from random import randint	 # For student id 
fake = Faker() 

def connect_db():
    client = MongoClient("18.139.1.63", 27019)
    return client

client = connect_db()
db = client.ms_dataset
print (db)
# password='$2b$10$VtHbWj8WssH3tGhGsC8HvOAbzRIlWtBPqu5Y3mjmzJKzbflqYhsKO'

#serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)
def input_data(x): 

	 
	user_data =[]
	for i in range(0, x): 
		temp={}  
		temp['width']=1024
		temp['height']=1027
		# temp['name']= fake.name()
		# temp['role']='admin' 
		# temp['email']=fake.email()
		# temp['password']=password
		# temp['phone']=fake.random_int(9000000000,9999999999) 
		# temp['created-at']=time.now()
		# temp['updated-at']=time.now()

		temp['is_active']='true'
		temp['image_url']=str(fake.image_url())
		user_data.append(temp) 
	#print(user_data) 
	result=db.images.insert_many(user_data)
	print(result)
	

	# dictionary dumped as json in a json file 
	# with open('students.json', 'w') as fp: 
	# 	json.dump(user_data, fp) 
	
	
def main() :
	# Enter number of students 
	# number_of_users = 10 # For the above task make this 100 
	input_data(10) 

main()

# # The folder or location where this python code 
# # is save there a students.json will be created 
# # having 10 students data. 

