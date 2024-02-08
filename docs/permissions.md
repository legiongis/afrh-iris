## AFRH Permissions System

!!! Important
    Work in progress

Following requests from the AFRH, an implementation-specific permission system has been created. However, it has been done so in a granular manner that should allow easy conversion to meet completely different needs.

The main set of permissions is managed on a resource type basis. A standard set of Permission ojects are created per resource type, and then assigned to specific Group objects as necessary. Thus, a new user can be created as part of a preset group, thereby gaining a number of preset individual permissions, but can also have individual permissions added. The creation of all permissions and groups is handled in setup.py (as well as the prior removal of the default Arches-HIP permissions and groups), and the assignment of a resource type's subset permissions to a specific group is defined as a new key/value pair in settings.RESOURCE_TYPE_CONFIGS().

A more specific configuration was added to allow any given Information Resource to be hidden from the public (i.e. any 'anonymous' user). This is based on the value of a single node in the Information Resource graph. In other words, it implemented completely outside of the built-in Django admin framework system.

### Permission Objects

For each resource type, CREATE, EDIT, FULLREPORT, and VIEW. CREATE and EDIT are self-explanatory. FULLREPORT means that the user will view an unfiltered report for resources of a certain type, and if a user lacks VIEW permission, the resource type will be screened from 1. the map view, 2. search results, and 3. related resource graphs.

Therefore, the list of all available permissions looks something like this:

CREATE | Inventory Resource
CREATE | Actor
..etc

An additional permission object called "AFRH | RDM Access" gives users access to the Reference Data Manager.

### Permission Groups

The app has the following permission groups:

+ *admin1*
+ *admin2*
+ *afrh_staff*
+ *afrh_volunteer*
+ *development*

Each group is automatically assigned specific permissions, as defined in settings.RESOURCE_TYPE_CONFIGS(). During the install of this app, a sample user is made for each group, whose name and password are one of the groups listed above.

### Permissions Detail

#### RDM

| Group           | RDM      |
| --------------- | :------: |
| public*         | **x**    |
| admin1          | &#10004; |
| admin2          | **x**    |
| afrh_staff      | **x**    |
| afrh_volunteer  | **x**    |
| development     | **x**    |

### Inventory Resource

| Group           | CREATE    | EDIT     | FULLREPORT | VIEW     |
| --------------- | :-------: | :------: | :--------: | :------: |
| public*         | **x**     | **x**    | **x**      | &#10004; |
| admin1          | &#10004;  | &#10004; | &#10004;   | &#10004; |
| admin2          | &#10004;  | &#10004; | &#10004;   | &#10004; |
| afrh_staff      | **x**     | **x**    | &#10004;   | &#10004; |
| afrh_volunteer  | **x**     | **x**    | **x**      | &#10004; |
| development     | **x**     | **x**    | **x**      | &#10004; |

### Master Plan Zone

| Group           | CREATE    | EDIT     | FULLREPORT | VIEW     |
| --------------- | :-------: | :------: | :--------: | :------: |
| public*         | **x**     | **x**    | &#10004;   | &#10004; |
| admin1          | &#10004;  | &#10004; | &#10004;   | &#10004; |
| admin2          | &#10004;  | &#10004; | &#10004;   | &#10004; |
| afrh_staff      | **x**     | **x**    | &#10004;   | &#10004; |
| afrh_volunteer  | **x**     | **x**    | &#10004;   | &#10004; |
| development     | **x**     | **x**    | &#10004;   | &#10004; |

### Character Area

| Group           | CREATE    | EDIT     | FULLREPORT | VIEW     |
| --------------- | :-------: | :------: | :--------: | :------: |
| public*         | **x**     | **x**    | &#10004;   | &#10004; |
| admin1          | &#10004;  | &#10004; | &#10004;   | &#10004; |
| admin2          | &#10004;  | &#10004; | &#10004;   | &#10004; |
| afrh_staff      | **x**     | **x**    | &#10004;   | &#10004; |
| afrh_volunteer  | **x**     | **x**    | &#10004;   | &#10004; |
| development     | **x**     | **x**    | &#10004;   | &#10004; |

### Archaeological Zone

