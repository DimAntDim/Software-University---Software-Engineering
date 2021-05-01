import os

files = {}


def create_report_txt_on_desktop():
    username = os.getlogin()  # Fetch username
    try:
        open(f'C:\\Users\\{username}\\Desktop\\report.txt', 'x')
    except FileExistsError:
        pass


def extract_files_from_directory():
    f = os.scandir("Example")
    for i in f:
        file = i.name
        try:
            extension_index = file.index('.')
        except ValueError:
            continue
        extension = file[extension_index:]
        if extension not in files:
            files[extension] = []
        files[extension].append(file)


def load_data_in_report_file():
    username = os.getlogin()
    try:
        with open(f'C:\\Users\\{username}\\Desktop\\report.txt', 'a') as report_file:
            for file_extension, file_name in sorted(files.items(), key=lambda x: (x[0], x[1])):
                file_ = file_extension
                report_file.write(f"{file_}\n")
                for _ in file_name:
                    report_file.write(f"- - - {''.join(_)}\n")
    except FileNotFoundError:
        print(FileNotFoundError)
    except FileExistsError:
        print(FileExistsError)


create_report_txt_on_desktop()
extract_files_from_directory()
load_data_in_report_file()


