MarkLogic Integration Knowledge Module for ODI
=======================

What Is This?
-------------

This is a knowledge module allows data to be tranfered to MarkLogic using Oracle's ODI.

Technology Versions
-------------------

This was tested against the following technologies:

- Oracle ODI 12c
- MarkLogic 8.0-5.5
- MarkLogic XCC 8.0-5


How To Install The Knowledge Module
-----------------------------------

This Knowledge Module relies on MarkLogic's XCC Java library. You can download the library from https://developer.marklogic.com/products/xcc. After downloading the zipped distribution, you'll need to copy lib/marklogic-xcc-8.0.5.jar into the ~/.odi/oracledi/userlib folder. 

In order for the library to be found, the ODI Studio will need to be restarted.

At this point, you can import the Knowledge Module XML (full-marklogic-ikm-export.xml). 


How To Run The Knowledge Module
-------------------------------

1. Setup a XCDB Server associated with the desired content database as described at https://docs.marklogic.com/guide/admin/xdbc#id_21458. Note that for the associated Modules database, you can select Modules.

2. Create a target Model, with a child target Datastore.

3. Define the attributes that you want to be sent to MarkLogic in the target datastore.

4. Create a new Mapping.

5. Add the source datastore to your new Mapping.

6. Add your target datastore created in step 1.

7. Assign the attributes from the source datastore to the target datastore by dragging source attributes to the corresponding attribute in the target datastore.

8. On the "Physical" view of your mapping, select the target datastore to view its Integration Knowledge Module attributes. Be sure to select "IKM SQL to MarkLogic" and adjust the connection options to reflect your MarkLogic XDBC Server instance created in step 1. 

9. Run your Mapping to send your content to MarkLogic!