from playwright.sync_api import sync_playwright
import config
import time

def linkedin_bot():
    username = config.LINKEDIN_USERNAME
    password = config.LINKEDIN_PASSWORD

    company_name = input("Aramak istediğiniz şirket ismini girin: ")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.linkedin.com/login")
        print("LinkedIn'e giriş yapılıyor...")
        page.fill("input#username", username)
        page.fill("input#password", password)
        page.click("button[type=submit]")

        try:
            page.wait_for_url("https://www.linkedin.com/feed/", timeout=24000)
            print("Giriş başarılı!")
        except Exception as e:
            print(f"Giriş başarısız oldu: {e}")
            browser.close()
            return

        search_url = "https://www.linkedin.com/search/results/people/?origin=FACETED_SEARCH"
        page.goto(search_url)
        print("Arama sayfasına gidiliyor...")

        try:
            page.wait_for_selector("#searchFilter_currentCompany", timeout=10000)
            page.locator("#searchFilter_currentCompany").scroll_into_view_if_needed()
            page.click("#searchFilter_currentCompany")
            print("Mevcut şirket filtresi açıldı.")

            page.fill("input[placeholder='Şirket ekle']", company_name)
            time.sleep(2)

            company_list_selector = "div[role='listbox'] > div"
            page.wait_for_selector(company_list_selector, timeout=30000)

            first_company = page.locator(company_list_selector).first
            first_company.scroll_into_view_if_needed()
            first_company.click()
            print(f"'{company_name}' şirketi seçildi.")
        except Exception as e:
            print(f"Şirket seçimi sırasında bir hata oluştu: {e}")
            browser.close()
            return

        time.sleep(2)

        try:
            buttons = page.locator("button:has-text('Sonuçları göster')")
            for i in range(buttons.count()):
                button = buttons.nth(i)
                if button.is_visible():
                    button.scroll_into_view_if_needed()
                    button.click()
                    print("Doğru butona tıklandı!")
                    break
            else:
                print("Hiçbir buton tıklanabilir durumda değil.")
        except Exception as e:
            print(f"Sonuçları göster butonuna tıklama sırasında bir hata oluştu: {e}")
            browser.close()
            return

        time.sleep(5)

        employees = []
        page_number = 1
        while True:
            print(f"Sayfa {page_number} çalışan bilgileri çekiliyor...")

            for _ in range(5): 
                page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
                time.sleep(1)

            try:
                employee_cards = page.locator("li.AzUHSIcDpyaLkwSZmBtCoOlWIyexIQYxg")
                for i in range(employee_cards.count()):
                    try:
                        card = employee_cards.nth(i)
                        name = card.locator("span.QwrfzQPBYvtFCKlQkDFOMFZpyRFA > a").inner_text()
                        job_title = card.locator("div.HfZFuPHGtwgBtEhYPPjErraXxsQikCfmkzcE").inner_text()
                        location = card.locator("div.TIPiImOlYjdixdiCAixhFkTwgWSITjWTBPJg").inner_text()
                        employees.append({"name": name, "job_title": job_title, "location": location})
                        print(f"İsim: {name} | İş unvanı: {job_title} | Lokasyon: {location}")
                    except Exception as e:
                        print(f"Bir çalışan bilgisi alınamadı: {e}")
                        continue
            except Exception as e:
                print(f"Çalışan bilgilerini çekerken hata oluştu: {e}")
                break

            next_button = page.locator("button[aria-label='İleri']").first
            if next_button.is_enabled():
                next_button.scroll_into_view_if_needed()
                next_button.click()
                print(f"Sayfa {page_number + 1} geçiliyor...")
                time.sleep(5)

            else:
                print("Son sayfaya ulaşıldı.")
                break

            page_number += 1

        print(f"Toplam {len(employees)} çalışan bilgisi alındı.")
        with open("employees_info.txt", "w", encoding="utf-8") as f:
            for emp in employees:
                f.write(f"İsim: {emp['name']}\n")
                f.write(f"İş Unvanı: {emp['job_title']}\n")
                f.write(f"Lokasyon: {emp['location']}\n")
                f.write("\n")
        print("Çalışan bilgileri 'employees_info.txt' dosyasına kaydedildi.")

        browser.close()

linkedin_bot()