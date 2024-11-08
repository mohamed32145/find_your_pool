
# FastAPI Pool Management System

This project is a FastAPI-based application for managing pools, bracelets, and managers. The app connects to a PostgreSQL database and allows CRUD operations for pools, bracelets, and managers, as well as functionalities to link bracelets to pools. The project is Dockerized for easy deployment.

## Features

- **Add Pools, Bracelets, and Managers**: Create entries in the database for pools, bracelets, and managers.
- **Retrieve Pools**: Get details of a pool by its unique code.
- **Connect Bracelets to Pools**: Link bracelets to pools to track customers associated with each pool.
- **Delete Entities**: Remove entries from the database as needed.
- **Dockerized Environment**: Easy setup with Docker Compose, including a PostgreSQL database.

## Technologies Used

- **FastAPI**: The web framework.
- **PostgreSQL**: The database for storing pool, bracelet, and manager data.
- **Docker & Docker Compose**: For containerization of the application and database.

## Getting Started

### Prerequisites

- **Docker** and **Docker Compose** installed on your machine.



### API Endpoints

#### Pool Endpoints

- **Add Pool**: `POST /add_pool/`
- **Get Pool**: `GET /get_pool/?poolcode={poolcode}`
- **Delete Pool**: `DELETE /deletpool/{pool_id}`

#### Bracelet Endpoints

- **Add Bracelet**: `POST /addbracelet/`
- **Delete Bracelet**: `DELETE /deletabrac/{brac_code}`
- **Connect Bracelet to Pool**: `POST /connect_bracelet_to_pool`

#### Manager Endpoints

- **Add Manager**: `POST /addmanager/`
- **Delete Manager**: `DELETE /deletmanager/{manager_id}`



### Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Create a pull request.

