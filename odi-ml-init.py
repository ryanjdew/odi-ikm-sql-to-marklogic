import string
import java.lang as lang
import re

from java.io import *
from java.net import URI;
from javax.xml.parsers import *
from javax.xml.transform import *
from javax.xml.transform.dom import *
from javax.xml.transform.stream import *

from com.marklogic.xcc import *

from org.w3c.dom import *

cs = ContentSourceFactory.newContentSource(URI("xcc://<%=odiRef.getOption("ML_USER")%>:<%=odiRef.getOption("ML_PASSWORD")%>@<%=odiRef.getOption("ML_HOST")%>:<%=odiRef.getOption("ML_PORT")%>"));
session = cs.newSession();
docFactory = DocumentBuilderFactory.newInstance()
builder = docFactory.newDocumentBuilder()
tf = TransformerFactory.newInstance()
transformer = tf.newTransformer()
transformer.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, "yes")
rowCount = 0