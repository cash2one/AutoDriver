
try:
    import http.client as http_client
except ImportError:
    import httplib as http_client

import shutil
import socket
import sys
from .firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.extension_connection import ExtensionConnection
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


class WebDriver(RemoteWebDriver):

    # There is no native event support on Mac
    NATIVE_EVENTS_ALLOWED = sys.platform != "darwin"

    def __init__(self, firefox_profile=None, firefox_binary=None, timeout=30,
                 capabilities=None, proxy=None):

        self.binary = firefox_binary
        self.profile = firefox_profile

        if self.profile is None:
            self.profile = FirefoxProfile()

        self.profile.native_events_enabled = (
            self.NATIVE_EVENTS_ALLOWED and self.profile.native_events_enabled)

        if self.binary is None:
            self.binary = FirefoxBinary()

        if capabilities is None:
            capabilities = DesiredCapabilities.FIREFOX

        if proxy is not None:
            proxy.add_to_capabilities(capabilities)

        RemoteWebDriver.__init__(self,
            command_executor=ExtensionConnection("127.0.0.1", self.profile,
            self.binary, timeout),
            desired_capabilities=capabilities,
            keep_alive=True)
        self._is_remote = False

    def quit(self):
        """Quits the driver and close every associated window."""
        try:
            RemoteWebDriver.quit(self)
        except (http_client.BadStatusLine, socket.error):
            # Happens if Firefox shutsdown before we've read the response from
            # the socket.
            pass
        self.binary.kill()
        try:
            shutil.rmtree(self.profile.path)
            if self.profile.tempfolder is not None:
                shutil.rmtree(self.profile.tempfolder)
        except Exception as e:
            print(str(e))

    @property
    def firefox_profile(self):
        return self.profile

    def find_id(self,id_):
        return self.find_element_by_id(id_)
