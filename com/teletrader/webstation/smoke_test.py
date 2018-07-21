import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from com.teletrader.webstation.elements_and_data import Elements,Data


class SmokeTest(unittest.TestCase):

    # Navigation buttons
    market_button = By.CSS_SELECTOR, ".navigation-vertical [href='securities_overview.aspx']"
    currencies_button = By.CSS_SELECTOR, ".navigation-vertical [href='currencies_Currencies.aspx']"
    commodities_button = By.CSS_SELECTOR, ".navigation-vertical [href='commodities.aspx']"
    fixed_income_button = By.CSS_SELECTOR, ".navigation-vertical [href='bonds_governmentyields.aspx']"
    funds_button = By.CSS_SELECTOR, ".navigation-vertical [href='funds_topperformerOverview.aspx']"
    futures_button = By.CSS_SELECTOR, ".navigation-vertical [href='funds_topperformerOverview.aspx']"
    news_button = By.CSS_SELECTOR, "[class*='navigation'][href*='news']"
    calendar_button = By.CSS_SELECTOR, ".navigation-vertical [href*='company_calendar']"
    analyzer_button = By.CSS_SELECTOR, ".navigation-vertical [href='analyzer.aspx']"
    portfolio_button = By.CSS_SELECTOR, ".navigation-vertical [href='personal_portfolioDetail.aspx']"
    alert_button = By.CSS_SELECTOR, ".navigation-vertical [href='personal_notifications.aspx']"
    economic_data_button = By.CSS_SELECTOR, ".navigation-vertical [href='economic_calendar.aspx']"
    trump_effect_button = By.CSS_SELECTOR, ".navigation-vertical [href='trump_effect.aspx']"
    back_tester_button = By.CSS_SELECTOR, ".navigation-vertical [href='portfolio_backtester.aspx']"
    screener_button = By.CSS_SELECTOR, ".navigation-vertical [href='screener_overview.aspx']"
    etf_button = By.CSS_SELECTOR, ".navigation-vertical [href='funds_etfOverview.aspx']"
    real_time_button = By.CSS_SELECTOR, ".navigation-vertical [href='realtime_Indications.aspx']"

    # Deatail page headers
    market_header = By.CSS_SELECTOR, ".main-pages-header.markets"

    # Methods
    def change_region_germany(self):
        boolean_funds_visible = self.driver.find_element(*self.funds_button).is_selected()
        region_box = self.driver.find_element(*self.region_box)
        select_region = Select(region_box)
        if not boolean_funds_visible:
            self.driver.find_element(*self.user_button).click()
            self.driver.find_element(*self.account_settings).click()
            select_region.select_by_value("DE")

    def is_eula_selected(self):
        boolean_eula = self.driver.find_element(*self.eula_xpath).is_selected()
        if not boolean_eula:
            self.driver.find_element(*self.eula_css).click()

    def login_method(self):
        self.driver.find_element(*self.username).clear()
        self.driver.find_element(*self.username).send_keys(self.str_username)
        self.driver.find_element(*self.password).send_keys(self.str_password)
        self.is_eula_selected()
        self.driver.find_element(*self.login).click()

    # TEST
    def test(self):
        # Instance of Chrome browser
        driver = webdriver.Chrome()
        driver.maximize_window()

        # Opens test branch
        driver.get(Data.base_url)
        # Test Case: Assert Title is TeleTrader WebStation
        assert Data.base_title == driver.title
        # Test Case: Uncheck eula
        driver.find_element(*Elements.username).send_keys(Data.str_username)
        driver.find_element(*Elements.password).send_keys(Data.str_password)
        driver.find_element(*Elements.login_button).click()
        assert Data.error_accept_eula == driver.find_element(*Elements.error_container).text
        '''
        # Test Case: Successful login
        self.login_method()
        # Test Outcome: Assert logo is_displayed
        assert self.driver.find_element(*self.logo_ws).is_displayed()

        # Test Case: Logout
        self.driver.find_element(*self.user_button).click()
        self.driver.find_element(*self.logout).click()
        # Test Outcome: Login page should appear with empty username and password text box.
        # „EULA“ and „Stay logged in“ are selected.
        self.driver.implicitly_wait(10)
        
        assert self.driver.find_element(*self.eula_xpath).is_selected()
        assert self.driver.find_element(*self.auto_login).is_selected()
        
        # NAVIGATION BUTTONS

        # Market button
        self.login_method()
        self.driver.find_element(*self.market_button).click()
        #Test Outcome:
        assert self.driver.find_element(*self.market_header).is_displayed()
        # Currencies button:
        self.driver.find_element(*self.currencies_button).click()
        # Test Outcome
        #assert self.driver.find_element(*self.currencies_header).is_displayed()
        # Commodities button
        self.driver.find_element(*self.currencies_button).click()
        # Test Outcome
        # assert self.driver.find_element(*self.currencies_header).is_displayed()
        # Fixed Income button
        self.driver.find_element(*self.fixed_income_button).click()
        # Test Outcome
        # assert self.driver.find_element(*self.currencies_header).is_displayed()
        # Funds button
        self.change_region_germany()
        self.driver.find_element(*self.funds_button).click()
        # Test Outcome
        # assert self.driver.find_element(*self.currencies_header).is_displayed()
        # Futures button
        self.driver.find_element(*self.futures_button).click()
        # Test Outcome
        # assert self.driver.find_element(*self.currencies_header).is_displayed()
        # News button
        self.driver.find_element(*self.news_button).click()
        # Test Outcome
        # assert self.driver.find_element(*self.currencies_header).is_displayed()
        # Calendar button
        self.driver.find_element(*self.calendar_button).click()
        # Test Outcome
        # assert self.driver.find_element(*self.currencies_header).is_displayed()
        # Analyzer button
        self.driver.find_element(*self.analyzer_button).click()
        # Test Outcome
        # assert self.driver.find_element(*self.currencies_header).is_displayed()
        # Portfolio button
        self.driver.find_element(*self.portfolio_button).click()
        # Test Outcome
        # assert self.driver.find_element(*self.currencies_header).is_displayed()
        # Alert button
        self.driver.find_element(*self.alert_button).click()
        # Test Outcome
        # assert self.driver.find_element(*self.currencies_header).is_displayed()
        # Economic Data button
        self.driver.find_element(*self.economic_data_button).click()
        # Test Outcome
        # assert self.driver.find_element(*self.currencies_header).is_displayed()
        # Trump Effect button
        self.driver.find_element(*self.trump_effect_button).click()
        # Test Outcome
        # assert self.driver.find_element(*self.currencies_header).is_displayed()
        # Smart Beck Tester button
        self.driver.find_element(*self.back_tester_button).click()
        # Test Outcome
        # assert self.driver.find_element(*self.currencies_header).is_displayed()
        # Screener Button
        self.driver.find_element(*self.screener_button).click()
        # Test Outcome
        # assert self.driver.find_element(*self.currencies_header).is_displayed()
        # ETF button
        self.driver.find_element(*self.etf_button).click()
        # Test Outcome
        # assert self.driver.find_element(*self.currencies_header).is_displayed()
        # Real Time button
        self.driver.find_element(*self.real_time_button).click()
        # Test Outcome
        # assert self.driver.find_element(*self.currencies_header).is_displayed()
        '''