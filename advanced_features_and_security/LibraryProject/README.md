# Django Permissions and Groups Setup

This Django app uses **custom permissions** and **user groups** to control access to the `Article` model and its related views.

---

## Custom Permissions

The `Article` model defines the following permissions:

- `can_view`: Permission to view articles.
- `can_create`: Permission to create new articles.
- `can_edit`: Permission to edit existing articles.
- `can_delete`: Permission to delete articles.

---

## User Groups and Permission Assignment

Three user groups are created to manage these permissions:

| Group   | Permissions                              |
|---------|----------------------------------------|
| Viewers | `can_view`                             |
| Editors | `can_view`, `can_create`, `can_edit`  |
| Admins  | `can_view`, `can_create`, `can_edit`, `can_delete` |

---

## Setup Instructions

1. **Apply migrations** (run this after any model or permission changes):

   ```bash
   python manage.py makemigrations
   python manage.py migrate
