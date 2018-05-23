
**WORK IN PROGRESS**

# MarkLogic Integration Knowledge Module for ODI Using DMSDK

## What Is This?

This is an Oracle Data Integrator (ODI) Integration Knowledge Module (IKM) that allows data to be transferred from an ORACLE database to a MarkLogic database using Oracle's ODI and the Data Movement SDK. This project is a fork from [Ryan Dew's](https://github.com/ryanjdew) [odi-ikm-sql-to-marklogic](https://github.com/ryanjdew/odi-ikm-sql-to-marklogic) project that uses XCC

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

At this point, you can import the IKM XML (**KM_IKM_SQL_to_MarkLogic__Batch.xml**). 
From the designer tab in ODI Studio:
1. Connect to the repository if not connected.
2. Expand **Demo**.
3. Right click **Knowledge Modules**.
4. Set the **File import directory** to the location of the IKM XML file.
5. Select the filename from the list and click **OK**.

## How To Run The IKM

1. Create a target model and child target Datastore:
   1. Expand **Models**
   2. Right click **Orders Application** (or create a new model and right click it) and select **New Datastore**
   3. Enter a name.
   4. Click the **Attributes** tab and add attributes to be sent to MarkLogic.
   5. Save the changes.
2. Create a new Mapping:
   1. From the **Projects** section, expand **Sales Administration**.
   2. Right click on **Mappings** and select **New Mapping**.
   3. Name the new map and save it.
3. Drag the source datastore to your new Mapping.
4. Drag your target datastore created in step 1 into the new mapping.
5. Assign the attributes from the source datastore to the target datastore by dragging source attributes to the corresponding attribute in the target datastore.
6. Use the IKM for the new map:
   1. On the **Physical** view of your mapping, select the target datastore.
   2. Click the **Integration Knowledge Module attributes** tab. 
   3. Select ***IKM SQL to MarkLogic (Batch)**
7. From the same screen and tab from step 6, update the options:
   * **FORMAT -** XML/JSON - File format to go into MarkLogic
   * **LOG_FILE -** Local File Path - The path and name of the logfile the IKM should write to.
   * **BATCH_SIZE -** Number - The number of documents to process in each batch sent to MarkLogic.
   * **ML_HOST -** Host name or IP of the target MarkLogic instance.
   * **ML_PORT -** Port to use for the connection. (This should point to the destination database)
   * **ML_USER -** Marklogic user to use for the jobs.
   * **ML_PASSWORD -** Password
   * **ML_COLLECTION -** Collection that incoming documents should be added to.
   * **XML_ROOT -** Name of the root XML element to use.
8. Run your Mapping to send your content to MarkLogic!
