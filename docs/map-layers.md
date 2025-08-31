# Map Layers

We have 12 historical maps that are added as Overlays for the Arches search interface. These are all stored in a single Django fixture that are loaded directly into the database, rather than as multiple map layer definitions that Arches can store in packages. The map layers can be loaded like any other Django fixture:

    python manage.py loaddata historic-map-overlays

The georeferenced maps are GeoTIFFs stored in an S3-compatible bucket, and served to Arches as XYZ tile layers using the [TiTiler](https://developmentseed.org/titiler) installation at [titiler.oldinsurancemaps.net](https://titiler.oldinsurancemaps.net).

|Source name|Layer name|File location|
|---|---|---|
|1851-layer|c. 1851 Plat Map|[https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1850_George_Riggs.tif](https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1850_George_Riggs.tif)|
|1865-layer|1865 Boschke/Barnard Map|[https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1865_Barnard.tif](https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1865_Barnard.tif)|
|1867-layer|1867 Micheler Map|[https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1866-67_Michler_Memory.tif](https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1866-67_Michler_Memory.tif)|
|1873-layer|1873 Map|[https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1873_Bootes.tif](https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1873_Bootes.tif)|
|1877-layer|1877 J.C. Entiwistle Map|[https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1877_JC_Entiwistle.tif](https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1877_JC_Entiwistle.tif)|
|1892-layer|1892 USGS Map|[https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1892_USGS.tif](https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1892_USGS.tif)|
|1910-layer|1910 Army Corps of Engineers Map|[https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1910_ACoE.tif](https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1910_ACoE.tif)|
|1914-layer|1914 Topographical Map|[https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1914_Topo.tif](https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1914_Topo.tif)|
|1944-layer|1944 Topographical Map|[https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1944_Topo.tif](https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1944_Topo.tif)|
|1953-layer|1953 Master Plan Map|[https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1953_Master_Plan.tif](https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1953_Master_Plan.tif)|
|1967-layer|1967 Topographical Map|[https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1967_Topo.tif](https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1967_Topo.tif)|
|1975-layer|1975 Schedule of Structures|[https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1975_Schedule_of_Structures.tif](https://legion-maps.us-southeast-1.linodeobjects.com/afrh/1975_Schedule_of_Structures.tif)|
