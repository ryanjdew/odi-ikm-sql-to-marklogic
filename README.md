
**WORK IN PROGRESS**

# MarkLogic Integration Knowledge Module for ODI Using DMSDK

## What Is This?

This is an Oracle Data Integrator (ODI) Integration Knowledge Module (IKM) that allows data to be transferred from an ORACLE database to a MarkLogic database using Oracle's ODI and the Data Movement SDK

### Technology Versions

This was tested against the following technologies:

- Oracle ODI 12c
- MarkLogic 9.0-5
- MarkLogic Client API 4.0.4

## How To Install The IKM

The sample IKM relies on MarkLogic's Java Client API. You can download the library from https://developer.marklogic.com/products/java. After downloading and unzipping, you'll need to copy the following jar files into the __~/.odi/oracledi/userlib__ folder:

* marklogic-client-api-4.0.4.jar
* okhttp-3.10.0.jar
* okio-1.14.0.jar 

In order for the library to be found, the ODI Studio will need to be restarted.

At this point, you can import the IKM XML (odi-ikm-sql-to-marklogic-full-export.xml). 

## How To Run The IKM

1. Create a target Model, with a child target Datastore.

2. Define the attributes that you want to be sent to MarkLogic in the target datastore.

3. Create a new Mapping.

4. Add the source datastore to your new Mapping.

5. Add your target datastore created in step 1.

6. Assign the attributes from the source datastore to the target datastore by dragging source attributes to the corresponding attribute in the target datastore.

7. On the "Physical" view of your mapping, select the target datastore to view its Integration Knowledge Module attributes. Be sure to select "IKM SQL to MarkLogic" and adjust the connection options to reflect your MarkLogic XDBC Server instance created in step 1. 

8. Run your Mapping to send your content to MarkLogic!
