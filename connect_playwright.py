from read_to_config import *
from playwright.sync_api import sync_playwright

def run():
    
    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False)  # Запуск браузера
        page = browser.new_page()  # Создание новой страницы
        
        try:
            page.goto(JIRA_URL)  # переход по ссылке
            
            # Вход в систему
            page.get_by_role("textbox", name="Логин").click()
            page.get_by_role("textbox", name="Логин").fill(f"{USERNAME}")
            page.get_by_role("textbox", name="Логин").press("Tab")
            page.get_by_role("textbox", name="Пароль").fill(f"{PASSWORD_OR_TOKEN}")
            page.get_by_role("button", name="Вход").click()
        except:
            print("Проблемма с входом в систему")
            logging.error(f"Ошибка входа в {JIRA_URL}")
            
        for url in SESSION:
            try:
                page.goto(url)

                # Извелечение данных
                session_grade = ''
            except:
                print("Возможно ссылка повреждена")
                logging.error(f"Проверьте ссылку: {url}")

        
        browser.close()
        
        
        
if __name__ == "__main__":
    run()
    
    