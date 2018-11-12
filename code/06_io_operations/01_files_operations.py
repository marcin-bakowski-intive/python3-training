import os

CURRENT_DIR = os.path.dirname(__file__)


def get_non_empty_lines(file_path):
    content = []
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            if line:
                content.append(line)
    return content


def save_file_content(file_path, lines):
    lines_num = len(lines)
    lines = ["%s\n" % line if idx + 1 < lines_num else line for idx, line in enumerate(lines)]
    with open(file_path, "w") as f:
        f.writelines(lines)


def copy_non_empty_lines(src_file_path, dst_file_path):
    lines = get_non_empty_lines(src_file_path)
    save_file_content(dst_file_path, lines)


copy_non_empty_lines(os.path.join(CURRENT_DIR, "..", "..", "README.md"), "output.txt")
