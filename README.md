# Tasks and Goals
Create a Django application implementing the following guidelines:
Create a custom user model extending the default Django user model.

### There should be some mandatory fields in the custom user model like:
- username
- user_type
- authentication_token

Django super admin can create a manager_type user manually.
There should be 2 types of users, `manager` and `customer` and the user type will be defined by "the user_type" flag
`authentication_token` should be an auto-generated field and when a user is created a 16-character auto-generated token should
be generated and saved to this field.

Write a Rest API in DRF(Django Rest Framework) which will CRUD(Create Retrieve Update Delete) user.
- Only manager type users can create, update, or delete user
- When a user is created through API then the auto-generated `authentication_token` should be the API response
- For any further request a user should use that authentication token as a request body
- Only customer type users can view the list of users  or details of a user
- To create a new user you have to provide "a username", "email" and "password" as requested body
- To get specific user details you have to provide a username at the end of the API like `127.0.0.1:8000/users/<username>`

### Write custom middleware to log details of  a request as below
- username (who called the API)
- date with time(when the API is called)
- use a separate model to keep this log instead of a file log

### Write a custom middleware to check user type
- user type should be checked using `authentication_token`
- Anonymous users cannot view any data or if they request any endpoint then handle it with proper response.

### API endpoints are as follows:
- `http://127.0.0.1:8000/API/users` (POST:  create a new user)
- `http://127.0.0.1:8000/API/users` (GET:  list all users)
- `http://127.0.0.1:8000/API/users/<user_name>` (GET:  get detail of a user)
- `http://127.0.0.1:8000/API/users/<user_name>` (DELETE:  delete a specific user)
- `http://127.0.0.1:8000/API/users/<user_name>` (PUT:  update a specific user)
- After completing the task complete the necessary testing and then upload to a GitHub repository and share the GitHub repository(make sure the repository is public). 
- Update the GitHub readme file with clear instructions about how to run the project on the local machine. This is an essential part because we will only follow your instructions and if it does not run, you may be eliminated from this step and may not go to the next step in the recruiting process.

## Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgments section. Here are a few examples.

* [Python 3.x](https://www.python.org/)
* [Django 5.x](https://www.djangoproject.com/)
* [SQLite Database](https://www.sqlite.org/index.html)
* [Django Rest Framework](https://www.django-rest-framework.org/)

## Installation

You can easily set up the project by following the steps below. In that case, `Docker` and `Docker Compose` are required.

1. Clone the repo
   ```sh
   git clone git@github.com:farjanul/bitmorpher.git
   cd your-repository
   ```
   
2. Create the `.env` file copying from `.env.example` and update these values for both projects.
3. Create and activate a virtual environment
   ```sh
   python3 -m venv <your_virtualenv_name>
   source <your_virtualenv_name>/bin/activate
   ```
4. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
5. Apply database migrations
   ```shell
   python manage.py migrate
   ```
6. Create a superuser
   ```sh
   python manage.py create_admin_user
   ```
   You can see the output
   ```sh
   Default user created successfully
   Authentication token: <authentication_token>
   ```
7. Run the project.
    ```sh
    python manage.py runserver
    ```

## API Endpoints

**User List:** `http://127.0.0.1:8000/API/users/`
**Method:** `GET`
**Headers:**
- `Authorization: <authentication_token>`

**Response Body:**

```json
[
   {
      "username": "admin",
      "email": "admin@admin.com",
      "first_name": "Super",
      "last_name": "Admin",
      "user_type": "manager",
      "date_joined": "2024-06-23T08:16:00.638874Z"
   },
   {
      "username": "user",
      "email": "user@gmail.com",
      "first_name": "First Name",
      "last_name": "Last Name",
      "user_type": "customer",
      "date_joined": "2024-06-23T09:15:35.322213Z"
   }
]
```

**User Details:** `http://127.0.0.1:8000/API/users/<username>/`
**Method:** `GET`
**Headers:**
- `Authorization: <authentication_token>`

**Response Body:**

```json
{
  "username": "admin",
  "email": "admin@admin.com",
  "first_name": "Super",
  "last_name": "Admin",
  "user_type": "manager",
  "date_joined": "2024-06-23T08:16:00.638874Z"
}
```

**User Create:** `http://127.0.0.1:8000/API/users/`
**Method:** `POST`
**Headers:**
- `Authorization: <authentication_token>`

**Request Body:**
```json
{
    "username": "username",
    "first_name": "First Name",
    "last_name": "Last Name",
    "email": "user1@gmail.com"
}
```

**Response Body**
```json
{
    "message": "Created successfully",
    "authentication_token": "dzP3sHXI6YKLmv2u"
}
```

**User Update:** `http://127.0.0.1:8000/API/users/<username>/`
**Method:** `PUT`
**Headers:**
- `Authorization: <authentication_token>`

**Request Body:**
```json
{
    "username": "username",
    "first_name": "First Name",
    "last_name": "Last Name",
    "email": "user1@gmail.com"
}
```

**Response Body**
```json
{
    "message": "Updated successfully"
}
```

**User Delete:** `http://127.0.0.1:8000/API/users/<username>/`
**Method:** `DELETE`
**Headers:**
- `Authorization: <authentication_token>`

**Response Body**
```json
{
    "message": "Deleted successfully"
}
```

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Developer
Follow me on - [@LinkedIn](https://www.linkedin.com/in/farjanuln/)

😊 Happy Coding 😊
