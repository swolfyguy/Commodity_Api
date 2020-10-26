# Commodity_Api

Used Tech Stack

1. Django
2. Sqlite


# Installation steps 

pip install -r requirements.txt

# Running steps 

1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py createsuperuser
   create super user for authentication for accessing login 
4. python manage.py runserver



baseurl = http://127.0.0.1:8000
basic_auth = username and password 

# Elements API CRUD operation 

GET - baseurl/elements/Element_Id
Post - baseurl/elements
       body = {"name":"element_name"}

# Commodity API CRUD operation 

    get commodity details
1. GET- baseurl/commodities/{commodity_id}

    create commodity
2. POST - baseurl/commodities
       body ={"name": "commodity_name", "inventory": inventery_value,"price": price,}
       
    update commodities
3. Patch -baseurl/commodities
       body ={"name": "commodity_name", "inventory": inventery_value,"price": price,}

# Composition API CRUD operation

Add element to commodity with commodity 
1. POST - baseurl/compositions
          body ={ "element_id":element_id,"percentage":percentage,"commodity_id":commodity_id}
 
# Note: 
1. element_id and commodity_id cannot be empty and should be present in Element and commodity Table
2. percentage cannot be more than 100%

# EXAMPLE for commodity APi as per the Requirements 
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
