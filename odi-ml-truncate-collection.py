from com.marklogic.client import query
from java.lang import String
from jarray import array
print >> log, "Deleting the documents in the collection: " + str("<%=odiRef.getOption("ML_COLLECTION")%>")
queryManager = client.newQueryManager()
deleteQuery = queryManager.newDeleteDefinition()
deleteQuery.setCollections(array(["<%=odiRef.getOption("ML_COLLECTION")%>"], String))
queryManager.delete(deleteQuery)
print >> log, "Starting transfer."