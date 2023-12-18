from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from dotenv import load_dotenv
import os
"""
This class is to sensitive configuation
details for other parts of your application

Use this app to retrive things such as
    * API keys
    * Database connections
    * etc
"""
class Config():
    def __init__(self):
        load_dotenv()

    def get_model_api_key(self):
        return os.getenv("MODEL_API_TOKEN")

    def connect_web_proxy(self):
        """
        returns selenimum driver with webproxy connection
        """
        AUTH = f'{os.getenv("USER_REMOTE_PROXY")}:{os.getenv("PASS_REMOTE_PROXY")}:'
        SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'
        sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
        driver = Remote(sbr_connection, options=ChromeOptions())
        return driver