| Group           |  CREATE   | EDIT     | FULLREPORT | VIEW     |
| --------------- | :-------: | :------: | :--------: | :------: |
| public*         | **x**     | **x**    | **x**      | &#10004; |
| admin1          | &#10004;  | &#10004; | &#10004;   | &#10004; |
| admin2          | &#10004;  | &#10004; | &#10004;   | &#10004; |
| afrh_staff      | **x**     | **x**    | &#10004;   | &#10004; |
| afrh_volunteer  | **x**     | **x**    | **x**      | &#10004; |
| development     | **x**     | **x**    | **x**      | &#10004; |

### Historic Area

| Group           | CREATE    | EDIT     | FULLREPORT | VIEW     |
| --------------- | :-------: | :------: | :--------: | :------: |
| public*         | **x**     | **x**    | &#10004;   | &#10004; |
| admin1          | &#10004;  | &#10004; | &#10004;   | &#10004; |
| admin2          | &#10004;  | &#10004; | &#10004;   | &#10004; |
| afrh_staff      | **x**     | **x**    | &#10004;   | &#10004; |
| afrh_volunteer  | **x**     | **x**    | &#10004;   | &#10004; |
| development     | **x**     | **x**    | &#10004;   | &#10004; |

### Field Investigation

| Group           | CREATE    | EDIT     | FULLREPORT | VIEW     |
| --------------- | :-------: | :------: | :--------: | :------: |
| public*         | **x**     | **x**    | **x**      | &#10004; |
| admin1          | &#10004;  | &#10004; | &#10004;   | &#10004; |
| admin2          | &#10004;  | &#10004; | &#10004;   | &#10004; |
| afrh_staff      | **x**     | **x**    | &#10004;   | &#10004; |
| afrh_volunteer  | **x**     | **x**    | **x**      | &#10004; |
| development     | **x**     | **x**    | **x**      | &#10004; |

### Actor

| Group           | CREATE    | EDIT     | FULLREPORT | VIEW     |
| --------------- | :-------: | :------: | :--------: | :------: |
| public*         | **x**     | **x**    | **x**      | &#10004; |
| admin1          | &#10004;  | &#10004; | &#10004;   | &#10004; |
| admin2          | &#10004;  | &#10004; | &#10004;   | &#10004; |
| afrh_staff      | &#10004;  | &#10004; | &#10004;   | &#10004; |
| afrh_volunteer  | &#10004;  | &#10004; | &#10004;   | &#10004; |
| development     | &#10004;  | &#10004; | &#10004;   | &#10004; |

### Information Resource

| Group           | CREATE    | EDIT     | FULLREPORT | VIEW     |
| --------------- | :-------: | :------: | :--------: | :------: |
| public*         | **x**     | **x**    | &#10004;   | &#10004; |
| admin1          | &#10004;  | &#10004; | &#10004;   | &#10004; |
| admin2          | &#10004;  | &#10004; | &#10004;   | &#10004; |
| afrh_staff      | **x**     | **x**    | &#10004;   | &#10004; |
| afrh_volunteer  | &#10004;  | &#10004; | &#10004;   | &#10004; |
| development     | **x**     | **x**    | &#10004;   | &#10004; |

Management Activity (A)

| Group           | CREATE    | EDIT     | FULLREPORT | VIEW     |
| --------------- | :-------: | :------: | :--------: | :------: |
| public*         | **x**     | **x**    | **x**      | **x**    |
| admin1          | &#10004;  | &#10004; | &#10004;   | &#10004; |
| admin2          | &#10004;  | &#10004; | &#10004;   | &#10004; |
| afrh_staff      | &#10004;  | &#10004; | &#10004;   | &#10004; |
| afrh_volunteer  | **x**     | **x**    | **x**      | **x**    |
| development     | **x**     | **x**    | **x**      | **x**    |

Management Activity (B)

| Group           | CREATE    | EDIT     | FULLREPORT | VIEW     |
| --------------- | :-------: | :------: | :--------: | :------: |
| public*         | **x**     | **x**    | **x**      | **x**    |
| admin1          | &#10004;  | &#10004; | &#10004;   | &#10004; |
| admin2          | &#10004;  | &#10004; | &#10004;   | &#10004; |
| afrh_staff      | **x**     | **x**    | &#10004;   | &#10004; |
| afrh_volunteer  | **x**     | **x**    | **x**      | **x**    |
| development     | &#10004;  | &#10004; | &#10004;   | &#10004; |
