# XHR Endpoints

Documentation for all requests available on /xhr (used by the frontend).

## Open Endpoints

### Authentication

In order to authenticate you need to post a request to one of the following endpoints.
All session data that is associated with an ID is stored server-side.

- [Authenticate local user](/docs/xhr/authentication.md#authlocal) : `POST /xhr/login`
- --[Authenticate LDAP user](/docs/xhr/authentication.md#authldap) : `POST /xhr/login/ldap`--
- --[Authenticate TOTP](/docs/xhr/authentication.md#authtotp) : `POST /xhr/totp`--
- [Remote Authentication](/docs/xhr/authentication.md#authremote) : `POST /xhr/login/remote`

### Frontend

- [Site settings](/docs/xhr/frontend.md#sitesetting) : `GET /xhr/site/_name/:name`
- [Frontend options](/docs/xhr/frontend.md#options) : `GET /xhr/frontend/options`

## Endpoints with authentication required

### Domain related

- [Get domains](/docs/xhr/domain.md#getdomains) : `GET /xhr/domain`
- [Get domain by ID](/docs/xhr/domain.md#getdomainbyid) : `GET /xhr/domain/_id/:id`
- [Get domain by FQDN](/docs/xhr/domain.md#getdomainbyfqdn) : `GET /xhr/domain/:fqdn`
- [Add domain](/docs/xhr/domain.md#adddomain) : `POST /xhr/domain`
- [Update domain](/docs/xhr/domain.md#updatedomain) : `PATCH /xhr/domain/_id/:id`
- [Delete domain](/docs/xhr/domain.md#deletedomain) : `DELETE /xhr/domain/_id/:id`

### User related

- [Get users](/docs/xhr/user.md#getusers) : `GET /xhr/user`
- [Get user by ID](/docs/xhr/user.md#getuserbyid) : `GET /xhr/user/_id/:id`
- [Add user](/docs/xhr/user.md#adduser) : `POST /xhr/user`
- [Update user](/docs/xhr/user.md#updateuser) : `PATCH /xhr/user/_id/:id`
- [Delete user](/docs/xhr/user.md#deleteuser) : `DELETE /xhr/user/_id/:id`
- [Get user relation by ID](/docs/xhr/user.md#getrelation) : `GET /xhr/user/relation/_id/:id`
- [Add user relation](/docs/xhr/user.md#addrelation) : `POST /xhr/user/_id/:id/relation`
- [Delete user relation](/docs/xhr/user.md#deleterelation) : `DELETE /xhr/user/relation/_id/:id`

### Settings related

- [Get settings](/docs/xhr/settings.md#getsettings) : `GET /xhr/schema/settings`
- [Get setting by ID](/docs/xhr/settings.md#getsettingbyid) : `GET /xhr/schema/settings/_id/:id`
- [Add setting](/docs/xhr/settings.md#addsetting) : `POST /xhr/schema/_id/:id/settings`
- [Update setting](/docs/xhr/settings.md#updatesetting) : `PATCH /xhr/schema/settings/_id/:id`
- [Delete setting](/docs/xhr/settings.md#deletesetting) : `DELETE /xhr/schema/settings/_id/:id`

### Schema settings

- [Get schemas](/docs/xhr/schema.md#getschemas) : `GET /xhr/schema`
- [Get schema by ID](/docs/xhr/schema.md#getschemabyid) : `GET /xhr/schema/_id/:id`
- [Add schema](/docs/xhr/schema.md#addschema) : `POST /xhr/schema`
- [Update schema](/docs/xhr/schema.md#updateschema) : `PATCH /xhr/schema/_id/:id`
- [Delete schema](/docs/xhr/schema.md#deleteschema) : `DELETE /xhr/schema/_id/:id`
- [Get schema groups](/docs/xhr/schema.md#getgroups) : `GET /xhr/schemagroup`
- [Get schema group by ID](/docs/xhr/schema.md#getgroupbyid) : `GET /xhr/schemagroup/_id/:id`
- [Add schema group](/docs/xhr/schema.md#addgroup) : `POST /xhr/schemagroup`
- [Update schema group](/docs/xhr/schema.md#updategroup) : `PATCH /xhr/schemagroup/_id/:id`
- [Delete schema group](/docs/xhr/schema.md#deletegroup) : `DELETE /xhr/schemagroup/_id/:id`

### Roles

- [Get roles](/docs/xhr/role.md#getroles) : `GET /xhr/role`
- [Get role by ID](/docs/xhr/role.md#getrolebyid) : `GET /xhr/role/_id/:id`
- [Add role](/docs/xhr/role.md#addrole) : `POST /xhr/role`
- [Update role](/docs/xhr/role.md#updaterole) : `PATCH /xhr/role/_id/:id`
- [Delete role](/docs/xhr/role.md#deleterole) : `DELETE /xhr/role/_id/:id`
- [Add permission to role](/docs/xhr/role.md#addpermission) : `POST /xhr/role/_id/:id/permission`
- [Update permission](/docs/xhr/role.md#updatepermission) : `PATCH /xhr/role/permission/_id/:id`
- [Delete permission](/docs/xhr/role.md#deletepermission) : `DELETE /xhr/role/permission/_id/:id`

### Audit log

- [Get audit log](/docs/xhr/audit.md#getaudit) : `GET /xhr/audit`

### Session

- [Logout user](/docs/xhr/session.md#logout) : `GET /xhr/logout`
- [Session information](/docs/xhr/session.md#info) : `GET /xhr/session`
- [Generate TOTP secret](/docs/xhr/session.md#generatetotp) : `GET /xhr/session/totp/generate`
- [Add TOTP](/docs/xhr/session.md#addtotp) : `POST /xhr/session/totp`
- [Delete TOTP](/docs/xhr/session.md#deletetotp) : `DELETE /xhr/session/totp`

### Site settings

- [Get site options](/docs/xhr/site.md#getsiteoptions) : `GET /xhr/site`
- [Get site option by ID](/docs/xhr/site.md#getoptionbyid) : `GET /xhr/site/_id/:id`
- [Get options names](/docs/xhr/site.md#getoptions) : `GET /xhr/site/options`
- [Add site soption](/docs/xhr/site.md#addoption) : `POST /xhr/site`
- [Update option](/docs/xhr/site.md#updateoption) : `UPDATE /xhr/site/_id/:id`
- [Delete option](/docs/xhr/site.md#deleteoption) : `DELETE /xhr/site/_id/:id`

### Other

- [Web-logui](/docs/xhr/integrations.md#weblogui) : `GET /xhr/enduser`
- [Transfer session to Web-logui](/docs/xhr/integrations.md#webloguitransfer) : `GET /xhr/enduser/transfer`
