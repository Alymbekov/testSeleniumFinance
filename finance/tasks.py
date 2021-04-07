from celery.decorators import task
from celery.utils.log import get_task_logger
from time import sleep

from decouple import config
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

from finance import utils
from finance.csv_to_db import get_csv_file_write_to_db

logger = get_task_logger(__name__)

URL = 'http://selenium:4444/wd/hub'


@task(name='selenium_run')
def selenium_run(duration,  title) -> str:
    sleep(duration)
    if config('DOCKER', cast=bool, default=False):
        parse_object = utils.Parser(webdriver.Remote(command_executor=URL,
                                                     desired_capabilities=DesiredCapabilities.CHROME))
    else:
        parse_object = utils.Parser(
            driver=webdriver.Chrome(
                ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
        )
    result = parse_object.get_max_data(
        url=f"https://finance.yahoo.com/quote/{title}/history?p={title}",
        title=title)
    if result:
        write_to_csv.delay(duration=2, title=title)
    return'selenium done'


@task(name='write_to_csv')
def write_to_csv(duration, title) -> str:
    sleep(duration)
    get_csv_file_write_to_db(title)
    return'selenium done'
