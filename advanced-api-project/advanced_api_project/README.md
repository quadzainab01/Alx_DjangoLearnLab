# Advanced API Project - Custom & Generic Views

## Overview
This module implements CRUD operations for the Book model using Django REST Framework's generic views.

## Endpoints
- `GET /books/` → List all books (public)
- `GET /books/<id>/` → Retrieve book by ID (public)
- `POST /books/create/` → Create book (authenticated users only)
- `PUT /books/<id>/update/` → Update book (authenticated users only)
- `DELETE /books/<id>/delete/` → Delete book (authenticated users only)

## Permissions
- **Public Access**: List and Detail views
- **Authenticated Access**: Create, Update, Delete

## Customizations
- `perform_create` and `perform_update` methods used for extra logic.
- Optional: Role-based access using `IsAdminOrReadOnly` permission.

## Testing
Test endpoints with Postman or curl. Ensure token-based authentication is active.
