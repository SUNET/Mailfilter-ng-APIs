# User

<a name="getusers"></a>

## Get users

**URL** : `/xhr/user`

**Method** : `GET`

**Authentication required** : `YES`

**Query parameters**

- **filter.field**: ["username", "role"]
- **filter.value**: string
- **sort.orderby**: "username" | "created" | "modified" | "lastactive"
- **sort.direction**: "asc" | "desc"
- **sort.limit**: number
- **sort.offset**: number
- **sort.page**: number

**Example**

```
GET /xhr/user?sort[limit]=2&sort[orderby]=username&sort[direction]=desc
```

### On success

Response Code : `200`

```
{
  "results": [
    {
      "id": 2,
      "username": "user",
      "role_id": 4,
      "domain_id": 1,
      "created_at_ts0": "2020-03-09T13:36:51.000Z",
      "last_modified_ts0": null,
      "last_active_ts0": null,
      "domain": "example.com",
      "relation": []
    },
    {
      "id": 3,
      "username": "helpdesk",
      "role_id": 2,
      "domain_id": 2,
      "created_at_ts0": "2020-03-09T13:54:40.000Z",
      "last_modified_ts0": null,
      "last_active_ts0": null,
      "domain": "example.org",
      "relation": []
    }
  ],
  "total": 7
}
```

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="getuserbyid"></a>

## Get user by ID

**URL** : `/xhr/user/_id/:id`

**Method** : `GET`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (User ID)

**Example**

```
GET /xhr/user/_id/1
```

### On success

Response Code : `200`

```
{
  "id": 1,
  "username": "admin",
  "role_id": 3,
  "domain_id": 1,
  "created_at_ts0": "2020-03-09T13:36:36.000Z",
  "last_modified_ts0": "2020-03-09T13:54:06.000Z",
  "last_active_ts0": null,
  "domain": "example.com",
  "relation": []
}
```

### On failure

Response Code :

- `401 Unauthorized`
- `404 Not Found`
- `500 Internal Server Error`

---

<a name="adduser"></a>

## Add user

**URL** : `/xhr/user`

**Method** : `POST`

**Authentication required** : `YES`

**Body parameters**

- **username**: string (Username, without domain suffix)
- **role_id**: number (Role ID)
- **domain_id**: number (Domain ID)
- **password**: string | null

**Body parameters (optional)**

- **domain**: string (FQDN, overrides the `domain_id` parameter)

**Example**

```
POST /xhr/user
{
  "username": "admin",
  "role_id": 1,
  "domain_id": 1,
  "password": "badpassword",
  "password_verify": "badpassword"
}
```

### On success

Response Code : `200`

```
{
  "id": number
}
```

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="updateuser"></a>

## Update user by ID

**URL** : `/xhr/user/_id/:id`

**Method** : `PATCH`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (User ID)
- **password**: string | null

**Body parameters**

- **role_id**: number (Role ID)

**Body parameters (optional)**

- **domain**: string (FQDN, overrides the `domain_id` parameter)

**Example**

```
PATCH /xhr/user/_id/1
{
  "password": "newpassword",
  "password_verify": "newpassword",
  "role_id": 2
}
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="deleteuser"></a>

## Delete user by ID

**URL** : `/xhr/user/_id/:id`

**Method** : `DELETE`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (User ID)

**Example**

```
DELETE /xhr/user/_id/1
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="getrelation"></a>

## Get user relation by ID

**URL** : `/xhr/user/relation/_id/:id`

**Method** : `GET`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Relation ID)

**Example**

```
GET /xhr/user/relation/_id/1
```

### On success

Response Code : `200`

```
{
  "id": 1,
  "user_id": 1,
  "access_type": "user",
  "access": "adminalias@example.com",
  "user": {
    "id": 1,
    "username": "admin",
    "role_id": 1,
    "domain_id": 1,
    "created_at_ts0": "2020-07-14T05:59:21.000Z",
    "last_modified_ts0": null,
    "last_active_ts0": null
  }
}
```

### On failure

Response Code :

- `401 Unauthorized`
- `404 Not Found`
- `500 Internal Server Error`

---

<a name="addrelation"></a>

## Add user relation

description...

**URL** : `/xhr/user/_id/:id/relation`

**Method** : `POST`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (User ID)

**Body parameters**

- **type**: "user"
- **access**: string (Email or FQDN)

**Example**

```
POST /xhr/user/_id/1/relation
{
  "type": "user",
  "access": "box@example.com"
}
```

### On success

Response Code : `200`

```
{
  "id": number
}
```

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="deleterelation"></a>

## Delete user relation by ID

**URL** : `/xhr/user/relation/_id/:id`

**Method** : `DELETE`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Relation ID)

**Example**

```
DELETE /xhr/user/relation/_id/1
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`
