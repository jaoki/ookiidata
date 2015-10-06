import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
from xml.dom import minidom

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../..")
TARGET_DIR = PROJECT_ROOT + "/target"
RESOURCES_DIR = PROJECT_ROOT + "/src/main/resources"
RESOURCE_HTML_DIR = RESOURCES_DIR + "/html"

def replace_to_jp(root):
    lang_roots = root.findall(".//*[@ok_lang='root']")
    for lang_root in lang_roots:
        en = lang_root.find("*[@ok_lang='en']")
        jp = lang_root.find("*[@ok_lang='jp']")
        if jp is not None:
            lang_root.remove(en)
#             ens_parent.append(jp)
#         parent = en.getparent()



def process_html(file_path):
    print "processing " + file_path
    try:
        root = ET.parse(file_path).getroot()
    except ParseError:
        print "file " + file_path + " got a parse error"
        raise
    replace_to_jp(root)
    return minidom.parseString(ET.tostring(root)).toprettyxml()


def make_work_dir():
    if not os.path.exists(TARGET_DIR):
        os.mkdir(TARGET_DIR)

def main():
    print "project root: " + PROJECT_ROOT

    make_work_dir()

    for dir_name, _subdirs, file_names in os.walk(RESOURCE_HTML_DIR, topdown=False):
        for file_name in file_names:
            extention = os.path.splitext(file_name)[1]
            if extention == ".html":
                full_path = os.path.join(dir_name, file_name)
                html = process_html(full_path)
                processed_file_name = full_path.replace(RESOURCE_HTML_DIR + "/", "").replace("/", "_")
                processed_file_path = os.path.join(TARGET_DIR, processed_file_name)
                print "Processed file: " + processed_file_path
                with open(processed_file_path, 'w') as f:
                    f.write(html.encode("utf-8"))

main()
