import string
import java.lang as lang
import re
from time import gmtime, strftime
from java.io import *
from java.net import URI;
from javax.xml.parsers import *
from javax.xml.transform import *
from javax.xml.transform.dom import *
from javax.xml.transform.stream import *
from com.marklogic.xcc import *
from com.marklogic.client import *
from org.w3c.dom import *
# Open a file for logging
print >> open("<%=odiRef.getOption("LOG_FILE")%>", 'w'), strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
log = open("<%=odiRef.getOption("LOG_FILE")%>", 'a')
# Determine the file format for incoming documents
fileFormat = io.Format.JSON if "<%=odiRef.getOption("FORMAT")%>" == "JSON" else io.Format.XML
print >> log, "File Format: <%=odiRef.getOption("FORMAT")%>"
# Create a database connection
auth = DatabaseClientFactory.DigestAuthContext("<%=odiRef.getOption("ML_USER")%>","<%=odiRef.getOption("ML_PASSWORD")%>");
client = DatabaseClientFactory.newClient("<%=odiRef.getOption("ML_HOST")%>", int("<%=odiRef.getOption("ML_PORT")%>"), auth);
print >> log, "Created a database connection to <%=odiRef.getOption("ML_HOST")%>:<%=odiRef.getOption("ML_PORT")%> with user: <%=odiRef.getOption("ML_USER")%>."
# Use DataMovementManager
manager = client.newDataMovementManager();
# Setup a write batcher to be used to batch process files.
writer = manager.newWriteBatcher();
writer = writer.withJobName("IKM Import");
writer = writer.withBatchSize(int("<%=odiRef.getOption("BATCH_SIZE")%>"));
<% if (odiRef.getOption("FORMAT").equals("XML")) { %>
# Use a transformer for XML
tf = TransformerFactory.newInstance()
transformer = tf.newTransformer()
transformer.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, "yes")
<% } %>
# TODO: Do something with onBatchFailure and onBatchSuccess listeners
# Start the job to be used while processing files.
job = manager.startJob(writer);
docFactory = DocumentBuilderFactory.newInstance()
builder = docFactory.newDocumentBuilder()

rowCount = 0