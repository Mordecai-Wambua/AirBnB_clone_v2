#!/usr/bin/python3
"""
    Creates and distributes an archive to your web servers.
    Prototype: def deploy():
"""

from fabric.api import put, run, env, local
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['52.91.118.63', '54.175.17.114']


def do_pack():
    """Compresses the web_static folder into a .tgz archive"""
    day = datetime.now().strftime("%Y%m%d%H%M%S")
    if not isdir("versions"):
        local("mkdir versions")
    archive = "versions/web_static_{}.tgz".format(day)
    output = local("tar -czvf {} web_static".format(archive))
    if output.failed:
        return None
    return archive


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


def deploy():
    """Creates ans deploys the archive."""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(archive_path)
