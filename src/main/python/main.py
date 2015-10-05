import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../..")
TARGET_DIR = PROJECT_ROOT + "/target"
RESOURCES_DIR = PROJECT_ROOT + "/src/main/resources"

def replace_to_jp(root):
    lang_roots = root.findall(".//*[@ok_lang='root']")
    for lang_root in lang_roots:
        en = lang_root.find("*[@ok_lang='en']")
        jp = lang_root.find("*[@ok_lang='jp']")
        if jp is not None:
            lang_root.remove(en)
#             ens_parent.append(jp)
#         parent = en.getparent()


def main():
    print "project root: " + PROJECT_ROOT

    if not os.path.exists(TARGET_DIR):
        os.mkdir(TARGET_DIR)

    root = ET.parse(RESOURCES_DIR + "/html/index.html").getroot()
    replace_to_jp(root)
#     ens_parents = root.findall(".//*[@ok_lang='en']/..")
#     for ens_parent in ens_parents:
#         target = ens_parent.find("*[@ok_lang='en']")
# #         parent = en.getparent()
#         ens_parent.remove(target)

#     root.remove(a)
    html = minidom.parseString(ET.tostring(root)).toprettyxml()
    with open(TARGET_DIR + '/index.html', 'w') as the_file:
        the_file.write(html.encode("utf-8"))


    print "hello"

main()
