#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages, os

changelog = "debian/changelog"
if os.path.exists(changelog):
    head = open(changelog).readline()
    try:
        version = head.split("(")[1].split(")")[0]
    except:
        print("debian/changelog format is wrong for get version")
        version = ""
    f = open("parduspackageinstaller/Version.py", "w")
    f.write('version = "%s"\n' % version)
    f.close()

data_files = [
    ("/usr/share/applications", ["tr.org.pardus.package-installer.desktop"]),
    ("/usr/share/locale/tr/LC_MESSAGES", ["po/tr/pardus-package-installer.mo"]),
    ("/usr/share/pardus/pardus-package-installer", ["ui/MainWindow.glade", "icon.svg", "actions.py"]),
    ("/usr/bin", ["pardus-package-installer-action"]),
    ("/usr/share/polkit-1/actions", ["tr.org.pardus.pkexec.pardus-package-installer.policy"])
]

setup(
    name="Pardus Package Installer",
    version=version,
    packages=find_packages(),
    scripts=["pardus-package-installer"],
    install_requires=["PyGObject"],
    data_files=data_files,
    author="Fatih Altun",
    author_email="fatih.altun@pardus.org.tr",
    description="Pardus Deb Package Installer.",
    license="GPLv3",
    keywords="deb package installer",
    url="https://www.pardus.org.tr",
)
