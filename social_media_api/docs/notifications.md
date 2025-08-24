## Additional Endpoints

These endpoints handle **likes** and **notifications** for posts.

| Endpoint                  | Method | Description                              |
|---------------------------|--------|------------------------------------------|
| `/posts/<pk>/like/`       | POST   | Like a post                              |
| `/posts/<pk>/unlike/`     | POST   | Unlike a post                            |
| `/notifications/`         | GET    | List all notifications for the logged-in user |

### Example Requests

**Like a post**

```bash
POST /posts/1/like/
Content-Type: application/json
Authorization: Token <your-token>
Unlike a post

bash
POST /posts/1/unlike/
Content-Type: application/json
Authorization: Token <your-token>
Get notifications

bash
GET /notifications/
Content-Type: application/json
Authorization: Token <your-token>
Notes
Replace <pk> with the specific post ID.

All endpoints require the user to be authenticated.

Notifications are returned only for the logged-in user.

yaml
Copy code
