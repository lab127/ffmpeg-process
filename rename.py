import os
import re


def rename_em(loc, new_loc):
    for f in os.listdir(loc):
        file_name, ext = os.path.splitext(f)
        res_name = re.sub(r"(\[.*\]|\(.*\))(.*)", r"\2", file_name)
        res_name = re.sub(r"\s{2,}", " ", res_name)
        res_name = res_name.strip()
        old_name = f"{loc}/{file_name}{ext}"
        new_name = f"{new_loc}/{res_name}{ext}"
        if len(res_name) >= 10 and not os.path.isfile(new_name):
            os.rename(old_name, new_name)


rename_em("old-dir", "new-dir")
