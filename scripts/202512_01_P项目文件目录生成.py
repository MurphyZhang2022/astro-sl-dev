# -*- coding: utf-8 -*-
# @Time     : 2025/12/17 00:45
# @Author   : Zack Murphy
# @File     : 202512_01_P项目文件目录生成.py

import os

def create_project_dir(root_dir):
    """
    root_dir:  要创建的项目路径
    """

    dirs = {
        "data": ["raw", "processed"],
        "scripts": [],
        "notebooks": [],
        "models": [],
        "results": []
    }

    files = [
        "environment.yml",
        "requirements.txt",
        ".gitignore",
        "README.md",
        "workflow.txt"
    ]

    # 创建 README.md 内容
    workflow_content = []
    workflow_content.append("# workflow 流程说明\n\n")
    workflow_content.append("1.环境与工具：\n")
    workflow_content.append(
        "- *Conda environment*：astro-ssl-dev。\n")
    workflow_content.append(
        "- *PyCharm*：编写训练、推理脚本。\n")
    workflow_content.append(
        "- *Jupyter Notebook*：数据探索、可视化、快速实验。\n\n")
    workflow_content.append("2.数据流：\n")
    workflow_content.append(
        "- *PyCharm*：data/raw → scripts/train_xxx.py → models/\n")
    workflow_content.append(
        "- *Jupyter Notebook*：data/raw → notebooks/00_exploration.ipynb → results/\n")
    workflow_content.append(
        "- raw：data/raw → 原始 FITS / 图像，不 push\n")
    workflow_content.append(
        "- processed：经过裁剪 / 归一化的训练数据，可推送 GitHub\n\n")
    workflow_content.append("3.代码管理：\n")
    workflow_content.append(
        "- scripts + notebooks → GitHub 管理\n")
    workflow_content.append(
        "- models + results → 本地或科研服务器备份，不 push\n\n")

    workflow_content.append("4.开发循环：\n")
    workflow_content.append(
        "- PyCharm scripts      ↔  GitHub  #在 PyCharm 写标准化训练脚本,GitHub 管理脚本与 notebook 版本\n")
    workflow_content.append(
        "- train/test → models → inference → results\n")
    workflow_content.append(
        "- notebooks (exploration / visualization  #notebook 快速验证模型效果\n\n")

    workflow_content.append("## 目录结构\n\n")


    # 创建文件夹目录及二级目录
    for main_dir, subdirs in dirs.items():
        main_dir_path = os.path.join(root_dir, main_dir)
        os.makedirs(main_dir_path, exist_ok=True)
        for subdir in subdirs:
            subdir_path = os.path.join(main_dir_path, subdir)
            os.makedirs(subdir_path, exist_ok=True)

    # 创建文件
    for file in files:
        file_path = os.path.join(root_dir, file)
        if not os.path.exists(file_path) and "workflow" in file:
            print(file_path)
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(workflow_content)
        else:
            with open(file_path, "w", encoding="utf-8"):
                pass #创建空文件



    print("所有的文件夹及文件已创建成功")

if __name__ == "__main__":
    folder_dir = "E:\PProjects/astro-sl-dev"
    create_project_dir(folder_dir)