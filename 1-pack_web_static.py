#!/usr/bin/python3
"""Script that generates a .tgz archive from webstatic folder contents."""

from datetime import datetime
from fabric.api import local
from os.path import isdir


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
