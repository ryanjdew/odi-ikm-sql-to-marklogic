request = session.newAdhocQuery ("xdmp:delete-collection(\"<%=odiRef.getOption("ML_COLLECTION")%>\")")
session.submitRequest(request)