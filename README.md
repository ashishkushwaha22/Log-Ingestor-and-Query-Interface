# Log Ingestor and Query Interface in Django 

## Introduction

This Django Log Ingestor is a comprehensive system designed for efficient handling, storage, and querying of log data. Built with Django and Django REST Framework (DRF), it offers a robust API with advanced functionalities.

## System Design

- **Framework:** Django with Django REST Framework.
- **Database:** PostgreSQL with an option to configure MongoDB.
- **Key Features:**
  - CRUD operations on log entries.
  - Advanced filtering and search capabilities including regex-based searching.
  - Role-based access control for API endpoints.
  - Database optimization through indexing.
  - Scalable architecture capable of handling large volumes of data.

## Features Implemented

1. **CRUD Operations:** Create, Read, Update, and Delete log entries.
2. **Advanced Filtering and Search:** Regex-based and other advanced search capabilities.
3. **Role-Based Authentication:** Secure API with role-based access controls.
4. **Database Indexing:** Improved performance with database indexing.
5. **Support for PostgreSQL and MongoDB:** Flexible database configuration.
6. **API Documentation:** Integrated Swagger/ReDoc for API documentation.
7. **Code Documentation:** Well-documented codebase for maintainability.

## Getting Started

### Prerequisites

- Python 3.x
- Django and Django REST Framework
- PostgreSQL or MongoDB

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/dyte-submissions/november-2023-hiring-ashishkushwaha22
   ```
2. Change directory to the project folder:
   ```
   cd logInjestorProject\
   ```
3. Create and activate a virtual environment:
   ```
   python -m venv venv
   ```
   ```
   venv/bin/activate # On Windows, use venv\Scripts\activate
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Configure the database in `settings.py`. Default is Postgres.

6. Run migrations:
   ```
   python manage.py migrate
   ```

### Running the Project

1. Start the Django server:
   ```
   python manage.py runserver 3000
   ```
2. Access the API endpoints through the provided URLs (e.g., `localhost:3000/`).

### Create Superuser

1. Navigate to root folder:
   ```
   logInjestorProject\
   ```
2. Run the following command:
   ```
   python manage.py createsuperuser
   ```
3. Enter Superuser Details

   You'll be prompted to enter the following details:

- **Username**: Enter a unique username for the superuser.
- **Email address**: Provide an email address for the superuser.
- **Password**: Set a strong password. The characters won't be visible as you type.

4. Complete the process

   After entering the details, press `Enter`. You should see a confirmation that the superuser account has been created.


## API Documentation

- Swagger documentation can be accessed at `/swagger/`.
- ReDoc documentation is available at `/redoc/`.

## Limitations

- Currently, the system does not implement sharding, which could be crucial for handling extremely large datasets.
- The architecture, while scalable, has not yet been adapted for a microservices approach, which may limit its ability to scale horizontally in certain high-demand scenarios.
- Lack of integration with message queues means that the system might not optimally handle sudden surges in log data.
- The system is not yet configured for deployment on distributed systems or cloud-based solutions, which could offer enhanced scalability and performance.

## Future Plans

- **Database Sharding:** Implement database sharding to handle larger datasets and improve scalability.
- **Microservices Architecture:** Transition to a microservices-based architecture to facilitate easier scaling and maintenance.
- **Message Queues Integration:** Incorporate message queues to efficiently manage and process high volumes of incoming log data.
- **Cloud-Based Solutions:** Explore options for deploying the application on cloud platforms to leverage their scalability and distributed nature.

