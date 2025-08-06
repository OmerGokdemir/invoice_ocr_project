# 🧾 Invoice OCR Extraction

This Python project extracts key information from scanned PDF invoices using OCR (Optical Character Recognition) with **Tesseract** and image conversion tools.
It reads PDF files from an input folder, extracts invoice details such as Invoice Number, Date, Total Amount, and Company Name, and saves the results into both CSV and Excel files.

## 🚀 Features

*   Convert PDF pages to images for OCR processing

*   Extract invoice data (Invoice Number, Date, Total Amount, Company Name) using regex

*   Save extracted data to CSV and XLSX formats

*   Works with scanned PDFs (image-based) using Tesseract OCR

*   Easy to configure input/output directories and filenames

****

## 📦 Requirements

* Python 3.x

* [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed and added to your system PATH (or specify executable path in script)

* Python libraries:

  *   pytesseract

  *   pdf2image

  *   pandas

  *   Pillow

  *   openpyxl (for Excel export)

Install Python dependencies via pip:

```bash
pip install pytesseract pdf2image pandas pillow openpyxl
```

****

## 🖥️ Setup

1. Install Tesseract OCR:
   *   Download and install from the official repository.
   *   Make sure to update the `pytesseract.pytesseract.tesseract_cmd` variable in the script with the correct path to your Tesseract executable if it's not in your system PATH.

2. Input PDFs:
   *   Place your scanned invoice PDF files into the `invoices` directory (create if it doesn't exist).

3. Run the script:

    ```bash
    python extract_invoices.py
    ```

****

## 📤 Output

*   `extracted_invoices.csv` — CSV file with extracted invoice data

*   `extracted_invoices.xlsx` — Excel file with the same data for easier analysis

****

## ⚙️ How it works

*   Converts each page of the PDF into an image

*   Performs OCR on the images to extract text

*   Uses regular expressions to find invoice details in the text

*   Aggregates data from all PDFs into structured tabular format

****

## 👤 Customization

*   Modify `INPUT_DIR`, `OUTPUT_CSV`, `OUTPUT_XLSX` in the script to change input/output paths

*   Update regex patterns in `extract_data_from_text()` for different invoice formats or to extract additional fields

****

## 🧪 Troubleshooting

*   **No data extracted?**
    Check Tesseract OCR installation and paths

*   **Wrong or incomplete data?**
    Adjust regex expressions to match your invoice layouts

*   **Performance issues?**
    Processing scanned PDFs can be slow; consider batching files or optimizing OCR parameters

****

## 📄 License

[MIT License](LICENCE) — free to use and modify.

****

## 📩 Contact

For questions or improvements, feel free to reach out!

****

# 🧾 Fatura OCR Veri Çıkarımı

Bu Python projesi, OCR (Optik Karakter Tanıma) kullanarak taranmış PDF faturalardan önemli bilgileri çıkartır. Tesseract ve görsel dönüştürme araçlarını kullanarak PDF dosyalarını işler, fatura numarası, tarih, toplam tutar ve şirket adı gibi bilgileri alır ve sonuçları CSV ve Excel dosyalarına kaydeder.

## 🚀 Özellikler

* PDF sayfalarını OCR işlemi için görsellere dönüştürür

* Fatura verilerini çıkarır (Fatura Numarası, Tarih, Toplam Tutar, Şirket Adı)

* Çıkarılan verileri CSV ve XLSX formatlarında kaydeder

* Taranmış (görsel tabanlı) PDF’lerle çalışır

* Girdi/çıktı dizinleri ve dosya adları kolayca yapılandırılabilir

****

## 📦 Gereksinimler

* Python 3.x

* Tesseract OCR yüklü ve sistem PATH’ine eklenmiş olmalı (ya da scriptte açıkça belirtilmeli)

* Gerekli Python kütüphaneleri:

```bash
pip install pytesseract pdf2image pandas pillow openpyxl
```

****

## 🖥️ Kurulum

1. Tesseract OCR Kurulumu:

    * Resmi Tesseract deposundan indirip yükleyin

    * Eğer sistem PATH’ine eklenmediyse, script içerisindeki pytesseract.pytesseract.tesseract_cmd değişkenine Tesseract’ın kurulu olduğu dizini yazın

2. Girdi PDF’leri:

    * invoices adında bir klasör oluşturun (yoksa)

    * Taranmış fatura PDF dosyalarınızı bu klasöre yerleştirin

3. Scripti çalıştırın:

```bash
python extract_invoices.py
```

****

## 📤 Çıktılar

* `extracted_invoices.csv` — Çıkarılan fatura verilerini içeren CSV dosyası

* `extracted_invoices.xlsx` — Excel formatında aynı veriler, analiz için daha uygun

****

## ⚙️ Nasıl Çalışır?

* Her PDF sayfasını bir görsele dönüştürür

* Görseldeki metni OCR ile çözümler

* Metin içinden düzenli ifadeler (regex) ile fatura bilgilerini bulur

* Tüm PDF’lerden alınan verileri tablo halinde birleştirir

****
## 👤 Özelleştirme

* Girdi/çıktı klasörlerini ve dosya adlarını değiştirmek için scriptteki INPUT_DIR, OUTPUT_CSV, OUTPUT_XLSX değişkenlerini düzenleyin

* Farklı fatura formatları için veya ek alanlar çıkartmak için extract_data_from_text() fonksiyonundaki regex desenlerini güncelleyin

****

## 🧪 Sorun Giderme

* Veri çıkmıyor mu? → Tesseract OCR kurulumunu ve yollarını kontrol edin

* Yanlış veya eksik veri mi çıkıyor? → Regex ifadelerini kendi fatura yapınıza göre uyarlayın

* Performans yavaş mı? → PDF’leri toplu işleyin veya OCR parametrelerini optimize edin

****

## 📄 Lisans

[MIT License](LICENCE) — Ücretsiz olarak kullanılabilir ve değiştirilebilir.

****

## 📩 İletişim

Sorularınız ya da geliştirme önerileriniz için [benimle](@OmerGokdemir) iletişime geçebilirsiniz!

****

