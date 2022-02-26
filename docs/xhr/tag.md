# Tags

<a name="gettags"></a>

## Get users

**URL** : `/xhr/tags`

**Method** : `GET`

**Authentication required** : `YES`

**Query parameters**

- **filter.field**: ["name", "owner"]
- **filter.query**: string
- **sort.orderby**: "name" | "owner" | "count"
- **sort.direction**: "asc" | "desc"
- **sort.limit**: number
- **sort.offset**: number
- **sort.page**: number

**Example**

```
GET /xhr/tags?sort[limit]=2&sort[orderby]=name&sort[direction]=desc
```

### On success

Response Code : `200`

```
{
  "results": [
    {
      "id": 10,
      "name": "example tag",
      "owner_id": null,
      "classname": "tag-1",
      "domain": null,
      "tag_count":4
    }
  ],
  "total": 1
}
```

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="gettagbyid"></a>

## Get tag by ID

**URL** : `/xhr/tags/_id/:id`

**Method** : `GET`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Tag ID)

**Example**

```
GET /xhr/tags/_id/1
```

### On success

Response Code : `200`

### On failure

Response Code :

- `401 Unauthorized`
- `404 Not Found`
- `500 Internal Server Error`

---

<a name="addtag"></a>

## Add tag

**URL** : `/xhr/tags`

**Method** : `POST`

**Authentication required** : `YES`

**Body parameters (required)**

- **name**: string (Tag name)

**Body parameters (optional)**

- **owner_id**: string | null (Domain owner)
- **classname**: "" | "tag-1" | "tag-2" | "tag-3" | "tag-4" | null (Tag type)

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="updatetag"></a>

## Update tag

**URL** : `/xhr/tags/_id/:id`

**Method** : `PATCH`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Tag ID)

**Body parameters (optional)**

- **name**: string (Tag name)
- **owner_id**: string | null (Domain owner)
- **classname**: "" | "tag-1" | "tag-2" | "tag-3" | "tag-4" | null (Tag type)

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `404 Not Found`
- `500 Internal Server Error`

---

<a name="deletetag"></a>

## Delete tag

**URL** : `/xhr/tags/_id/:id`

**Method** : `DELETE`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Tag ID)

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `404 Not Found`
- `500 Internal Server Error`

---
