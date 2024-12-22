**Create a simple loyalty management system prototype for an eCommerce platform. The system should manage loyalty points for individual users and groups.**

**Steps to Set Up the Project**
1. Clone the Repository

    First, clone the Wagtail project repository from GitHub using the following command:
    ```
    git clone https://github.com/monjor-morshed/loyalty_manager.git
    cd loyalty_manager
   
   ```
2. Install Project Dependencies
```
pip install -r requirements.txt
```
3. Set Up the Database
```
python manage.py migrate

```
4. Create a Superuser
```
python manage.py createsuperuser

```
5. Run the Development Server
```
python manage.py runserver
```
6. Access Wagtail Admin Panel(Optional)
```
http://http://localhost:8000/django-admin/
```
