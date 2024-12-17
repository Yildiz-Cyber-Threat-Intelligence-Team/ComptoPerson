# ComptoPerson

# TR

Bu proje, seçilen bir şirketin çalışan bilgilerini LinkedIn üzerinden toplayarak bir .txt dosyasına aktarmayı amaçlamaktadır. 

## Özellikler
- Otomatik bir şekilde chromium ekranı açılarak önceden `config.py`‘ye girmiş olduğunuz mail ve şifre girişi gerçekleştirir. 
(Bu aşamada doğrulama kodu veya captcha işlemleri karşınıza çıkabilir. Manuel olarak geçmeniz gerekmektedir.) 
- Seçilen şirketin çalışanlarının isim, iş unvanı ve lokasyon bilgilerini toplar.   
- Verileri ‘employees_info.txt’ dosyasına kaydeder.   

## Kod Açıklaması
### Gereksinimler
- Python 3.9.12 veya daha yeni bir sürümünün bilgisayarınızda yüklü olması gerekmektedir. 
- Ayrıca, Playwright kütüphanesinin kurulması gereklidir. Playwright, tarayıcı otomasyonu için kullanılan bir Python kütüphanesidir. Yüklemek için şu komutları kullanabilirsiniz: 
     `pip install playwright` 
     `playwright install` 

### LinkedIn Giriş Bilgileri
- LinkedIn hesabınıza giriş yapmak için `config.py` dosyasını düzenlemeniz gerekmektedir. Bu dosyaya LinkedIn kullanıcı adı (email) ve şifrenizi ekleyin: 
     `LINKEDIN_USERNAME = "email_adresiniz"` 
     `LINKEDIN_PASSWORD = "şifreniz"`

### Çalıştırma
Ana dosyayı çalıştırmak için aşağıdaki komutu terminalde kullanın:   
`python main.py` 

### Şirket Adı Girişi
- Proje çalıştırıldığında, terminal üzerinden aramak istediğiniz şirketin adını girmeniz istenecektir. 
- Şirket adı birden fazla kelimeden oluşuyorsa, kelimeler arasında `-` kullanmalısınız. 
   - Örnek:  google-cloud 

### Botun Çalışması
- Bot, LinkedIn'e otomatik olarak giriş yaptıktan sonra, seçtiğiniz şirketin sayfasına gider. 
- Veriler toplandıktan sonra, bot bir sonraki sayfaya geçer ve işlemi tekrarlar.  
- Tüm sayfalar geçildikten sonra, bot veri toplama işlemini sonlandırır ve verileri bir dosyaya kaydeder.

### Doğrulama İşlemi
- LinkedIn giriş doğrulaması manuel olarak yapılmalıdır. Giriş yaptıktan sonra, bot veri toplamaya devam eder. 
- Doğrulama işlemi genellikle bir güvenlik kontrolüdür, bu yüzden kullanıcı girişin doğruluğunu sağlamalıdır. 

### Sonuçların Kaydedilmesi
- Çalışan bilgileri, her biri isim, iş unvanı ve lokasyon olmak üzere `employees_info.txt` dosyasına kaydedilir. Bu dosya proje dizininde yer alacaktır.

### Kodunun Kullanılacağı Zaman Güncellenmesi Gereken Bölümler
- Kodun en son güncellenme tarihi 17.12.2024 tarihidir. Linkedln'in dinamik yapıda bir web sayfası olmasından kaynaklı id'ler düzenli olarak değişmekteir. Kodu kullanmadan önce id leri kontrol edip gücellemeniz gerekmektedir. 
- İd lere kodu çalıştırınca açılan sekmenin kaynak kodunu inceleyerek ulaşabilirsiniz.  
Gerekli adımlar ekran resmi olarak aşağıda yer almaktadır. 
1.
![1](https://github.com/user-attachments/assets/d75df3d9-82c0-4350-ac12-a2f39fd11117)
2.
![2](https://github.com/user-attachments/assets/1218ae82-3621-4849-9c3e-dafe419fa266)
3.
![3](https://github.com/user-attachments/assets/549a1a39-80ab-496f-b697-a3ebf7db2d26)
4.
![4](https://github.com/user-attachments/assets/744a59c5-18b3-4ffd-b190-e87103507e5b)

# EN
This project aims to collect employee information of a selected company from LinkedIn and export it to a .txt file.

## Features
- The chromium screen opens automatically and the e-mail and password you entered in config.py are entered.
  (At this stage, you may encounter a verification code or captcha. You must pass it manually.)
- Collects the name, job title and location information of the employees of the selected company.
- Saves the data in the `employees_info.txt` file.

## Code Description
### Requirements
- You must have Python 3.9.12 or later installed on your computer.
- In addition, the Playwright library must be installed. Playwright is a Python library used for browser automation. You can use the following commands to install it:
`pip install playwright`
`playwright install`

### LinkedIn Login Information
- To log in to your LinkedIn account, you need to edit the config.py file. Add your LinkedIn username (email) and password to this file:
`LINKEDIN_USERNAME = "your_email_address"`
`LINKEDIN_PASSWORD = "your_password"`

### Operating
To run the main file, use the following command in the terminal:
`python main.py`

### Company Name Entry
- When the project is launched, you will be asked to enter the name of the company you want to search for via the terminal.
- If the company name consists of more than one word, you must use `-` between the words.
- Examples: google-cloud

### How the Bot Works
- After automatically logging into LinkedIn, the bot will go to the company page you selected.
- Once the data is collected, the bot will move to the next page and repeat the process.
- Once all the pages have been passed, the bot will finish collecting data and save the data to a file.

### Verification Process
- LinkedIn login verification must be done manually. After logging in, the bot continues to collect data.
- Verification is usually a security check, so the user must ensure that the login is correct.

### Recording Results
- Employee information, including name, job title, and location, is recorded in the file `employees_info.txt`. This file will be located in the project directory.

### Sections That Need to Be Updated When Using the Code
- The last update date of the code is 17.12.2024. Since LinkedIn is a dynamic web page, the IDs change regularly. Before using the code, you need to check and update the IDs.
- You can access the IDs by examining the source code of the tab that opens when you run the code.
- The necessary steps are given below as a screenshot.


   
