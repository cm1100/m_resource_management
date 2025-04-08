# Multi-Tenant Task Management System

## 1. Overview

This project is a multi-tenant task management system built using Django. It supports dynamic schema creation and schema switching at request time, ensuring data isolation for each tenant. The system uses PostgreSQL as the database and Django REST Framework for API development.

---

## 2. System Design Decisions

### Dynamic Schema Creation and Switching

- **Tenant Table in Public Schema**: The `Tenant` table resides in the public schema and stores metadata about tenants, including their schema names.
- **Separate Schemas for Tenant Data**: Each tenant's data is stored in a separate schema, ensuring data isolation and scalability.
- **Dynamic Schema Switching**: The `SchemaMiddleware` dynamically switches the database schema based on the `TENANT-ID` provided in the request headers. This ensures that each request operates within the correct tenant's schema.

### Key Features

- **Dynamic Schema Management**: Schemas are created dynamically when a new tenant is added, and migrations are applied to the new schema.
- **JWT Authentication**: Secure authentication using JSON Web Tokens (JWT) with tenant-specific user data.
- **Rate Limiting**: Tenant-specific rate limiting using custom throttling classes.
- **Audit Logging**: Automatic logging of resource creation, updates, and deletions for accountability.

---

## 3. Instructions to Run the Project

### Prerequisites

- Docker and Docker Compose installed.

### Steps to Run

1. Clone the repository:
   ```bash
   git clone git@github.com:cm1100/m_resource_management.git
   cd cd m_resource_management/
   sudo docker compose up --build
   ```

---

## 4. Documentation

    postman collection is already in the folder
