from celery.decorators import task
from celery.utils.log import get_task_logger
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from finance import utils
from finance.csv_to_db import get_csv_file_write_to_db

logger = get_task_logger(__name__)


@task(name='selenium_run')
def selenium_run(duration, download_url, title) -> str:
    sleep(duration)
    parse_object = utils.Parser(
        driver=webdriver.Chrome(
            ChromeDriverManager().install()
        )
    )
    result = parse_object.get_max_data(
        url=f"https://finance.yahoo.com/quote/{title}/history?p={title}",
        download_url=download_url,
        title=title)
    if result:
        write_to_csv.delay(duration=2, title=title)
    return'selenium done'


@task(name='write_to_csv')
def write_to_csv(duration, title) -> str:
    sleep(duration)
    get_csv_file_write_to_db(title)
    return'selenium done'
