class Parser:
    """
    Class for get data
    and download csv
    """
    def __init__(self, driver):
        self.driver = driver

    def get_page(self, url) -> str:
        driver = self.driver
        return driver.get(url)

    def get_page_data(self, name_of_class, search_item) -> None:
        url = "https://finance.yahoo.com/?guccounter=1"
        self.get_page(url=url)
        search_box = self.driver.find_element_by_name(name_of_class)
        search_box.send_keys(search_item)
        # time.sleep(2)
        search_box.submit()

    def get_max_data(self, url, download_url, title="ZUO") -> dict:
        self.get_page_data(name_of_class="yfin-usr-qry", search_item=title)
        self.driver.get(url)
        # time.sleep(2)
        self.driver.get(download_url)
        return {"msg": "successfully done selenium parse"}