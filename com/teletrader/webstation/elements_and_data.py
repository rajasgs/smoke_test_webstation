from selenium.webdriver.common.by import By


class Data:
    base_url = 'http://webstationtest3.ttweb.net/WebStation.aspx'
    base_title = 'TeleTrader WebStation'
    str_username = 'ivan.coric91'
    str_password = 'ictrader123'
    error_accept_eula = 'You have to accept the End User License Agreement in order to log in.'


class Elements:
    username = By.ID, 'userName'
    password = By.ID, 'password'
    login_button = By.ID, 'loginUser'
    error_container = By.CLASS_NAME, 'error_container_inner'
    eula_css = By.CSS_SELECTOR, "[for='eulaAccepted'].checkBoxLabel"
    eula_xpath = By.XPATH, "//*[@id='eulaAccepted']"
    auto_login = By.XPATH, "//*[@id='autologin']"
    logo_ws = By.ID, 'logo-ws'
    user_button = By.ID, 'user-button'
    account_settings = By.CSS_SELECTOR, "[href='personal_registration.aspx']"
    region_box = By.ID, 'regionBox'
    logout = By.CSS_SELECTOR, "[href='Logout.aspx']"

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

    # Detail page headers
    market_header = By.CSS_SELECTOR, ".main-pages-header.markets"
