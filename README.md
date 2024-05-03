# Vendor Management System with Performance Metrics

Develop a Vendor Management System using Django and Django REST Framework. This
system will handle vendor profiles, track purchase orders, and calculate vendor performance
metrics.

## Installation

### Requirements
- Python
- Django
- Django rest Framework

  Complete list available in requirements.txt file

### Quickstart
- Clone the repo.  
    ```bash
    git clone https://github.com/shaweta/Vendor-Mangement-System.git
    ```

- Inside the backend folder, make a virtual environment and activate it 
    ```bash
    cd vendor_management
    python -m venv env 
    source env/bin/activate(./env/Scripts/activate)

    ```

- Install requirements from requirements.txt
    ```
    pip install -r requirements.txt
    ```

- Makemigrations and migrate the project
    ```
    python manage.py makemigrations && python manage.py migrate
    ```

- Create a superuser
    ```
    python manage.py createsuperuser
    ```

- Runserver
    ```
    python manage.py runserver
    ```

**Note: After running the server, you can use the api inside browser or you can use Postman to make api calls. Make sure in each api call, you provide username, password by creating a user
Here  token authentication is applied so when testing with postman or thunder client in VSCode make sure to pass token in the header while making calls.
.**



While working with api in browser, you can login using `http://127.0.0.1:8000/api/` link.


## API
<details>
<summary> Vendor model </summary> 

- Vendor:
    - name: string(unique),
    - contact_details: text,
    - address: text
    - vendor_code:charfield

</details>

<details>
<summary> PurchaseOrder Model </summary>


</details>

<details>
<summary>HistoricalPerformance </summary>

</details>



### Endpoints

Brief explanation of endpoints:

| Function                                                                                               | REQUEST    | Endpoint                                                | Authorization | form-data                                 |
|--------------------------------------------------------------------------------------------------------|------------|---------------------------------------------------------|---------------|-------------------------------------------|
| Create new Vendor                                                                                      | POST       | http://127.0.0.1:8000/api/vendors/                      | Token Auth    | username, email, password pass token in header                   |
| Returns list of all existing Vendors                                                                   | GET        |  http://127.0.0.1:8000/api/vendors/                     | Token Auth    |                                           |
| Returns the detail of an Vendor instance                                                               | GET        | http://127.0.0.1:8000/api/vendors/{int:id}/             | Token Auth    |                                           |
| Update the detail of an Vendor instance                                                                | PUT, PATCH | http://127.0.0.1:8000/api/vendors/{int:id}/             | Token Auth   |                                           |
| Delete an Vendor instance                                                                              | DELETE     | http://127.0.0.1:8000/api/vendors/{int:id}/             | Token Auth    |                                           |
|                                                                                                        |            |                                                         |               |                                           |
| Returns a list of all existing Purchase orders                                                         | GET        | http://127.0.0.1:8000/api/purchase_orders/              | Token Auth  |                                           |
| Creates a new Purchase orders . Returns created Purchase orders  data                                  | POST       | http://127.0.0.1:8000/api/purchase_orders/              | Token Auth   |  |
| Returns the details of a Purchase orders instance.                                                     | GET        | http://127.0.0.1:8000/api/purchase_orders/{int:id}/     | Token Auth    |                                           |
| Updates an existing Purchase orders . Returns updated Purchase orders                                  | PUT, PATCH | http://127.0.0.1:8000/api/purchase_orders/{int:id}/     | Token Auth   |  |
| Deletes the existing Purchase orders                                                                   | DELETE     | http://127.0.0.1:8000/api/purchase_orders/{int:id}/     | Token Auth    |                                           |
| Update Acknowledement  in purchase orders                                                              | POST       | http://127.0.0.1:8000/api/purchase_orders/{int:id}/acknowledge/| Token Auth |                                           |
| Vendor Performance                                                                                     | GET        | http://127.0.0.1:8000/api/vendors/{int:id}/performance   |Token Auth    |                        |
| 

You can use  VSCode thunder client or postman to interact with the apis and to get access of apiyou need to give Token in Header 


