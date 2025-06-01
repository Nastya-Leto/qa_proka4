from selenium.webdriver.remote.webelement import WebElement


class TableHandler:
    _TABLE_LOCATOR = ('xpath', "//table")
    _ROW_LOCATOR = ('xpath', './/tbody//tr')
    _CELL_LOCATOR = ('xpath', ".//td")
    _TITLE_CELL_LOCATOR = ('xpath', "//table/thead//th")
    _BUTTON_ACTION_MENU_LOCATOR = ('xpath', ".//button[@type='button']")
    _DOWNLOAD_BUTTON_LOCATOR = ('xpath', "//button[text()='Скачать']")

    def init(self, driver):
        self.driver = driver

    @property
    def _table(self) -> WebElement:  # получить таблицу
        return self.driver.find_element(*self._TABLE_LOCATOR)

    @property
    def _rows(self) -> list[WebElement]:  # получить все строки
        table = self._table
        return table.find_elements(*self._ROW_LOCATOR)

    def row_count(self):
        return len(self._rows)  # получить кол-во строк в таблице

    def get_cell_content(self, row_number, column_number):
        row = self._rows[row_number - 1]  # из списка строк получаем нужную
        cell = row.find_elements(*self._CELL_LOCATOR)[
            column_number - 1]  # в нужной строке находим все ячейки, и выбираем нужную ячейку
        return cell.text

    def get_list_cell_content_in_title(self):
        return [cell.text for cell in self._table.find_elements(*self._TITLE_CELL_LOCATOR)]
        # возвращаем список заголовков из таблицы

    def get_row_content(self, row_number):
        row = self._rows[row_number - 1]  # из списка строк получаем нужную
        return [cell.text for cell in row.find_elements(*self._CELL_LOCATOR)]
        # возвращаем список всех ячеек из нужной строки

    def get_row_content_2(self, row_number):
        row = self._rows[row_number - 1]  # из списка строк получаем нужную
        list_cell_texts = []
        for cell in row.find_elements(*self._CELL_LOCATOR):
            list_cell_texts.append(cell.text)
        return list_cell_texts

    def get_column_content(self, column_number):
        column_content = []
        for row in self._rows:  # перебираем ряд по списку рядов
            cells = row.find_elements(*self._CELL_LOCATOR)  # внутри ряда находим все ячейки
            column_content.append(cells[column_number - 1].text)  # добавляем текст из ячейки по номеру столбца
        return column_content

    def get_content_cell_in_title(self, title):
        for index, cell in enumerate(self.get_list_cell_content_in_title(),
                                     start=1):  # берем индекс, ячейку и идем по списку заголовков
            if title in cell:  # если нужный заголовок равен тексту из ячейки
                return self.get_column_content(index)  # возвращаем текст из ячейки
        raise ValueError(f'Колонка с заголовком {title}не найдена')

    def get_index_column_in_title(self, title):
        for index, cell in enumerate(
                self.get_list_cell_content_in_title()):  # берем индекс, ячейку и идем по списку заголовков
            if title == cell:  # если нужный заголовок равен тексту из ячейки
                return index  # возвращаем индекс
        raise ValueError(f'Колонка с заголовком {title}не найдена')

    def click_button_action_menu(self, row_number):
        row = self._rows[row_number - 1]  # из списка строк получаем нужную
        menu_button = row.find_elements(*self._CELL_LOCATOR)[0].find_element(*self._BUTTON_ACTION_MENU_LOCATOR)
        # внутри строки находим все ячейки, берем с нулевым индексов, внутри этой ячейки находим кнопку меню
        menu_button.click()

    def download_button(self):
        index_title = self.get_index_column_in_title('Статус')  # получаем индекс столбца с нужным названием

        for row_number, row in enumerate(self._rows, start=1): # перебираем номер строки и строку
            cells = row.find_elements(*self._CELL_LOCATOR) # в строке находим все ячейки
            if cells[index_title].text in 'Отправлено в ФНС': # если в ячейке с индексом, полученным на шаге 1, есть нужный текст
                self.click_button_action_menu(row_number) #то каликам на меню
                self.driver.find_element(*self._DOWNLOAD_BUTTON_LOCATOR).click() # кликаем на кнопку скачивания
                return
        raise AssertionError('Не найдена строка со статусом "Отправлено в ФНС"')
