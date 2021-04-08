# Site settings

<a name="getsiteoptions"></a>

## Get site options

A list of options for the frontend.

**URL** : `/xhr/site`

**Method** : `GET`

**Authentication required** : `YES`

**Example**

```
GET /xhr/site
```

### On success

Response Code : `200`

```
[
  {
    "id": 1,
    "name": "_site_dashboard_footer",
    "value": "Managed Service UI | [example.com](https://www.example.com) | [support@example.com](mailto:support@example.com)"
  },
  {
    "id": 2,
    "name": "_site_dashboard_card_title",
    "value": "Managed Service UI | Information"
  }
]
```

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="getoptionbyid"></a>

## Get site option by ID

**URL** : `/xhr/site/_id/:id`

**Method** : `GET`

**Authentication required** : `YES`

**Query parameters**

- **id**: number (Option ID)

**Example**

```
GET /xhr/site/_id/1
```

### On success

Response Code : `200`

```
{
  "id": 1,
  "name": "_site_dashboard_footer",
  "value": "Managed Service UI | [example.com](https://www.example.com) | [support@example.com](mailto:support@example.com)"
}
```

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="getoptions"></a>

## Get options names

Returns a list of all predefined options.

**URL** : `/xhr/site/options`

**Method** : `GET`

**Authentication required** : `YES`

**Query parameters**

- **parameter**: type (description)

**Example**

```
GET /xhr/site/options
```

### On success

Response Code : `200`

```
[
  {
    "name": "_site_title",
    "placeholder": "Managed Service UI",
    "type": "text"
  },
  {
    "name": "_site_navbar_title",
    "placeholder": "Managed Service UI",
    "type": "text"
  }
]
```

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="addoption"></a>

## Add site option

**URL** : `/xhr/site`

**Method** : `POST`

**Authentication required** : `YES`

**Body parameters**

- **name**: string (A valid option name)
- **value**: string

**Example**

```
POST /xhr/site
{
  "name": "_site_title",
  "value": "New page title"
}
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="updateoption"></a>

## Update site option

description...

**URL** : `/xhr/site/_id/:id`

**Method** : `PATCH`

**Authentication required** : `YES`

**Body parameters**

- **value**: string

**Example**

```
PATCH /xhr/site/_id/1
{
  "value": "Managed Service UI"
}
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="deleteoption"></a>

## Delete site option

**URL** : `/xhr/site/_id/:id`

**Method** : `DELETE`

**Authentication required** : `YES`

**Example**

```
DELETE /xhr/site/_id/1
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`


