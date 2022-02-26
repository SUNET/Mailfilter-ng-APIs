# Settings

<a name="getsettingsbydomain"></a>

## Get settings

Returns all settings for a domain.

**URL** : `/settings/domain/_id/:id`

**Method** : `GET`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Domain ID)

**Query parameters (Optional)**

- **schema_id**: number (Schema ID)

**Example**

```
GET /xhr/settings/domain/_id/1
```

### On success

Response Code : `200`

```
[
  {
    "schema_id": 1,
    "settings_schema_default": "medium",
    "settings_default": null,
    "settings": null
  },
  {
    "schema_id": 2,
    "settings_schema_default": null,
    "settings_default": {
      "id": 21,
      "properties": {
        "value": [
          "{\"value\":\"127.0.0.2\"}"
        ]
      },
      "settings_schema_id": 10,
      "domain_id": null,
      "user_id": null,
      "default_id": 1
    },
    "settings": {
      "id": 22,
      "properties": {
        "value": []
      },
      "settings_schema_id": 10,
      "domain_id": 1,
      "user_id": null,
      "default_id": null
    }
  }
]
```

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="getsettingsbyuser"></a>

## Get settings

Returns all settings for a user.

**URL** : `/settings/user/_id/:id`

**Method** : `GET`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (User ID)

**Query parameters (Optional)**

- **schema_id**: number (Schema ID)

**Example**

```
GET /xhr/settings/user/_id/1
```

### On success

Response Code : `200`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="getsettingsbydefault"></a>

## Get settings

Returns all settings for a default setting.

**URL** : `/settings/default/_id/:id`

**Method** : `GET`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Default ID)

**Example**

```
GET /xhr/settings/default/_id/1
```

### On success

Response Code : `200`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="getsettingbyid"></a>

## Get setting by ID

**URL** : `GET /xhr/schema/settings/_id/:id`

**Method** : `GET`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Settings ID)

**Example**

```
GET /xhr/schema/settings/_id/1
```

### On success

Response Code : `200`

```
{
  "id": 1,
  "properties": {
    "value": true
  },
  "settings_schema_id": 21,
  "domain_id": null,
  "user_id": null,
  "default_id": 1
}
```

### On failure

Response Code :

- `401 Unauthorized`
- `404 Not Found`
- `500 Internal Server Error`

---

<a name="addsetting"></a>

## Add setting

**URL** : `/xhr/schema/_id/:id/settings`

**Method** : `POST`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Schema ID)
- **force**: "1" | undefined (Force replace any existing value)
- **merge**: "1" | undefined (Merge with existing value, schema list type only)

**Body parameters**

- **properties**: object
  - **value**: string | number | boolean | array (Should respect schema's value type)
- **domain_id**: number (Domain ID)
- **user_id**: number (User ID)
- **default_id**: type (Default ID)

**Example**

```
POST /xhr/schema/_id/1/settings
{
  "user_id": 1,
  "properties": {
    "value": "high"
  }
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

<a name="updatesetting"></a>

## Update setting

**URL** : `/xhr/schema/settings/_id/:id`

**Method** : `PATCH`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Settings ID)

**Body parameters**

- **properties**: object
  - **value**: string | number | boolean | array (Should respect schema's value type)

**Example**

```
PATCH /xhr/schema/settings/_id/2
{
  "properties": {
    "value": "low"
  }
}
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="deletesetting"></a>

## Delete setting

**URL** : `/xhr/schema/settings/_id/:id`

**Method** : `DELETE`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Settings ID)

**Example**

```
DELETE /xhr/schema/settings/_id/2
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`
