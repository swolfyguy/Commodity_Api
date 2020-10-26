# Project 
Commodity_Api

# Tech Stack
1. Django
2. Sqlite


# Dependencies injection
pip install -r requirements.txt

# Execution steps 
1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py createsuperuser
   create super user for authentication for accessing login 
4. python manage.py runserver



baseurl = http://127.0.0.1:8000
basic_auth = username and password 

#################################################################################
# Elements API  
GET
baseurl/elements/<element_id>

POST
baseurl/elements
payload = {"name":"element_name"}

###########################################################################
# Commodity API
GET
baseurl/commodities/{commodity_id}

POST
baseurl/commodities
payload = {"name": "commodity_name", "inventory": inventery_value,"price": price,}
       

PATCH 
baseurl/commodities
payload = {"name": "commodity_name", "inventory": inventery_value,"price": price,}

###########################################################################
# Composition API 
POST
baseurl/compositions
payload = { "element_id":element_id,"percentage":percentage,"commodity_id":commodity_id}
 
# Note: 
1. element_id and commodity_id cannot be empty and should be exist in Element and Commodity Table
2. percentage cannot be more than 100%

# RESPONSE for commodity APi as per the Requirements 
{
    "name": "update_salt",
    "inventory": 10000,
    "price": 100,
    "chemical_composition": [
        {
            "percentage": 25,
            "element": {
                "id": 6,
                "name": "Sulphur"
            }
        },
        {
            "percentage": 25,
            "element": {
                "id": 10,
                "name": "Si"
            }
        },
        {
            "percentage": 8,
            "element": {
                "id": 11,
                "name": "unknown"
            }
        },
        {
            "percentage": 32,
            "element": {
                "id": 12,
                "name": "H20"
            }
        },
        {
            "element": {
                "id": 0,
                "name": "unknown_element"
            },
            "percentage": 10
        }
    ]
}
