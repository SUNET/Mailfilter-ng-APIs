# Integrations

<a name="weblogui"></a>

## Web-logui

Use to determine if the integration web-logui is enabled or not in the msui.yaml file.

**URL** : `/xhr/enduser`

**Method** : `GET`

**Authentication required** : `YES`

**Example**

```
GET /xhr/enduser
```

### On success

Response Code : `200`

```
{
  "enabled": true,
  "statistics": true
}
```

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="webloguitransfer"></a>

## Transfer session to Web-logui

Transfer current session to web-logui, when successful the response includes a unique URL to web-logui.

**URL** : `/xhr/enduser/transfer`

**Method** : `GET`

**Authentication required** : `YES`

**Example**

```
GET /xhr/enduser/transfer
```

### On success

Response Code : `200`

```
{
  "url": "https://.../session-transfer.php/"
  "session": "sessionid",
  "page": "index"
}
```

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

