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
from com.marklogic.client import *
from com.marklogic.client.datamovement import *
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
writer.withJobName("IKM Import");
writer.withBatchSize(int("<%=odiRef.getOption("BATCH_SIZE")%>"));

# Success Listener
<% if (odiRef.getOption("LOG_SUCCESS").equals("Yes")) { %>
class successListener(WriteBatchListener):
  def __init__(self,fn):
    self.processEvent=fn

@successListener
def batchSuccess(batch):
  print >> log, str(batch.getTimestamp().time) + " - SUCCESS (Batch: " + str(batch.getJobBatchNumber()) + ")"

writer.onBatchSuccess(batchSuccess)
<% } %>

# Failure Listener
<% if (odiRef.getOption("LOG_FAILURE").equals("Yes")) { %>
class failListener(WriteFailureListener):
  def __init__(self,fn):
    self.processEvent=fn

@failListener
def batchFail(batch):
  print >> log, str(batch.getTimestamp().time) + " - FAIL (Batch: " + str(batch.getJobBatchNumber()) + ")"

writer.onBatchFailure(batchFail)
<% } %>

<% if (odiRef.getOption("FORMAT").equals("XML")) { %>
# Use a transformer for XML
tf = TransformerFactory.newInstance()
transformer = tf.newTransformer()
transformer.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, "yes")
<% } %>
# Start the job to be used while processing files.
job = manager.startJob(writer);
docFactory = DocumentBuilderFactory.newInstance()
builder = docFactory.newDocumentBuilder()

rowCount = 0