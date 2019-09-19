import os
import re
import subprocess
import csv

EXTRACTED_FOLDER = "./extracted_folders/"
CSV_FOLER = "./csv_files/"
HEADER_FILE = "column_headers.tsv"
DATA_FILE = "hit_data.tsv"


def extract_tar_files_from(tar_folderpath):
        list_of_files = [filepath for filepath in os.listdir(tar_folderpath) if re.search("(.*)\.zip", filepath)]
        for file_with_ext in list_of_files:
                file_without_ext = file_with_ext[:-4]
                import pdb
                pdb.set_trace()
                new_directory = "{0}{1}".format(EXTRACTED_FOLDER, file_without_ext)
                if not os.path.exists(new_directory):
                        os.makedirs(new_directory)
                tar_file_path = "{0}/{1}".format(tar_folderpath, file_with_ext)
                extracted = os.system('unzip {0} -d {1}'.format(tar_file_path, new_directory))


def create_csv_file():
        list_of_extracted_folders = [filepath for filepath in os.listdir(EXTRACTED_FOLDER) if os.path.isdir("{0}{1}".format(EXTRACTED_FOLDER, filepath))]
        for extracted_folder in list_of_extracted_folders:
                extracted_folder_path = "{0}{1}".format(EXTRACTED_FOLDER, extracted_folder)
                header_file = None
                data_file = None
                for tsv_filepath in ["{0}/{1}".format(extracted_folder_path, tsv) for tsv in os.listdir(extracted_folder_path)]:
                        if HEADER_FILE in tsv_filepath:
                                header_file = tsv_filepath
                        elif DATA_FILE in tsv_filepath:
                                data_file = tsv_filepath
                header_list_list = list()
                data_list_list = list()

                with open(header_file, 'r') as csv_hfile:
                        headerreader = csv.reader(csv_hfile, delimiter='\t', quotechar='"')
                        for row in headerreader:
                                header_list_list.append(row)

                with open(data_file, 'r') as csv_dfile:
                        data_reader = csv.reader(csv_dfile, delimiter = '\t', quotechar = '"')
                        for row in data_reader:
                                data_list_list.append(row)

                with open("{0}{1}.tsv".format(CSV_FOLER, extracted_folder), "w") as final_file:
                        file_writer = csv.writer(final_file, delimiter = "\t", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        file_writer.writerow(header_list_list[0])

                        for data_row in data_list_list:
                                file_writer.writerow(data_row)


if __name__ == '__main__':
        extract_tar_files_from(os.environ.get('COMPRESSED_FILES_FOLDER'))
        print (os.environ.get('COMPRESSED_FILES_FOLDER'))
        create_csv_file()
