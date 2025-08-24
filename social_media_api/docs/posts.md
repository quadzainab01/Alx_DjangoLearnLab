# Social Media API Documentation

This API allows users to create posts, comment on posts, and manage their content. Authentication is required for creating, updating, and deleting resources.

---

## API Endpoints Overview

| Method | Endpoint                | Description                  |
|--------|------------------------|------------------------------|
| GET    | `/api/posts/`           | List all posts (paginated)   |
| POST   | `/api/posts/`           | Create a new post            |
| GET    | `/api/posts/{id}/`      | Retrieve a single post       |
| PUT    | `/api/posts/{id}/`      | Update post (owner only)     |
| DELETE | `/api/posts/{id}/`      | Delete post (owner only)     |
| GET    | `/api/comments/`        | List all comments (paginated)|
| POST   | `/api/comments/`        | Create a comment             |
| GET    | `/api/comments/{id}/`   | Retrieve a single comment    |
| PUT    | `/api/comments/{id}/`   | Update comment (owner only)  |
| DELETE | `/api/comments/{id}/`   | Delete comment (owner only)  |

---

## Testing the API

You can test the API using **Postman** or the **DRF browsable API**.

### Posts Endpoints

| Method | Endpoint            | Description                  |
|--------|-------------------|------------------------------|
| GET    | `/api/posts/`      | List all posts (paginated)   |
| POST   | `/api/posts/`      | Create a new post            |
| GET    | `/api/posts/{id}/` | Retrieve post details        |
| PUT    | `/api/posts/{id}/` | Update post (owner only)     |
| DELETE | `/api/posts/{id}/` | Delete post (owner only)     |

**Example Request:**

```bash
# List posts
GET /api/posts/

# Create a post
POST /api/posts/
Content-Type: application/json
Authorization: Token <your-token>

{
  "title": "My First Post",
  "content": "This is the content of the post."
}
Comments Endpoints
Method	Endpoint	Description
GET	/api/comments/	List all comments (paginated)
POST	/api/comments/	Create a comment
GET	/api/comments/{id}/	Retrieve comment details
PUT	/api/comments/{id}/	Update comment (owner only)
DELETE	/api/comments/{id}/	Delete comment (owner only)

Example Request:

# Create a comment
POST /api/comments/
Content-Type: application/json
Authorization: Token <your-token>

{
  "post": 1,
  "content": "This is a comment."
}
Notes
All POST, PUT, and DELETE requests require authentication.

Replace {id} with the specific post or comment ID.

Pagination is applied to list endpoints by default.