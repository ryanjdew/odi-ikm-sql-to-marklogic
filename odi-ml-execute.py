from java.lang import String
from com.marklogic.client import *
from jarray import array
rowCount = rowCount + 1
<% if (odiRef.getOption("FORMAT").equals("JSON")) { %>
output = "{ "
<%=odiRef.getColList("", "output = output + \u0022\\\u0022[CX_COL_NAME]\\\u0022 : \\\u0022#[CX_COL_NAME]\\\u0022", ",\u0022\n", "\u0022", "(INS and !TRG)")%>
output = output + "}"
extension = "json"
<% } else { %>
doc = builder.newDocument()
results = doc.createElement("<%=odiRef.getOption("XML_ROOT")%>")
doc.appendChild(results)
<%=odiRef.getColList("", "node = doc.createElement(\u0022[CX_COL_NAME]\u0022)\nnode.appendChild(doc.createTextNode(\u0022#[CX_COL_NAME]\u0022))\nresults.appendChild(node)", "\n", "", "(INS and !TRG)")%>
sw = StringWriter()
transformer.transform(DOMSource(doc), StreamResult(sw))
output = sw.getBuffer().toString()
extension = "xml"
<% } %>
output = output.encode('utf-8')
stringHandle = io.StringHandle(output);
stringHandle.withFormat(fileFormat);
collections = io.DocumentMetadataHandle();
collections.withCollections(array(["<%=odiRef.getOption("ML_COLLECTION")%>"], String));
writer.add("/<%=odiRef.getTable("ID")%>/" + str(rowCount) + "." + extension, collections, stringHandle);