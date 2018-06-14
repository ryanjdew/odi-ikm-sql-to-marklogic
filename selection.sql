<%for (int i=odiRef.getDataSetMin(); i <= odiRef.getDataSetMax(); i++){%>
<%=odiRef.getDataSet(i, "Operator")%>
select  <%=odiRef.getPop("DISTINCT_ROWS")%>
  <%=odiRef.getColList(i, "", "[EXPRESSION]\t[ALIAS_SEP] [CX_COL_NAME]", ",\n\t", "", "")%>
from  <%=odiRef.getFrom(i)%>
where (1=1)
<%=odiRef.getFilter(i)%>

<% if(odiRef.getOption("IS_HEIRARCHICAL").equals("YES")) { %>
<% if(odiRef.getOption("START_WITH").equals("")) { %>
<%} else {%>
START WITH <%=odiRef.getOption("START_WITH")%>
<%}%>

<% if (odiRef.getOption("IS_NOCYCLE").equals("YES")) {%>
CONNECT BY NOCYCLE
<%} else {%>
CONNECT BY 
<%}%>

PRIOR
<%=odiRef.getOption("CONNECT_OPTION")%>
<%}%>
<%=odiRef.getJrnFilter(i)%>
<%=odiRef.getJoin(i)%>
<%=odiRef.getGrpBy(i)%>
<%=odiRef.getHaving(i)%>
<%}%>