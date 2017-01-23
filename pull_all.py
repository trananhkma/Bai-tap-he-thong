# -*- coding: utf-8 -*-
import requests
import commands
from os import chdir, getcwd, listdir, path

def get_folders(mypath=None):
    if not mypath:
        mypath = getcwd()
    return [path.join(mypath, f) for f in listdir(mypath) if path.isdir(path.join(mypath, f))]


def pull_repo(repo):
    print('Pulling %s' % repo)
    chdir(repo)
    print commands.getstatusoutput('git checkout .')[1]
    print commands.getstatusoutput('git checkout master')[1]
    print commands.getstatusoutput('git pull origin master')[1]


def main():
    folders = get_folders()
    for folder in folders:
        repos = get_folders(folder)
        for repo in repos:
            pull_repo(repo)


if __name__ == '__main__':
    main()
