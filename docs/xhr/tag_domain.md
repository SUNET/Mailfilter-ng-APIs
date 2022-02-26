# Tag domain

<a name="tagdomain"></a>

## Tag domain

**URL** : `/xhr/tags/_id/:tag_id/domain/_id/:id`

**Method** : `POST`

**Authentication required** : `YES`

**Query parameters**

- **tag_id**: number (Tag ID)
- **id**: number (Domain ID)

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `404 Not Found`
- `500 Internal Server Error`

---

## Delete a tag from domain

<a name="deletedomaintag"></a>

## Tag domain

**URL** : `/xhr/tags/_id/:tag_id/domain/_id/:id`

**Method** : `DELETE`

**Authentication required** : `YES`

**Query parameters**

- **tag_id**: number (Tag ID)
- **id**: number (Domain ID)

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `404 Not Found`
- `500 Internal Server Error`

---
