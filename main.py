import git
from config import repo_url
from updates import print_updates, update
import os
import sys

local_head = git.Repo(search_parent_directories=True).head.object.hexsha
remote_head = git.cmd.Git().ls_remote(repo_url, heads=True)
_startup_cwd = os.getcwd()

# If they don't match then there are updates
if local_head != remote_head:
    print('[!] Update is available!')
    if input("[?] Do you want to update? (y/n): ").lower() == 'y':
        update()
        args = sys.argv[:]

        args.insert(0, sys.executable)
        if sys.platform == 'win32':
            args = ['"%s"' % arg for arg in args]

        os.chdir(_startup_cwd)
        os.execv(sys.executable, args)
