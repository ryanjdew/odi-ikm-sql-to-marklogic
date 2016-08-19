<%for (int i=odiRef.getDataSetMin(); i <= odiRef.getDataSetMax(); i++){%>
<%=odiRef.getDataSet(i, "Operator")%>
select	<%=odiRef.getPop("DISTINCT_ROWS")%>
	<%=odiRef.getColList(i, "", "[EXPRESSION]\t[ALIAS_SEP] [CX_COL_NAME]", ",\n\t", "", "")%>
from	<%=odiRef.getFrom(i)%>
where	(1=1)
<%=odiRef.getFilter(i)%>
<%=odiRef.getJrnFilter(i)%>
<%=odiRef.getJoin(i)%>
<%=odiRef.getGrpBy(i)%>
<%=odiRef.getHaving(i)%>
<%}%>
