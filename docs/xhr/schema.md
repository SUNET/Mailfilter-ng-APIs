# Schema settings

<a name="getschemas"></a>

## Get schemas

**URL** : `/xhr/schema`

**Method** : `GET`

**Authentication required** : `YES`

**Query parameters (optional)**

- **sort.orderby**: "name" | "weight"
- **sort.direction**: "asc" | "desc"
- **sort.limit**: number
- **sort.offset**: number
- **sort.page**: number

**Example**

```
GET /xhr/schema
```

### On success

Response Code : `200`

```
[
  {
    "id": 1,
    "identifier": "antispam",
    "name": "Enable antispam",
    "description": "Enable antispam for this domain.",
    "properties": {
      "type": "toggle",
      "default_value": true,
      "option_values": []
    },
    "access_type": "domain",
    "weight": 2,
    "group_id": 1
  },
  {
    "id": 2,
    "identifier": "spamlevel",
    "name": "Spam level",
    "description": "",
    "properties": {
      "type": "select",
      "default_value": "medium",
      "option_values": [
        "high",
        "medium",
        "low"
      ]
    },
    "access_type": "all",
    "weight": 2,
    "group_id": 1
  }
]
```

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="getschemabyid"></a>

## Get schema by ID

description...

**URL** : `/xhr/schema/_id/:id`

**Method** : `GET`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Schema ID)

**Example**

```
GET /xhr/schema/_id/1
```

### On success

Response Code : `200`

```
{
  "id": 1,
  "identifier": "antispam",
  "name": "Enable antispam",
  "description": "Enable antispam for this domain.",
  "properties": {
    "type": "toggle",
    "default_value": true,
    "option_values": []
  },
  "access_type": "domain",
  "weight": 2,
  "group_id": 1
}
```

### On failure

Response Code :

- `401 Unauthorized`
- `404 Not Found`
- `500 Internal Server Error`

---

<a name="addschema"></a>

## Add schema

**URL** : `/xhr/schema`

**Method** : `POST`

**Authentication required** : `YES`

**Body parameters**

- **identifier**: string (Unique settings identifier, which the MTA will use to fetch domain and user settings with)
- **name**: string (Display name)
- **description**: string (Description for the schema setting)
- **properties**: object
  - **type**: "input" | "textarea" | "select" | "multiselect" | "toggle" | "list"
  - **default_value**: string | number | boolean | array
  - **option_values**: array
  - **placeholder**: string (Display placeholder)
  - **ttl**: boolean (For list type)
  - **comment**: string (For list type)
  - **feature**: boolean
  - **validate**: object
    - **enabled**: boolean
    - **type**: "regex"
    - **regex**: object
      - **pattern**: string
      - **switches**: string
- **access_type**: "all" | "domain" | "user" (Applied to all or domains / users)
- **weight**: number (Sort order)
- **group_id**: number (Group ID)

**Example**

```
POST /xhr/schema
{
  "identifier": "antivirus",
  "name": "Enable antivirus",
  "description": "Enable or disable antivirus checks",
  "properties": {
    "type": "toggle",
    "default_value": true
  },
  "access_type": "all",
  "weight": 5
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

<a name="updateschema"></a>

## Update schema

**URL** : `/xhr/schema/_id/:id`

**Method** : `PATCH`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Schema ID)

**Body parameters**

- **identifier**: string (Unique settings identifier, which the MTA will use to fetch domain and user settings with)
- **name**: string (Display name)
- **description**: string (Description for the schema setting)
- **properties**: object
  - **type**: "input" | "textarea" | "select" | "multiselect" | "toggle" | "list"
  - **default_value**: string | number | boolean | array
  - **option_values**: array
  - **placeholder**: string (Display placeholder)
  - **ttl**: boolean (For list type)
  - **comment**: string (For list type)
  - **feature**: boolean
  - **validate**: object
    - **enabled**: boolean
    - **type**: "regex"
    - **regex**: object
      - **pattern**: string
      - **switches**: string
- **access_type**: "all" | "domain" | "user" (Applied to all or domains / users)
- **weight**: number (Sort order)
- **group_id**: number (Group ID)

**Example**

```
PATCH /xhr/schema/_id/1
{
  "weight": 5
}
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="deleteschema"></a>

## Delete schema

**URL** : `/xhr/schema/_id/:id`

**Method** : `DELETE`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Schema ID)

**Example**

```
DELETE /xhr/schema/_id/1
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="getgroups"></a>

## Get schema group

**URL** : `/xhr/schemagroup`

**Method** : `GET`

**Authentication required** : `YES`

**Query parameters (optional)**

- **sort.orderby**: "name" | "weight"
- **sort.direction**: "asc" | "desc"
- **sort.limit**: number
- **sort.offset**: number
- **sort.page**: number

**Example**

```
GET /xhr/schemagroup
```

### On success

Response Code : `200`

```
[
  {
    "id": 1,
    "name": "Inbound protection",
    "description": "Enable/disable features for antivirus and antispam",
    "weight": 0
  },
  {
    "id": 2,
    "name": "Outbound features",
    "description": "",
    "weight": 2
  }
]
```

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="getgroupbyid"></a>

## Get schema group by ID

**URL** : `/xhr/schemagroup/_id/:id`

**Method** : `GET`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Schema group ID)

**Example**

```
GET /xhr/schemagroup/_id/1
```

### On success

Response Code : `200`

```
{
  "id": 1,
  "name": "Inbound protection",
  "description": "Enable/disable features for antivirus and antispam.",
  "weight": 0
}
```

### On failure

Response Code :

- `401 Unauthorized`
- `404 Not Found`
- `500 Internal Server Error`

---

<a name="addgroup"></a>

## Add schema group

description...

**URL** : `/xhr/schemagroup`

**Method** : `POST`

**Authentication required** : `YES`

**Body parameters**

- **name**: string (Display name)
- **description**: string (Display description)
- **weight**: number (Sort order)

**Example**

```
POST /xhr/schemagroup
{
  "name": "Inbound features",
  "description": "",
  "weight": 1
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

<a name="updategroup"></a>

## Update schema group

**URL** : `/xhr/schemagroup/_id/:id`

**Method** : `PATCH`

**Authentication required** : `YES`

**Body parameters**

- **name**: string (Display name)
- **description**: string (Display description)
- **weight**: number (Sort order)

**Example**

```
PATCH /xhr/schemagroup/_id/1
{
  "description": "List of features related to inbound protection"
}
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="deletegroup"></a>

## Delete schema group

**URL** : `/xhr/schemagroup/_id/:id`

**Method** : `DELETE`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Schema group ID)

**Example**

```
DELETE /xhr/schemagroup/_id/1
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

