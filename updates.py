import os
from config import repo_url

def print_updates():
    # get the remote updates.txt file
    with open('updates.txt') as updates:
        updates = updates.read().split('#')
        for u in updates:
            print(f'- {u}')

def update():
    print('Fetching latest update...')
    os.system(f'git fetch --all --quiet')
    print('Updating...')
    os.system(f'git reset --hard origin/master --quiet')