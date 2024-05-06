#!/usr/bin/python3
"""
    Distributes an archive to your web servers.
    prototype: def do_deploy(archive_path):
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['52.91.118.63', '54.175.17.114']


def do_deploy(archive_path):
    """Deploy specified archive to  servers."""
    if not exists(archive_path):
        return False
    try:
        file_N = archive_path.split("/")[-1]
        n = file_N.split(".")[0]

        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')

        run('mkdir -p {}{}/'.format(path, n))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_N, path, n))
        run('rm /tmp/{}'.format(file_N))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, n))
        run('rm -rf {}{}/web_static'.format(path, n))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, n))
        return True
    except Exception:
        return False
