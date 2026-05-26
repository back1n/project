from read_to_config import *
from playwright.sync_api import sync_playwright

def run():
    
    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False)  # Запуск браузера
        page = browser.new_page()  # Создание новой страницы
        
        for i, url in enumerate(SESSION):
            
            page.goto(url)  # переход по ссылке
            
            page.get_by_role("textbox", name="Логин").click()
            page.get_by_role("textbox", name="Логин").fill(f"{USERNAME}")
            page.get_by_role("textbox", name="Логин").press("Tab")
            page.get_by_role("textbox", name="Пароль").fill(f"{PASSWORD_OR_TOKEN}")
            page.get_by_role("button", name="Вход").click()
            
            page.wait_for_load_state("networkidle")  # networkidle - ожидание пока подгрузяться js
            
            poker_block = page.locator(".session-participants-status")
            
        if poker_block.count() > 0:
            # 3. Берем HTML только внутри этого блока
            block_html = poker_block.inner_html()
        
            print("--- НАЙДЕННЫЙ БЛОК ---")
        
            # Можно сохранить в отдельный файл
            filename = f"page_{i+1}.html"
            with open(filename, "w", encoding="utf-8") as file:
                file.write(block_html)
                
        else:
            print("Блок с покером не найден!")
        
        browser.close()
        
        
        
if __name__ == "__main__":
    run()
    
    