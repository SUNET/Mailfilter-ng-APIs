# Frontend

<a name="sitesetting"></a>

## Site settings

Site settings that are available for public requests.

- _login_css

**URL** : `/xhr/site/_name/:name`

**Method** : `GET`

**Authentication required** : `NO`

**Query parameters**

- **name**: string (Valid setting name)

### On success

Response Code : `200`

```
{
  id: number,
  name: string,
  value: string
}
```

Response Code : `204`

Unknown or non public setting was requested.

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

<a name="options"></a>

## Frontend options

Used by the frontend to change behaviour depending on the option value.

**URL** : `/xhr/frontend/options`

**Method** : `GET`

**Authentication required** : `NO`

### On success

Response Code : `200`

```
{
  "option name": "value"
}
```

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`


