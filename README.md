# Healthcare Management API

A Django REST Framework API for managing users, patients, doctors, and patient-doctor assignments. Authentication uses JSON Web Tokens (JWT).

## Features

- Register and log in with an email address and password.
- Create, view, update, and delete patient records.
- Create, view, update, and delete doctor records.
- Assign a doctor to a patient and remove assignments.
- Prevent duplicate patient-doctor assignments.
- Restrict patient records to the user that created them.

## Project structure

```text
HealthcareManagement/
|-- healthcare_backend/
|   |-- manage.py
|   |-- api.http                 # Requests for the VS Code REST Client extension
|   |-- healthcare_backend/      # Django configuration
|   |-- users/                   # Custom user and JWT login/register API
|   |-- patients/
|   |-- doctors/
|   `-- mappings/
`-- venv/
```

## Requirements

- Python 3
- PostgreSQL
- Django
- Django REST Framework
- `djangorestframework-simplejwt`
- `django-environ`
- A PostgreSQL driver, such as `psycopg`

## Setup

1. Open a terminal in the `HealthcareManagement` directory.

2. Activate the virtual environment on Windows:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

3. Create `healthcare_backend/.env` using `healthcare_backend/.env.example` as a guide:

   ```env
   SECRET_KEY=replace-with-a-long-secret-value
   DEBUG=True
   DATABASE_URL=postgresql://postgres:your-password@localhost:5432/healthcare_db
   ```

4. Create the PostgreSQL database specified by `DATABASE_URL`.

5. Change into the Django project directory and run migrations:

   ```powershell
   cd healthcare_backend
   python manage.py migrate
   ```

6. Start the server:

   ```powershell
   python manage.py runserver
   ```

The API is then available at `http://127.0.0.1:8000/`.

## Authentication

Register a user:

```http
POST /api/auth/register/
Content-Type: application/json

{
  "name": "TestUser",
  "email": "TestUser@example.com",
  "password": "TestPassword@123"
}
```

Log in to receive `access` and `refresh` JWT tokens:

```http
POST /api/auth/login/
Content-Type: application/json

{
  "email": "TestUser@example.com",
  "password": "TestPassword@123"
}
```

For protected endpoints, send the access token in this header:

```http
Authorization: Bearer <access-token>
```

## API endpoints

| Area | Method | Endpoint | Description |
| --- | --- | --- | --- |
| Auth | POST | `/api/auth/register/` | Register a user |
| Auth | POST | `/api/auth/login/` | Log in and receive JWT tokens |
| Patients | GET, POST | `/api/patients/` | List or create the current user's patients |
| Patients | GET, PUT, PATCH, DELETE | `/api/patients/<id>/` | Manage one of the current user's patients |
| Doctors | GET, POST | `/api/doctors/` | List or create doctors |
| Doctors | GET, PUT, PATCH, DELETE | `/api/doctors/<id>/` | Manage one doctor |
| Mappings | GET, POST | `/api/mappings/` | List or create patient-doctor mappings |
| Mappings | GET | `/api/mappings/<patient_id>/` | List mappings for a patient |
| Mappings | DELETE | `/api/mappings/<id>/delete/` | Remove one mapping |

## Testing requests in VS Code

Install the **REST Client** extension by Huachao Mao (`humao.rest-client`). Open [`healthcare_backend/api.http`](healthcare_backend/api.http), start the Django server, then click **Send Request** above a request.

Run the requests in this order:

1. Register a user once.
2. Log in to obtain an access token.
3. Create a patient.
4. Create a doctor.
5. Create a patient-doctor mapping.

The file stores response values such as the access token, patient ID, doctor ID, and mapping ID as REST Client variables, so later requests can reuse them.

## Notes

- Patient `age` must be greater than zero.
- Doctor `specialization` cannot be blank.
- A doctor cannot be assigned to the same patient more than once.

