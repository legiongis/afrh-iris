# Permissions System

Arches provides capabilities for granting specific permissions for data access and editing to individual users, or to groups of users. You can read more about how Arches handles permissions [here](https://arches.readthedocs.io/en/stable/administering/managing-permissions/).

AFRH-IRIS must facilitate access by seven of different categories of users, which we classify as the following:

- **public** (visitors to the site that aren't signed in)
- **admin1**
- **admin2**
- **afrh_staff**
- **afrh_volunteer**
- **plc_staff**
- **contractor**

Each category of user has a different level of access to each resource model in the system, with regard to

1. Viewing resource instances
    - Full view, limited view, or access denied
2. Creating/editing resource intances

For a full breakdown by resource model, see [Permissions by Resource Model](#permissions-by-resource-model) below.

## Creating a New User

When a new user is created in the Django admin interface (afrh-iris.com/admin), they must be added to a series of groups in order to properly situate them within one of the permissions categories. The following table should be used to guide group assignment. Groups in **bold** are defalt Arches groups, all others are custom to the AFRH-IRIS system.

| admin1                   | admin2                   | afrh_staff               | afrh_volunteer              | plc_staff                   | contractor                  |
|--------------------------|--------------------------|--------------------------|-----------------------------|-----------------------------|-----------------------------|
| ArchaeologicalZone:Full  | ArchaeologicalZone:Full  | ArchaeologicalZone:Full  | ArchaeologicalZone:Limited  | ArchaeologicalZone:Limited  | ArchaeologicalZone:Limited  |
| CharacterArea:Full       | CharacterArea:Full       | CharacterArea:Full       | CharacterArea:Full          | CharacterArea:Full          | CharacterArea:Full          |
| HistoricArea:Full        | HistoricArea:Full        | HistoricArea:Full        | HistoricArea:Full           | HistoricArea:Full           | HistoricArea:Full           |
| MasterPlanZone:Full      | MasterPlanZone:Full      | MasterPlanZone:Full      | MasterPlanZone:Full         | MasterPlanZone:Full         | MasterPlanZone:Full         |
| InventoryResource:Full   | InventoryResource:Full   | InventoryResource:Full   | InventoryResource:Limited   | InventoryResource:Full      | InventoryResource:Full      |
| InformationResource:Full | InformationResource:Full | InformationResource:Full | InformationResource:Limited | InformationResource:Limited | InformationResource:Limited |
| Person:Full              | Person:Full              | Person:Full              | Person:Full                 | Person:Full                 | Person:Full                 |
| Organization:Full        | Organization:Full        | Organization:Full        | Organization:Full           | Organization:Full           | Organization:Full           |
| ARPAReview:Full          | ARPAReview:Full          | ARPAReview:Deny          | ARPAReview:Deny             | ARPAReview:Full             | ARPAReview:Deny             |
| ManagementActivity:Full  | ManagementActivity:Full  | ManagementActivity:Full  | ManagementActivity:Full     | ManagementActivity:Deny     | ManagementActivity:Deny     |
| **Resource Editor**         | **Resource Editor**          | **Resource Editor**          | **Resource Editor**             |                             | **Resource Editor**            |
| InventoryResource:Edit   | InventoryResource:Edit   | InventoryResource:Edit   | InventoryResource:Edit      |                             | InformationResource:Edit    |
| CharacterArea:Edit       | Person:Edit              | Person:Edit              | Person:Edit                 |                             |                             |
| HistoricArea:Edit        | Organization:Edit        | Organization:Edit        | Organization:Edit           |                             |                             |
| MasterPlanZone:Edit      | InformationResource:Edit | InformationResource:Edit | InformationResource:Edit    |                             |                             |
| ArchaeologicalZone:Edit  | ManagementActivity:Edit  |                          |                             |                             |                             |
| Person:Edit              |                          |                          |                             |                             |                             |
| Organization:Edit        |                          |                          |                             |                             |                             |
| InformationResource:Edit |                          |                          |                             |                             |                             |
| ManagementActivity:Edit  |                          |                          |                             |                             |                             |
| ARPAReview:Edit          |                          |                          |                             |                             |                             |
| **RDM Administrator**        |                          |                          |                             |                             |                             |

## Test Accounts

A suite of example user accounts, one per permission level, can be created with

```
python manage.py initialize test-users
```

The following users will be created and automatically assigned to groups as described above:

|username|password|
|---|---|
|admin1|admin1|
|admin2|admin2|
|afrh_staff|afrh_staff|
|afrh_volunteer|afrh_volunteer|
|plc_staff|plc_staff|
|contractor|contractor|

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
