from xml.etree import ElementTree
import json


def opml_to_dic(file_path):
    final_data = {}
    with open(file_path, 'rt') as f:
        tree = ElementTree.parse(f)
        root = tree.getroot()
        folder_names = []
        for child in root[1]:
            folder_names.append(child)
        for folder_name in folder_names:
            rss_data_folder_wise = []
            for rss_data in folder_name:
                rss_data_folder_wise.append(rss_data.attrib)
            final_data[folder_name.attrib['text']] = rss_data_folder_wise
    return final_data


def write_json(file_path, output):
    dic = opml_to_dic(file_path)
    with open(output, "w") as output:
        json.dump(dic, output, indent=4, sort_keys=True)


def ompl_to_json(path, filename):
    path = str(path + filename)
    write_json(path, "./res/temp.json")
    print(str(__name__) + " done!")
