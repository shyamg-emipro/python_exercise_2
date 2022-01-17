from xml.dom.minidom import getDOMImplementation

impl = getDOMImplementation()

newdoc = impl.createDocument(None, "some_tag", None)
top_element = newdoc.documentElement
text = newdoc.createTextNode('Some textual content.')
top_element.appendChild(text)

save_path_file = "gfg.xml"
xml_str = newdoc.toprettyxml(indent="\t")
with open(save_path_file, "w") as f:
    f.write(xml_str)
