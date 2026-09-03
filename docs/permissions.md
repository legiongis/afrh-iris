# Permissions System

## Overview

Arches provides capabilities for granting specific permissions for data access and editing to individual users, or to groups of users. You can read more about how Arches handles permissions [here](https://arches.readthedocs.io/en/stable/administering/managing-permissions/).

AFRH-IRIS must facilitate access by seven of different categories of users, which we classify as the following:

- **Public** (any visitors to the site who aren't signed in)
- **Admin 1**
- **Admin 2**
- **AFRH Staff**
- **AFRH Volunteer**
- **PLC Staff**
- **Contractor**

Each category of user has a different level of access to each Resource Model in the system, with regard to viewing, creating, editing, and deleting instances.

For a full breakdown by resource model, see [Permissions by Resource Model](#permissions-by-resource-model).

## Creating a new user

1. Enter the Django admin site (https://afrh-iris.com/admin) with your admin credentials.
2. Create a new user in the **Authentication and Authorization** > **User** section.
3. In the **Permissions** section of the new user's profile, select one or more items in the **Available groups** list and click the arrow to chose them (**Chosed groups**)

## Pre-configured group permissions by Resource Model

The following configurations have been made in the Arches Graph Designer.

### Inventory Resource

| Group           | VIEW    | CREATE/EDIT/DELETE |
| --------------- | :------------: | :--------: |
| Public*         | <span style="color:green">✔</span>   | <span style="color:red">✗</span> |
| Admin 1         | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| Admin 2         | <span style="color:green">✔</span>   | <span style="color:green">✔</span> |
| AFRH Staff      | <span style="color:green">✔</span>   | <span style="color:red">✗</span> |
| AFRH Volunteer  | <span style="color:green">✔</span>   | <span style="color:red">✗</span> |
| PLC Staff       | <span style="color:green">✔</span>   | <span style="color:red">✗</span> |
| Contractor      | <span style="color:green">✔</span>   | <span style="color:red">✗</span> |

### Information Resource

| Group           | VIEW    | CREATE/EDIT/DELETE |
| --------------- | :------------: | :--------: |
| Public*         | <span style="color:red">✗</span>   | <span style="color:red">✗</span> |
| Admin 1         | <span style="color:green">✔</span>   | <span style="color:green">✔</span> |
| Admin 2         | <span style="color:green">✔</span>   | <span style="color:green">✔</span> |
| AFRH Staff      | <span style="color:green">✔</span>   | <span style="color:green">✔</span> |
| AFRH Volunteer  | <span style="color:red">✗</span>   | <span style="color:red">✗</span> |
| PLC Staff       | <span style="color:red">✗</span>   | <span style="color:red">✗</span> |
| Contractor      | <span style="color:red">✗</span>   | <span style="color:red">✗</span> |

Note: In order to properly filter Information Resources, we will likely need to use resource instance based rules,
i.e. we will disallow groups of users from seeing specific information resources, but allow them to
see others. For now, **no access** is granted to any public or non-AFRH users.

### Master Plan Zone, Character Area, Historic Area

| Group           | VIEW    | CREATE/EDIT/DELETE |
| --------------- | :------------: | :--------: |
| Public*         | <span style="color:green">✔</span>   | <span style="color:red">✗</span> |
| Admin 1          | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| Admin 2          | <span style="color:green">✔</span>   | <span style="color:red">✗</span> |
| AFRH Staff      | <span style="color:green">✔</span>   | <span style="color:red">✗</span> |
| AFRH Volunteer  | <span style="color:green">✔</span>   | <span style="color:red">✗</span> |
| PLC Staff       | <span style="color:green">✔</span>   | <span style="color:red">✗</span> |
| Contractor      | <span style="color:green">✔</span>   | <span style="color:red">✗</span> |

### Archaeological Zone

| Group           | VIEW:LIMITED* | VIEW:FULL | CREATE/EDIT/DELETE |
| --------------- | :------------: | :--------: | :------: |
| Public*         | <span style="color:green">✔</span>   | <span style="color:red">✗</span>   | <span style="color:red">✗</span> |
| Admin 1          | <span style="color:green">✔</span> | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| Admin 2         | <span style="color:green">✔</span>   | <span style="color:green">✔</span> | <span style="color:red">✗</span> |
| AFRH Staff      | <span style="color:green">✔</span>   | <span style="color:green">✔</span> | <span style="color:red">✗</span> |
| AFRH Volunteer  | <span style="color:green">✔</span>   | <span style="color:red">✗</span>   | <span style="color:red">✗</span> |
| PLC Staff       | <span style="color:green">✔</span>   | <span style="color:green">✔</span> | <span style="color:red">✗</span> |
| Contractor      | <span style="color:green">✔</span>   | <span style="color:red">✗</span>   | <span style="color:red">✗</span> |

**\*** _Only allowed to view the Identification (name), Description, and Zone Boundary nodes. Not allowed to see the smaller boundaries of different types of resource concentrations within the zone._

### Person/Organization

| Group           | VIEW    | CREATE/EDIT | DELETE |
| --------------- | :------------: | :--------: | :--------: |
| Public*         | <span style="color:green">✔</span>   | <span style="color:red">✗</span> | <span style="color:red">✗</span> |
| Admin 1          | <span style="color:green">✔</span> | <span style="color:green">✔</span> |<span style="color:green">✔</span> |
| Admin 2          | <span style="color:green">✔</span>   | <span style="color:green">✔</span> |<span style="color:green">✔</span> |
| AFRH Staff      | <span style="color:green">✔</span>   | <span style="color:green">✔</span> |<span style="color:red">✗</span> |
| AFRH Volunteer  | <span style="color:green">✔</span>   | <span style="color:green">✔</span> |<span style="color:red">✗</span> |
| PLC Staff       | <span style="color:green">✔</span>   | <span style="color:red">✗</span> |<span style="color:red">✗</span> |
| Contractor      | <span style="color:green">✔</span>   | <span style="color:green">✔</span> |<span style="color:red">✗</span> |

### Management Activity

| Group           | VIEW    | CREATE/EDIT/DELETE |
| --------------- | :------------: | :--------: |
| Public*         | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   |
| Admin 1          | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| Admin 2          | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| AFRH Staff      | <span style="color:green">✔</span>   | <span style="color:red">✗</span> |
| AFRH Volunteer  | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   |
| PLC Staff       | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   |
| Contractor      | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   |

### All reviews (ARPA, NEPA, CFA, NCPC, Section 106)

| Group           | VIEW    | CREATE/EDIT/DELETE |
| --------------- | :------------: | :--------: |
| Public*         | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   |
| Admin 1          | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| Admin 2          | <span style="color:green">✔</span> | <span style="color:green">✔</span> |
| AFRH Staff      | <span style="color:red">✗</span>   | <span style="color:red">✗</span> |
| AFRH Volunteer  | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   |
| PLC Staff       | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   |
| Contractor      | <span style="color:red">✗</span>   | <span style="color:red">✗</span>   |

## Test accounts

A suite of example user accounts, one per permission level, can be created with

```
python manage.py initialize test-users
```

The following users will be created and automatically assigned to the appropriate group (passwords same as username):

|username|group
|---|---|
|admin1|Admin 1|
|admin2|Admin 2|
|afrh_staff|AFRH Staff|
|afrh_volunteer|AFRH Volunteer|
|plc_staff|PLC Staff|
|contractor|Contractor|
