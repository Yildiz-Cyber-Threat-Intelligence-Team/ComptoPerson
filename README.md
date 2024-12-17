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
   python main.py 

### Şirket Adı Girişi
- Proje çalıştırıldığında, terminal üzerinden aramak istediğiniz şirketin adını girmeniz istenecektir. 
- Şirket adı birden fazla kelimeden oluşuyorsa, kelimeler arasında `-` kullanmalısınız. 
   - Örnekler:  google-cloud 

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




   
