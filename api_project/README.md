## Authentication & Permissions Setup

- **Authentication**: Token-based (`rest_framework.authtoken`)
- **Token Endpoint**: `POST /api-token-auth/`
  - Payload: `username`, `password`
  - Returns: `{ "token": "<auth_token>" }`
- **Usage**:
  - Add header: `Authorization: Token <your_token>`
- **Permissions**: API views use `IsAuthenticated`
- **Endpoints**:
  - `GET /books/`: List all books (authenticated users only)
  - `POST /books/`: Create a new book (authenticated users only)
