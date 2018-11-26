import os

CURRENT_DIR = os.path.dirname(__file__)


def copy_file_content(src_path, dst_path, remove_char=""):
    with open(src_path) as src_file:
        with open(dst_path, "w") as dst_file:
            for line in src_file:
                dst_file.write(line.replace(remove_char, ""))


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


with open("/var/log/syslog") as src_file:
    for line in src_file:
        if "systemd" in line:
            print(line.strip())


src_file = open("/var/log/syslog")
for line in src_file:
    if "systemd" in line:
        print(line.strip())
src_file.close()

copy_file_content(__file__, os.path.join(CURRENT_DIR, "%s_striped" % __file__), "\n")
