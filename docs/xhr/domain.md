# Domain

<a name="getdomains"></a>

## Get domains

Returns a list of domains filtered by permissions, offset and limit.

**URL** : `/xhr/domain`

**Method** : `GET`

**Authentication required** : `YES`

**Query parameters (optional)**

- **filter.fields**: ["domain", "transport", "owner", "auth"]
- **filter.query**: string
- **filter.method**: "contains" | "is"
- **sort.orderby**: "domain" | "created" | "authentication" | "users" | "owner"
- **sort.direction**: "asc" | "desc"
- **sort.limit**: number
- **sort.offset**: number
- **sort.page**: number

**Example**

```
GET /xhr/domain?sort[limit]=1&sort[orderby]=domain&sort[direction]=desc
```

### On success

Response Code : `200`

```
{
  "results": [
    {
      "id": 1,
      "domain": "example.com",
      "transport": {
        "destination": [
          {
            "port": 25,
            "hostname": "mail.example.com"
          }
        ]
      },
      "authmethod": "database",
      "authmethod_id": null,
      "auto_create_users": 0,
      "auto_create_roleid": null,
      "parent_id": null,
      "owner_id": null,
      "created_at_ts0": "2020-03-09T13:20:26.000Z",
      "last_modified_ts0": "2020-05-29T10:24:37.000Z"
    }
  ],
  "total": 15
}
```

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="getdomainbyid"></a>

## Get domain by ID

**URL** : `/xhr/domain/_id/:id`

**Method** : `GET`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Domain ID)

**Example**

```
GET /xhr/domain/_id/1
```

### On success

Response Code : `200`

```
{
  "id": 1,
  "domain": "example.com",
  "transport": {
    "destination": [
      {
        "port": 25,
        "hostname": "mail.example.com"
      }
    ]
  },
  "authmethod": "database",
  "authmethod_id": null,
  "auto_create_users": 0,
  "auto_create_roleid": null,
  "parent_id": null,
  "owner_id": null,
  "created_at_ts0": "2020-03-09T13:20:26.000Z",
  "last_modified_ts0": "2020-05-29T10:24:37.000Z",
  "alias": [],
  "parent": null
}
```

### On failure

Response Code :

- `401 Unauthorized`
- `404 Not Found`
- `500 Internal Server Error`

---

<a name="getdomainbyfqdn"></a>

## Get domain by fully qualified domain name

**URL** : `/xhr/domain/:fqdn`

**Method** : `GET`

**Authentication required** : `YES`

**Query parameters**

- **fqdn**: string (Fully qualified domain name)

**Example**

```
GET /xhr/domain/example.com
```

### On success

Response Code : `200`

```
{
  "id": 1,
  "domain": "example.com",
  "transport": {
    "destination": [
      {
        "port": 25,
        "hostname": "mail.example.com"
      }
    ]
  },
  "authmethod": "database",
  "authmethod_id": null,
  "auto_create_users": 0,
  "auto_create_roleid": null,
  "parent_id": null,
  "owner_id": null,
  "created_at_ts0": "2020-03-09T13:20:26.000Z",
  "last_modified_ts0": "2020-05-29T10:24:37.000Z",
  "alias": [],
  "parent": null
}
```

### On failure

Response Code :

- `401 Unauthorized`
- `404 Not Found`
- `500 Internal Server Error`

---

<a name="adddomain"></a>

## Add domain

**URL** : `/xhr/domain`

**Method** : `POST`

**Authentication required** : `YES`

**Body parameters (required)**

- **domain**: string (Fully qualified domain name)
- **authmethod**: "database" | "ldap" (Auth method for domain users)

**Body parameters (optional)**

- **transport**: object (Destination(s) for inbound emails)
  - **destination**: array,
    - **hostname**: string,
    - **port**: number
- **auto_create_users**: number | null (Used as a flag to automatically create users from the MTA)
- **auto_create_roleid**: number | null (Auto created users will be given a predefined role ID)
- **parent_id**: number | null (Domain ID for a parent domain, used for alias domains, when specified, only domain parameter should be included)
- **owner_domain_id**: number | null (Gives another domain ownership of this domain, can be used to build an hierarchy of permissions)

**Example**

```
POST /xhr/domain
{
  "domain": "example.com",
  "transport": {
    "destination": [
      {
        "hostname": "mail.example.com",
        "port": 25
      }
    ]
  },
  "authmethod": "database",
  "owner_domain_id": 2
}
```

### On success

Response Code : `200`

```
{
  "id": 1
}
```

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="updatedomain"></a>

## Update domain by ID

**URL** : `/xhr/domain/_id/:id`

**Method** : `PATCH`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Domain ID)

**Body parameters (optional)**

- **domain**: string
- **authmethod**: "database" | "ldap"
- **transport**: object
  - **destination**: array,
    - **hostname**: string,
    - **port**: number
- **auto_create_users**: number | null
- **auto_create_roleid**: number | null
- **parent_id**: number | null
- **owner_domain_id**: number | null

**Example**

```
PATCH /xhr/domain/_id/1
{
  "domain": "example.org"
}
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="deletedomain"></a>

## Delete domain by ID

**URL** : `/xhr/domain/_id/:id`

**Method** : `DELETE`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Domain ID)

**Example**

```
DELETE /xhr/domain/_id/1
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`
