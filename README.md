# Simple Rest API to Create, Delete, Read and Delete Providers and its Polygons

#Instalation
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

1. set env variables
    * export DEBUG=1
    * export SECRET_KEY='some secrete'
    * export SECRET_KEY='db postgres url'

./manage.py migrate

Main url
/providers/
/polygons/
/polygons/given_coordinates_return_polygons/?lat=**x**&lng=**y**

With the last on you can fiter polygons given a latitude and longitude like this:
/polygons/given_coordinates_return_polygons/?lat=**125.6**&lng=**10.1**