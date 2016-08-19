from java.lang import String
from com.marklogic.xcc import *
from jarray import array

rowCount = rowCount + 1
<% if (odiRef.getOption("FORMAT").equals("JSON")) { %>
output = "{ "
<%=odiRef.getColList("", "output = output + \u0022\\\u0022[CX_COL_NAME]\\\u0022 : \\\u0022#[CX_COL_NAME]\\\u0022", ",\u0022\n", "\u0022", "(INS and !TRG)")%>
output = output + "}"
extension = "json"
createOptions = ContentCreateOptions.newJsonInstance()
<% } else { %>
doc = builder.newDocument()
results = doc.createElement("<%=odiRef.getOption("XML_ROOT")%>")
doc.appendChild(results)
<%=odiRef.getColList("", "node = doc.createElement(\u0022[CX_COL_NAME]\u0022)\nnode.appendChild(doc.createTextNode(\u0022#[CX_COL_NAME]\u0022))\nresults.appendChild(node)", "\n", "", "(INS and !TRG)")%>
writer = StringWriter()
transformer.transform(DOMSource(doc), StreamResult(writer))
output = writer.getBuffer().toString()
extension = "xml"
createOptions = ContentCreateOptions.newXmlInstance()
<% } %>
createOptions.setCollections(array(["<%=odiRef.getOption("ML_COLLECTION")%>"], String))
session.insertContent(ContentFactory.newContent("/<%=odiRef.getTable("ID")%>/" + str(rowCount) + "." + extension, output, createOptions))