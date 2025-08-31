# Permissions System

Arches provides capabilities for granting specific permissions for data access and editing to individual users, or to groups of users. You can read more about how Arches handles permissions [here](https://arches.readthedocs.io/en/stable/administering/managing-permissions/).

To implement permissions, we have created five Groups to which individual users can be added, and then used these groups to attach data-level permissions to each resource model. In this way different groups of users gain access to specific parts of each resource model.

The five groups are:

- **admin1**
- **admin2**
- **afrh_staff**
- **afrh_volunteer**
- **plc_staff**
- **contractor**

## Creating a New User

When a new user is created, they should be added to the Group that corresponds to their permissions level, as well as the **Resource Editor** group.

Any users at the **admin1** level should also be added to the **RDM Administrator** group, in order to give them access to the Reference Data Manager.

!!! Note
    The default `admin` user is already a "superuser" and automatically has all permissions, so that user need not be added to any groups.

## Test Accounts

A suite of example user accounts, one per permission level, can be created with

```
python manage.py initialize test-users
```

The following users will be created and assigned to these groups:

|username|password|groups|
|---|---|---|
|admin1|admin1|TBD admin1, Resource Editor, RDM Administrator|
|admin2|admin2|TBD admin2, Resource Editor|
|afrh_staff|afrh_staff|TBD afrh_staff, Resource Editor|
|afrh_volunteer|afrh_volunteer|TBD afrh_volunteer, Resource Editor|
|plc_staff|plc_staff|TBD plc_staff, Resource Editor|
|contractor|contractor|TBD development, Resource Editor|

!!! Warning
    Group names and memberships still need to be finalized.

## Permissions by Resource Model

To implement permissions on specific parts of a resource model so that certain users have edit, read-only, or no access at all, we must use the Permissions tab on that resource model in the Arches designer. **This must be performed manually after the initial installation of the package**.

The following tables provide a guide for how this should be implemented on each model.

!!! Important
    We still need to determine which fields should hidden for the VIEW:LIMITED level for each resource model.

### Inventory Resource

| Group           | CREATE/EDIT    | VIEW:FULL | VIEW:LIMITED |
| --------------- | :------------: | :--------: | :------: |
| public*         | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   | <span style="color:green">✔</span> |
| admin1          | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| admin2          | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| afrh_staff      | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| afrh_volunteer  | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   | <span style="color:green">✔</span> |
| plc_staff       | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| contractor      | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   | <span style="color:green">✔</span> |

### Master Plan Zone

| Group           | CREATE/EDIT    | VIEW:FULL | VIEW:LIMITED |
| --------------- | :------------: | :--------: | :------: |
| public*         | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| admin1          | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| admin2          | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| afrh_staff      | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| afrh_volunteer  | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| plc_staff       | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| contractor      | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |

### Character Area

| Group           | CREATE/EDIT    | VIEW:FULL | VIEW:LIMITED |
| --------------- | :------------: | :--------: | :------: |
| public*         | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| admin1          | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| admin2          | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| afrh_staff      | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| afrh_volunteer  | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| plc_staff       | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| contractor      | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |

### Archaeological Zone

| Group           | CREATE/EDIT    | VIEW:FULL | VIEW:LIMITED |
| --------------- | :------------: | :--------: | :------: |
| public*         | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   | <span style="color:green">✔</span> |
| admin1          | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| admin2          | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| afrh_staff      | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| afrh_volunteer  | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   | <span style="color:green">✔</span> |
| plc_staff       | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| contractor      | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   | <span style="color:green">✔</span> |

### Historic Area

| Group           | CREATE/EDIT    | VIEW:FULL | VIEW:LIMITED |
| --------------- | :------------: | :--------: | :------: |
| public*         | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| admin1          | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| admin2          | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| afrh_staff      | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| afrh_volunteer  | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| plc_staff       | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| contractor      | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |

### Information Resource

| Group           | CREATE/EDIT    | VIEW:FULL | VIEW:LIMITED |
| --------------- | :------------: | :--------: | :------: |
| public*         | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   | <span style="color:green">✔</span> |
| admin1          | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| admin2          | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| afrh_staff      | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| afrh_volunteer  | <span style="color:green">✔</span> | <span style="color:red">✗</span>   | <span style="color:green">✔</span> |
| plc_staff       | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   | <span style="color:green">✔</span> |
| contractor      | <span style="color:green">✔</span> | <span style="color:red">✗</span>   | <span style="color:green">✔</span> |

### Person

| Group           | CREATE/EDIT    | VIEW:FULL | VIEW:LIMITED |
| --------------- | :------------: | :--------: | :------: |
| public*         | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| admin1          | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| admin2          | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| afrh_staff      | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| afrh_volunteer  | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| plc_staff       | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| contractor      | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |

### Organization

| Group           | CREATE/EDIT    | VIEW:FULL | VIEW:LIMITED |
| --------------- | :------------: | :--------: | :------: |
| public*         | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| admin1          | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| admin2          | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| afrh_staff      | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| afrh_volunteer  | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| plc_staff       | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| contractor      | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |

### ARPA Review

| Group           | CREATE/EDIT    | VIEW:FULL | VIEW:LIMITED |
| --------------- | :------------: | :--------: | :------: |
| public*         | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   |
| admin1          | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| admin2          | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| afrh_staff      | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| afrh_volunteer  | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   |
| plc_staff       | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| contractor      | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   |

### Management Activity

| Group           | CREATE/EDIT    | VIEW:FULL | VIEW:LIMITED |
| --------------- | :------------: | :--------: | :------: |
| public*         | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   |
| admin1          | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| admin2          | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| afrh_staff      | <span style="color:red">✗</span>   | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| afrh_volunteer  | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   |
| plc_staff       | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   | <span style="color:green">✔</span> |
| contractor      | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   |
