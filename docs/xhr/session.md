# Session

<a name="logout"></a>

## Logout user

**URL** : `/xhr/logout`

**Method** : `GET`

**Authentication required** : `YES`

**Example**

```
GET /xhr/logout
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="info"></a>

## Session information

**URL** : `/xhr/session`

**Method** : `GET`

**Authentication required** : `YES`

**Example**

```
GET /xhr/session
```

### On success

Response Code : `200`

```
{
  "user": {
    "username": "admin",
    "superAdmin": true
  },
  "session": {
    "maxAge": 6729273,
    "totp": false
  }
}
```

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="generatetotp"></a>

## Generate TOTP secret

Returns a secret that should be used when setting up Google Authenticator.

**URL** : `/xhr/session/totp/generate`

**Method** : `GET`

**Authentication required** : `YES`

**Example**

```
GET /xhr/session/totp/generate
```

### On success

Response Code : `200`

```
{
  "secret": "OR5GG3..."
}
```

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="addtotp"></a>

## Add TOTP

Activate Google authentication for current user, can only be applied to database users.

**URL** : `/xhr/session/totp`

**Method** : `POST`

**Authentication required** : `YES`

**Body parameters**

- **secret**: string (Secret key generated from GET /xhr/session/totp/generate)
- **token**: string (A token from Google authenticator)

**Example**

```
POST /xhr/session/totp
{
  "secret": "OR5GG3...",
  "token": "123456"
}
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`

---

<a name="deletetotp"></a>

## Delete TOTP

**URL** : `/xhr/session/totp`

**Method** : `DELETE`

**Authentication required** : `YES`

**Body parameters**

- **token**: string (A token from Google Authenticator)

**Example**

```
DELETE /xhr/session/totp
{
  "token": "123456"
}
```

### On success

Response Code : `204`

### On failure

Response Code :

- `401 Unauthorized`
- `500 Internal Server Error`
