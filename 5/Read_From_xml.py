from xml.dom.minidom import parse, parseString, getDOMImplementation, Node

xml_file = parse("odoo_xml.xml")

template = xml_file.getElementsByTagName("template")
print("Root Tag: ", xml_file.firstChild.tagName)

for template_item in template:
    template_id = template_item.getAttribute("id")

    print()
    print(" Tag Name: ", template_item.tagName, ": ")
    print("    Attribute: id:", template_id)

    for xpath in template_item.childNodes:
        if xpath.nodeType == xpath.ELEMENT_NODE:
            position = xpath.getAttribute("position")

            print()
            print("    Tag Name: ", xpath.tagName)
            print("        Attribute: position: ", position)

            for child_tags in xpath.childNodes:
                if child_tags.nodeType == child_tags.ELEMENT_NODE:

                    if child_tags.tagName == "link":
                        href = child_tags.getAttribute("href").split("/")[-1]

                        print()
                        print("        Tag Name: ", child_tags.tagName)
                        print("           Attribute: href: ", href)
                    else:
                        src = child_tags.getAttribute("src").split("/")[-1]

                        print()
                        print("        Tag Name:", child_tags.tagName)
                        print("           Attribute: src: ", src)
