import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../..")
TARGET_DIR = PROJECT_ROOT + "/target"
RESOURCES_DIR = PROJECT_ROOT + "/src/main/resources"
RESOURCE_HTML_DIR = RESOURCES_DIR + "/html"

from processor import Processor

class Main:
    
    def main(self):
        print "project root: " + PROJECT_ROOT

        self.make_work_dir()
        processor = Processor()
        
        target_file_paths = self.build_targets()

        for full_path in target_file_paths:
            html = processor.process_html(full_path)
            processed_file_name = full_path.replace(RESOURCE_HTML_DIR + "/", "").replace("/", "_")
            processed_file_path = os.path.join(TARGET_DIR, processed_file_name)
            print "Processed file: " + processed_file_path
            with open(processed_file_path, 'w') as f:
                f.write(html.encode("utf-8"))

    def make_work_dir(self):
        if not os.path.exists(TARGET_DIR):
            os.mkdir(TARGET_DIR)

    def build_targets(self):
        target_file_paths = []
        for dir_name, _subdirs, file_names in os.walk(RESOURCE_HTML_DIR, topdown=False):
            for file_name in file_names:
                extention = os.path.splitext(file_name)[1]
                if extention == ".html":
                    full_path = os.path.join(dir_name, file_name)
                    target_file_paths.append(full_path)
        return target_file_paths

Main().main()
