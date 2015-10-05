import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../..")
TARGET_DIR = PROJECT_ROOT + "/target"
RESOURCES_DIR = PROJECT_ROOT + "/src/main/resources"

def main():
    print "project root: " + PROJECT_ROOT

    if not os.path.exists(TARGET_DIR):
        os.mkdir(TARGET_DIR)

    root = ET.parse(RESOURCES_DIR + "/html/index.html").getroot()
    ens_parents = root.findall(".//*[@ok_lang='en']/..")
    for ens_parent in ens_parents:
        target = ens_parent.find(".//*[@ok_lang='en']")
#         parent = en.getparent()
        ens_parent.remove(target)

#     root.remove(a)
    print minidom.parseString(ET.tostring(root)).toprettyxml()


    print "hello"

main()
