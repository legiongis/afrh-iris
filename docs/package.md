# Package Contents

The contents of the package define the database structure and schema for all data entry. Generally, package files are in JSON format. These files are used once during database initialization, and are no longer used after that.

If changes are made to the resource models in the AFRH-IRIS interface, it is a best practice to export that item and place it into the package, to maintain the integrity of new installations, when needed.

There is a default directory in the package for business_data (resource instances), but we keep these files out of version control.

## Resource Models

There are 10 resource models in the package:

- **Inventory Resource** The 250+ historic resources (buildings, sites, objects) managed by the AFRH-W.
- **Character Area** The character defining areas throughout the grounds
- **Historic Area** Designated historic areas of the grounds
- **Master Plan Zone** Management zones as defined in the AFRH-W master plan
- **Archaeological Zone** Archaeological Zones as defined in the AFRH-W development plan
- **Person** To store records for people that are associated with the Inventory Resources (e.g.,historical builders and architects)
- **Organization** To store records for organizations
- **Information Resource** Photos, documents, architectural drawings
- **Management Activity** To track and manage development projects that take place throughout the grounds 9more below)
- **ARPA Review** For ARPA reviews to be recorded and connected to relevant resources

### Management Activities

The **Management Activity** model allows for the creation of a "resource" in the database for a development project, like a golf hole relocation. Records of official reviews (NEPA, Section 106...), project boundaries, consultations, points of contact, etc. can all be attached to a Management Activity resource. In turn, the Management Activity can be related to any other database resource.

### Changes since Arches v3

There are a few differences in the resource models we have now, compared to those we implemented in our original Arches database.

- The original **Management Activity A** and **Management Activity B** models have been collapsed in the single **Management Activity** model.
- The original **Person/Organization** model has been split into two different models
- The original **Field Investigation** model has been deprecated.

## Ontologies

The resource models were designed using the Linked Art ontology, which in turn inherits from the CIDOC CRM. These ontology definitions are stored in the package and loaded during database initialization.

## Reference Data

A single thesuarus and set of collections is stored in the package. These populate the dropdowns that appear in various resource model nodes (`concept` and `concept-list` datatypes).
