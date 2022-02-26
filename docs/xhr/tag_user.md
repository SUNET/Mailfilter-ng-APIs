# Tag user

<a name="taguser"></a>

## Tag a user

**URL** : `/xhr/tags/_id/:tag_id/user/_id/:id`

**Method** : `POST`

**Authentication required** : `YES`

**Query parameters**

- **tag_id**: number (Tag ID)
- **id**: number (User ID)

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `404 Not Found`
- `500 Internal Server Error`

---

<a name="deleteusertag"></a>

## Delete a tag from user

**URL** : `/xhr/tags/_id/:tag_id/user/_id/:id`

**Method** : `DELETE`

**Authentication required** : `YES`

**Query parameters**

- **tag_id**: number (Tag ID)
- **id**: number (User ID)

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `404 Not Found`
- `500 Internal Server Error`

---
