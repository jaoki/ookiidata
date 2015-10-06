import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
from xml.dom import minidom

class Processor:
    def replace_to_jp(self, root):
        lang_roots = root.findall(".//*[@ok_lang='root']")
        for lang_root in lang_roots:
            en = lang_root.find("*[@ok_lang='en']")
            jp = lang_root.find("*[@ok_lang='jp']")
            if jp is not None:
                lang_root.remove(en)

    def process_html(self, file_path):
        print "processing " + file_path
        try:
            root = ET.parse(file_path).getroot()
        except ParseError:
            print "file " + file_path + " got a parse error"
            raise
        self.replace_to_jp(root)
        return minidom.parseString(ET.tostring(root)).toprettyxml()


