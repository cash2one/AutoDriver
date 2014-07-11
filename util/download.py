__author__ = 'Administrator'

import os
import shutil
import sys
import tempfile
import zipfile
import optparse
import subprocess
import platform
import textwrap
import contextlib

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

try:
    from site import USER_SITE
except ImportError:
    USER_SITE = None

DEFAULT_VERSION = "5.3"
DEFAULT_URL = "https://pypi.python.org/packages/source/s/setuptools/"

def _clean_check(cmd, target):
    """
    Run the command to download target. If the command fails, clean up before
    re-raising the error.
    """
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError:
        if os.access(target, os.F_OK):
            os.unlink(target)
        raise

def download_file_powershell(url, target):
    """
    Download the file at url to target using Powershell (which will validate
    trust). Raise an exception if the command cannot complete.
    """
    target = os.path.abspath(target)
    ps_cmd = (
        "[System.Net.WebRequest]::DefaultWebProxy.Credentials = "
        "[System.Net.CredentialCache]::DefaultCredentials; "
        "(new-object System.Net.WebClient).DownloadFile(%(url)r, %(target)r)"
        % vars()
    )
    cmd = [
        'powershell',
        '-Command',
        ps_cmd,
    ]
    _clean_check(cmd, target)

def download_file_wget(url, target):
    cmd = ['wget', url, '--quiet', '--output-document', target]
    _clean_check(cmd, target)

def download_file_curl(url, target):
    cmd = ['curl', url, '--silent', '--output', target]
    _clean_check(cmd, target)

def download_file_insecure(url, target):
    """
    Use Python to download the file, even though it cannot authenticate the
    connection.
    """
    src = urlopen(url)
    try:
        # Read all the data in one block.
        data = src.read()
    finally:
        src.close()

    # Write all the data in one block to avoid creating a partial file.
    with open(target, "wb") as dst:
        dst.write(data)

download_file_insecure.viable = lambda: True

def get_best_downloader():
    downloaders = (
        download_file_powershell,
        download_file_curl,
        download_file_wget,
        download_file_insecure,
    )
    viable_downloaders = (dl for dl in downloaders if dl.viable())
    return next(viable_downloaders, None)

def download_setuptools(version=DEFAULT_VERSION, download_base=DEFAULT_URL,
        to_dir=os.curdir, delay=15, downloader_factory=get_best_downloader):

    # making sure we use the absolute path
    to_dir = os.path.abspath(to_dir)
    zip_name = "setuptools-%s.zip" % version
    url = download_base + zip_name
    saveto = os.path.join(to_dir, zip_name)
    if not os.path.exists(saveto):

        downloader = downloader_factory()
        downloader(url, saveto)
    return os.path.realpath(saveto)

class ContextualZipFile(zipfile.ZipFile):
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def __new__(cls, *args, **kwargs):
        """
        Construct a ZipFile or ContextualZipFile as appropriate
        """
        if hasattr(zipfile.ZipFile, '__exit__'):
            return zipfile.ZipFile(*args, **kwargs)
        return super(ContextualZipFile, cls).__new__(cls)


@contextlib.contextmanager
def archive_context(filename):
    # extracting the archive
    tmpdir = tempfile.mkdtemp()
    old_wd = os.getcwd()
    try:
        os.chdir(tmpdir)
        with ContextualZipFile(filename) as archive:
            archive.extractall()

        # going in the directory
        subdir = os.path.join(tmpdir, os.listdir(tmpdir)[0])
        os.chdir(subdir)
        yield

    finally:
        os.chdir(old_wd)
        shutil.rmtree(tmpdir)

def main():
    """Install or upgrade setuptools and EasyInstall"""
    options = _parse_args()
    archive = download_setuptools(
        version=options.version,
        download_base=options.download_base,
        downloader_factory=options.downloader_factory,
    )
    return _install(archive, _build_install_args(options))

if __name__ == '__main__':
    sys.exit(main())