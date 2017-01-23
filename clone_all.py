# -*- coding: utf-8 -*-
import requests
import commands
import os


OWNER = raw_input('Github user: ')
URL = 'https://api.github.com/users/%s/repos' % OWNER
FILE = '%s_repos.txt' % OWNER


def get_repo_from_api():
    page = 1
    repos = []
    headers = {
        "Authorization": "token <the_token_from_Github>"}

    requests.packages.urllib3.disable_warnings()
    print('Collecting data from Github...')
    while True:
        print('Collecting page %s' % page)
        r = requests.get(URL + '?page=%s' % page, headers=headers)
        if r.ok:
            content = r.json()
            repos += [i['clone_url'] for i in content]
            if len(content) == 30:
                page += 1
                continue
            break
        else:
            print('Failed to connect to Github')
            print('Try again...')
    with open(FILE, 'w') as f:
        for repo in repos:
            f.write(repo + '\n')
    return repos


def get_repo_from_file(file):
    repos = []
    with open(file) as f:
        for line in f:
            repos.append(line.strip())
    return repos


def clone_repo(repos):
    print('There are %s repos.' % len(repos))
    for repo in repos:
        cmd = 'git clone ' + repo
        print(cmd)
        print(commands.getstatusoutput(cmd)[1])


def main():
    if os.path.isfile(FILE):
        repos = get_repo_from_file(FILE)
    else:
        repos = get_repo_from_api()
    clone_repo(repos)


if __name__ == '__main__':
    main()
