import os

def find_files(suffix, path):
    list_found_files = []
    list_found_files = _find_files_recursion(suffix, path)
    return list_found_files

def _find_files_recursion(suffix, path):
    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
        else:
            return None
    elif os.path.isdir(path):
        list_found_files = []
        file_list = os.listdir(path)
        for file in file_list:
            next_path = os.path.join(path, file)
            result = _find_files_recursion(suffix, next_path)
            if result is not None:
                list_found_files = list_found_files + result
        return list_found_files

result = find_files(".h", "./testdir")

print(result)

