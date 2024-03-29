# Permissions System

Arches provides capabilities for granting specific permissions for data access and editing to individual users, or to groups of users. You can read more about how Arches handles permissions [here](https://arches.readthedocs.io/en/stable/administering/managing-permissions/).

To implement permissions, we have created five Groups to which individual users can be added, and then used these groups to attach data-level permissions to each resource model. In this way different groups of users gain access to specific parts of each resource model.

The five groups are:

- **admin1**
- **admin2**
- **afrh_staff**
- **afrh_volunteer**
- **development**

## Creating a New User

When a new user is created, they should be added to the Group that corresponds to their permissions level, as well as the **Resource Editor** group.

Any users at the **admin1** level should also be added to the **RDM Administrator** group, in order to give them access to the Reference Data Manager.

!!! Note
    The default `admin` user is already a "superuser" and automatically has all permissions, so that user need not be added to any groups.

## Permissions by Resource Model

To implement permissions on specific parts of a resource model so that certain users have edit, read-only, or no access at all, we must use the Permissions tab on that resource model in the Arches designer. **This must be performed manually after the initial installation of the package**.

The following tables provide a guide for how this should be implemented on each model. Note that FULLREPORT means a group should have read-only access to every node in that resource model, while VIEW means they should only have read access to a subset of the nodes.

!!! Important
    We still need to determine which fields should be included in the VIEW level for each resource model. (We could also change this terminology).

### Inventory Resource

| Group           | CREATE/EDIT    | FULLREPORT | VIEW     |
| --------------- | :------------: | :--------: | :------: |
| public*         | **x**          | **x**      | &#10004; |
| admin1          | &#10004;       | &#10004;   | &#10004; |
| admin2          | &#10004;       | &#10004;   | &#10004; |
| afrh_staff      | **x**          | &#10004;   | &#10004; |
| afrh_volunteer  | **x**          | **x**      | &#10004; |
| development     | **x**          | **x**      | &#10004; |

### Master Plan Zone

| Group           | CREATE/EDIT    | FULLREPORT | VIEW     |
| --------------- | :------------: | :--------: | :------: |
| public*         | **x**          | &#10004;   | &#10004; |
| admin1          | &#10004;       | &#10004;   | &#10004; |
| admin2          | &#10004;       | &#10004;   | &#10004; |
| afrh_staff      | **x**          | &#10004;   | &#10004; |
| afrh_volunteer  | **x**          | &#10004;   | &#10004; |
| development     | **x**          | &#10004;   | &#10004; |

### Character Area

| Group           | CREATE/EDIT    | FULLREPORT | VIEW     |
| --------------- | :------------: | :--------: | :------: |
| public*         | **x**          | &#10004;   | &#10004; |
| admin1          | &#10004;       | &#10004;   | &#10004; |
| admin2          | &#10004;       | &#10004;   | &#10004; |
| afrh_staff      | **x**          | &#10004;   | &#10004; |
| afrh_volunteer  | **x**          | &#10004;   | &#10004; |
| development     | **x**          | &#10004;   | &#10004; |

### Archaeological Zone

| Group           | CREATE/EDIT    | FULLREPORT | VIEW     |
| --------------- | :------------: | :--------: | :------: |
| public*         | **x**          | **x**      | &#10004; |
| admin1          | &#10004;       | &#10004;   | &#10004; |
| admin2          | &#10004;       | &#10004;   | &#10004; |
| afrh_staff      | **x**          | &#10004;   | &#10004; |
| afrh_volunteer  | **x**          | **x**      | &#10004; |
| development     | **x**          | **x**      | &#10004; |

### Historic Area

| Group           | CREATE/EDIT    | FULLREPORT | VIEW     |
| --------------- | :------------: | :--------: | :------: |
| public*         | **x**          | &#10004;   | &#10004; |
| admin1          | &#10004;       | &#10004;   | &#10004; |
| admin2          | &#10004;       | &#10004;   | &#10004; |
| afrh_staff      | **x**          | &#10004;   | &#10004; |
| afrh_volunteer  | **x**          | &#10004;   | &#10004; |
| development     | **x**          | &#10004;   | &#10004; |

### Information Resource

| Group           | CREATE/EDIT    | FULLREPORT | VIEW     |
| --------------- | :------------: | :--------: | :------: |
| public*         | **x**          | &#10004;   | &#10004; |
| admin1          | &#10004;       | &#10004;   | &#10004; |
| admin2          | &#10004;       | &#10004;   | &#10004; |
| afrh_staff      | **x**          | &#10004;   | &#10004; |
| afrh_volunteer  | &#10004;       | &#10004;   | &#10004; |
| development     | **x**          | &#10004;   | &#10004; |

### Person

!!! Warning
    Is this correct?

| Group           | CREATE/EDIT    | FULLREPORT | VIEW     |
| --------------- | :------------: | :--------: | :------: |
| public*         | **x**          | **x**      | &#10004; |
| admin1          | &#10004;       | &#10004;   | &#10004; |
| admin2          | &#10004;       | &#10004;   | &#10004; |
| afrh_staff      | &#10004;       | &#10004;   | &#10004; |
| afrh_volunteer  | &#10004;       | &#10004;   | &#10004; |
| development     | &#10004;       | &#10004;   | &#10004; |

### Organization

!!! Warning
    Is this correct?

| Group           | CREATE/EDIT    | FULLREPORT | VIEW     |
| --------------- | :------------: | :--------: | :------: |
| public*         | **x**          | **x**      | &#10004; |
| admin1          | &#10004;       | &#10004;   | &#10004; |
| admin2          | &#10004;       | &#10004;   | &#10004; |
| afrh_staff      | &#10004;       | &#10004;   | &#10004; |
| afrh_volunteer  | &#10004;       | &#10004;   | &#10004; |
| development     | &#10004;       | &#10004;   | &#10004; |

### ARPA Review

!!! Warning
    Is this correct?

| Group           | CREATE/EDIT    | FULLREPORT | VIEW     |
| --------------- | :------------: | :--------: | :------: |
| public*         | **x**          | **x**      | **x**    |
| admin1          | &#10004;       | &#10004;   | &#10004; |
| admin2          | &#10004;       | &#10004;   | &#10004; |
| afrh_staff      | &#10004;       | &#10004;   | &#10004; |
| afrh_volunteer  | **x**          | **x**      | **x**    |
| development     | **x**          | **x**      | **x**    |

### Management Activity

!!! Warning
    Is this correct?

| Group           | CREATE/EDIT    | FULLREPORT | VIEW     |
| --------------- | :------------: | :--------: | :------: |
| public*         | **x**          | **x**      | **x**    |
| admin1          | &#10004;       | &#10004;   | &#10004; |
| admin2          | &#10004;       | &#10004;   | &#10004; |
| afrh_staff      | &#10004;       | &#10004;   | &#10004; |
| afrh_volunteer  | **x**          | **x**      | **x**    |
| development     | **x**          | **x**      | **x**    |
