# Roles

<a name="getroles"></a>

## Get roles

**URL** : `/xhr/role`

**Method** : `GET`

**Authentication required** : `YES`

**Example**

```
GET /xhr/role
```

### On success

Response Code : `200`

```
[
  {
    "id": 1,
    "name": "Administrator",
    "parent_id": null,
    "permissions": [
      {
        "id": 1,
        "type": "users",
        "access": "write",
        "role_id": 1,
        "settings_id": null
      },
      {
        "id": 2,
        "type": "domains",
        "access": "write",
        "role_id": 1,
        "settings_id": null
      },
      {
        "id": 3,
        "type": "audit",
        "access": "read",
        "role_id": 1,
        "settings_id": null
      },
      {
        "id": 4,
        "type": "settings",
        "access": "write",
        "role_id": 1,
        "settings_id": null
      }
    ]
  }
]
```

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="getrolebyid"></a>

## Get role by ID

**URL** : `/xhr/role/_id/:id`

**Method** : `GET`

**Authentication required** : `YES`

**Query parameters**

- **parameter**: id (Role ID)

**Example**

```
GET /xhr/role/_id/1
```

### On success

Response Code : `200`

```
{
  "id": 1,
  "name": "Administrator",
  "parent_id": null,
  "parent": null,
  "permissions": [
    {
      "id": 2,
      "type": "domains",
      "access": "write",
      "role_id": 1,
      "settings_id": null
    },
    {
      "id": 1,
      "type": "users",
      "access": "write",
      "role_id": 1,
      "settings_id": null
    },
    {
      "id": 4,
      "type": "settings",
      "access": "write",
      "role_id": 1,
      "settings_id": null
    },
    {
      "id": 3,
      "type": "audit",
      "access": "read",
      "role_id": 1,
      "settings_id": null
    }
  ]
}
```

### On failure

Response Code :

- `401 Unauthorized`
- `404 Not Found`
- `500 Internal Server Error`

---

<a name="addrole"></a>

## Add role

**URL** : `/xhr/role`

**Method** : `POST`

**Authentication required** : `YES`

**Body parameters**

- **name**: string (Display name)

**Body parameters (optional)**

- **parent_id**: number (Set a role ID as parent)

**Example**

```
POST /xhr/role
{
  "name": "User",
  "parent_id": 1
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

<a name="updaterole"></a>

## Update role

**URL** : `/xhr/role/_id/:id`

**Method** : `PATCH`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Role ID)

**Body parameters**

- **name**: string (Display name)
- **parent_id**: number (Set a role ID as parent)

**Example**

```
PATCH /xhr/role/_id/1
{
  "name": "Enduser"
}
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="deleterole"></a>

## Delete role

When deleting a role, other roles down the hierarchy based on parent_id will also be deleted.

**URL** : `/xhr/role/_id/:id`

**Method** : `DELETE`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Role ID)

**Example**

```
DELETE /xhr/role/_id/1
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="addpermission"></a>

## Add permission to role

**URL** : `/xhr/role/_id/:id/permission`

**Method** : `POST`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Role ID)

**Body parameters**

- **type**: "domains" | "users" | "settings" | "audit"
- **access**: "read" | "write"

**Body parameters (optional)**

- **settings_id**: number (When type is set to "settings", set permissions to a specific schema setting)

**Example**

```
POST /xhr/role/_id/1/permission
{
  "type": "domains",
  "access": "read"
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

<a name="updatepermission"></a>

## Update permission

When updating role permissions, the changes may affect other roles down the hierarchy based on the role parent_id.

**URL** : `/xhr/role/permission/_id/:id`

**Method** : `PATCH`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Permission ID)

**Body parameters**

- **type**: "domains" | "users" | "settings" | "audit"
- **access**: "read" | "write"

**Example**

```
PATCH /xhr/role/permission/_id/1
{
  "type": "domains",
  "access": "write"
}
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="deletepermission"></a>

## Delete permission

**URL** : `/xhr/role/permission/_id/:id`

**Method** : `DELETE`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Permission ID)

**Example**

```
DELETE /xhr/role/permission/_id/1
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

