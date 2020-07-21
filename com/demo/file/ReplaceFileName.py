#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/7/20 9:46
# @Author: yuzq
# @File  : FileReplace
import logging
import os
import shutil
from pathlib import Path


class FileReplace:
    logging.basicConfig(level=logging.DEBUG)

    def __init__(self, directory, oldStr, newStr):
        self.__dir = directory
        self.__old_str = oldStr
        self.__new_str = newStr
        self.__files = []

    def get_files(self):
        path = Path(self.__dir)
        self.__get_files(path, self.__files)

    def list_files(self):
        for file in self.__files:
            logging.debug(str(file))

    def list_files_by_tree(self):
        self.show_dir_tree_by_dfs(self.__dir, 0)

    def __get_files(self, path, files=[]):
        if path.exists():
            if path.is_dir():
                for file in path.iterdir():
                    if Path.is_file(file):
                        files.append(file)
                    else:
                        self.__get_files(file, files)
            else:
                files.append(path)
        else:
            logging.debug("文件不存在！")

    def replace_file_name(self):
        for filePath in self.__files:
            filePath = Path(filePath)
            soureName = filePath.name
            targetName = soureName.replace(self.__old_str, self.__new_str)
            # logging.debug("---------源文件--------" + str(filePath))
            targetPath = filePath.with_name(targetName)
            # logging.debug("---------目标文件--------" + str(targetPath))

    def replace_file_content(self):
        for filePath in self.__files:
            filePath = Path(filePath)
            targetContent = ""

            with open(filePath, 'r+') as f:
                content = f.read()
                targetContent = content.replace(self.__old_str, self.__new_str)
            with open(filePath, "w") as fw:
                fw.write(targetContent)
                fw.flush()

    def show_dir_tree_by_dfs(self, path, depth):
        path = Path(path)
        if Path.exists(path):
            if depth == 0:
                logging.info("root:[" + os.path.abspath(path) + "]")

            for item in Path.iterdir(path):

                if (item.is_dir()):
                    logging.info("|------" * depth + "+--" + item.name)
                    self.show_dir_tree_by_dfs(item.parent.joinpath(item), depth + 1)
                else:
                    logging.info("|      " * depth + "---" + item.name)
        else:
            logging.debug("文件不存在！")


if __name__ == '__main__':

    # file = FileReplace("E:\\RDJ-YUZHENQUAN\\Desktop\\linshi\\201\\16\\settlement2", "Settlement","ReceiveAnalyzeByOrg")
    # file.get_files()
    # file.list_files()
    # file.list_files_by_tree()
    # file.replace_file_name()
    # file.replace_file_content()
    entries = os.scandir("E:\\RDJ-YUZHENQUAN\\Desktop\\linshi\\201\\16\\settlement2")
    print(entries)
    entries2 = os.listdir("E:\\RDJ-YUZHENQUAN\\Desktop\\linshi\\201\\16\\settlement2")
    print(entries2)
    f = Path("E:\\RDJ-YUZHENQUAN\\Desktop\\linshi\\201\\16\\settlement2")
    entries3 = f.iterdir()
    print(entries3)

    for entry1 in entries3:
        print(entry1)
        # print(entry2)
        # print(entry3)

    shutil.copy("E:\\RDJ-YUZHENQUAN\\Desktop\\linshi\\201\\16\\settlement2","E:\\RDJ-YUZHENQUAN\\Desktop\\linshi\\201\\16\\settlement3")
    shutil.copy2("E:\\RDJ-YUZHENQUAN\\Desktop\\linshi\\201\\16\\settlement2","E:\\RDJ-YUZHENQUAN\\Desktop\\linshi\\201\\16\\settlement4")