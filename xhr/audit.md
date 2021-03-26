# Audit log

<a name="getaudit"></a>

## Get audit log

The audit log can be accessed by all admins in settings.json and with the audit permission. The result may be filtered based on the user's domain permissions.

**URL** : `/xhr/audit`

**Method** : `GET`

**Authentication required** : `YES`

**Example**

```
GET /xhr/audit
```

### On success

Response Code : `200`

```
[
  {
    "id": 1,
    "user": "admin",
    "identifier": null,
    "type": "localauth",
    "action": "login",
    "output": "success",
    "message": "",
    "owner_id": null,
    "created_at_ts0": "2020-03-09T13:20:12.000Z"
  },
  {
    "id": 2,
    "user": "admin",
    "identifier": "example.com",
    "type": "domain",
    "action": "add",
    "output": "success",
    "message": "",
    "owner_id": null,
    "created_at_ts0": "2020-03-09T13:20:26.000Z"
  }
]
```

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`
