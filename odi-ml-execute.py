from java.lang import String
from com.marklogic.client import *
from jarray import array
rowCount = rowCount + 1

# Get the record ID for the current row
newRecordId = ""
<%=odiRef.getColList("", "if \u0022[CX_COL_NAME]\u0022 == recordIdentifier: newRecordId = \u0022#[CX_COL_NAME]\u0022", "\n", "", "(INS and !TRG)")%>

# Initialize recordId if this is the first record
if newRecordId != "" and recordId == "": recordId = newRecordId

# Add the record to the batch writer when a new record ID is encountered
if recordId != newRecordId:
  addToBatch(output)
  # Reset output and the recordId
  output = ""
  recordId = newRecordId

<% if (odiRef.getOption("FORMAT").equals("JSON")) { %>
if output != "": output = output + ","
output = output + "{ "
<%=odiRef.getColList("", "output = output + \u0022\\\u0022[CX_COL_NAME]\\\u0022 : \\\u0022#[CX_COL_NAME]\\\u0022", ",\u0022\n", "\u0022", "(INS and !TRG)")%>
output = output + "}"
extension = "json"
<% } else { %>
# TODO: Fix XML root for multiple row records.
doc = builder.newDocument()
results = doc.createElement("<%=odiRef.getOption("XML_ROOT")%>")
doc.appendChild(results)
<%=odiRef.getColList("", "node = doc.createElement(\u0022[CX_COL_NAME]\u0022)\nnode.appendChild(doc.createTextNode(\u0022#[CX_COL_NAME]\u0022))\nresults.appendChild(node)", "\n", "", "(INS and !TRG)")%>
sw = StringWriter()
transformer.transform(DOMSource(doc), StreamResult(sw))
output = output + sw.getBuffer().toString()
extension = "xml"
<% } %>
