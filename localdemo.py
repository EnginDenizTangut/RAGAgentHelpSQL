import sqlite3
from openai import OpenAI
from typing import List, Dict
import json

class SQLRAG:
    def __init__(self, db_path: str, openai_api_key: str):
        """SQL RAG sistemi başlatır"""
        self.db_path = db_path
        self.client = OpenAI(api_key=openai_api_key)
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def create_demo_database(self):
        """Demo veritabanı oluşturur - Genişletilmiş versiyon"""

        self.cursor.execute()

        self.cursor.execute()

        self.cursor.execute()

        self.cursor.execute()

        self.cursor.execute()

        self.cursor.execute()

        self.cursor.execute()

        self.cursor.execute()

        self.cursor.execute()

        calisanlar_data = [
            (1, 'Ahmet', 'Yılmaz', 'IT', 'Yazılım Geliştirici', 15000, '2020-03-15', '1990-05-12', 'ahmet.yilmaz@sirket.com', '0532-111-1111', 'İstanbul'),
            (2, 'Ayşe', 'Demir', 'IT', 'Veri Analisti', 14000, '2021-06-20', '1992-08-25', 'ayse.demir@sirket.com', '0533-222-2222', 'İstanbul'),
            (3, 'Mehmet', 'Kaya', 'Satış', 'Satış Müdürü', 18000, '2019-01-10', '1985-03-18', 'mehmet.kaya@sirket.com', '0534-333-3333', 'Ankara'),
            (4, 'Fatma', 'Şahin', 'Satış', 'Satış Temsilcisi', 12000, '2022-04-05', '1995-11-30', 'fatma.sahin@sirket.com', '0535-444-4444', 'İzmir'),
            (5, 'Ali', 'Çelik', 'İK', 'İK Uzmanı', 13000, '2020-11-30', '1988-07-22', 'ali.celik@sirket.com', '0536-555-5555', 'İstanbul'),
            (6, 'Zeynep', 'Arslan', 'IT', 'Backend Developer', 16000, '2021-02-14', '1991-12-05', 'zeynep.arslan@sirket.com', '0537-666-6666', 'İstanbul'),
            (7, 'Can', 'Öztürk', 'Pazarlama', 'Pazarlama Müdürü', 17000, '2019-09-01', '1987-04-15', 'can.ozturk@sirket.com', '0538-777-7777', 'İstanbul'),
            (8, 'Elif', 'Yıldız', 'Pazarlama', 'Sosyal Medya Uzmanı', 11000, '2022-07-18', '1996-02-28', 'elif.yildiz@sirket.com', '0539-888-8888', 'Ankara'),
            (9, 'Burak', 'Aydın', 'Finans', 'Mali Müşavir', 19000, '2018-05-20', '1984-09-10', 'burak.aydin@sirket.com', '0530-999-9999', 'İstanbul'),
            (10, 'Selin', 'Kurt', 'İK', 'İK Müdürü', 16500, '2019-03-12', '1986-06-17', 'selin.kurt@sirket.com', '0531-000-0000', 'İstanbul'),
            (11, 'Emre', 'Polat', 'IT', 'DevOps Engineer', 17500, '2020-08-25', '1989-11-03', 'emre.polat@sirket.com', '0532-101-0101', 'İstanbul'),
            (12, 'Deniz', 'Şen', 'Satış', 'Satış Temsilcisi', 11500, '2023-01-09', '1997-01-20', 'deniz.sen@sirket.com', '0533-202-0202', 'İzmir'),
            (13, 'Murat', 'Koç', 'IT', 'IT Müdürü', 22000, '2017-06-01', '1983-08-14', 'murat.koc@sirket.com', '0534-303-0303', 'İstanbul'),
            (14, 'Nazlı', 'Güler', 'Pazarlama', 'İçerik Editörü', 10500, '2023-03-15', '1998-05-09', 'nazli.guler@sirket.com', '0535-404-0404', 'Ankara'),
            (15, 'Kerem', 'Yavuz', 'Finans', 'Muhasebe Uzmanı', 12500, '2021-10-20', '1993-12-22', 'kerem.yavuz@sirket.com', '0536-505-0505', 'İstanbul')
        ]

        departmanlar_data = [
            (1, 'IT', 13, 500000, 3),
            (2, 'Satış', 3, 300000, 1),
            (3, 'İK', 10, 200000, 2),
            (4, 'Pazarlama', 7, 250000, 2),
            (5, 'Finans', 9, 400000, 4)
        ]

        urunler_data = [
            (1, 'Laptop Dell XPS 15', 'Elektronik', 35000, 45, 'Dell', 2024, 24),
            (2, 'iPhone 15 Pro', 'Elektronik', 45000, 80, 'Apple', 2024, 12),
            (3, 'Mekanik Klavye', 'Aksesuar', 1500, 150, 'Logitech', 2023, 24),
            (4, 'Ergonomik Mouse', 'Aksesuar', 800, 200, 'Logitech', 2023, 12),
            (5, 'LG UltraWide Monitör', 'Elektronik', 12000, 60, 'LG', 2024, 36),
            (6, 'Samsung Galaxy S24', 'Elektronik', 38000, 70, 'Samsung', 2024, 12),
            (7, 'AirPods Pro', 'Aksesuar', 8500, 100, 'Apple', 2023, 12),
            (8, 'iPad Air', 'Elektronik', 22000, 50, 'Apple', 2024, 12),
            (9, 'Webcam HD', 'Aksesuar', 2500, 120, 'Logitech', 2023, 24),
            (10, 'USB-C Hub', 'Aksesuar', 600, 180, 'Anker', 2023, 12),
            (11, 'Laptop Asus ROG', 'Elektronik', 42000, 30, 'Asus', 2024, 24),
            (12, 'Kulaklık Sony WH-1000XM5', 'Aksesuar', 11000, 90, 'Sony', 2023, 12),
            (13, 'Harici SSD 1TB', 'Aksesuar', 3500, 140, 'Samsung', 2024, 36),
            (14, 'Grafik Tablet', 'Elektronik', 5500, 40, 'Wacom', 2023, 24),
            (15, 'Akıllı Saat Apple Watch', 'Elektronik', 15000, 65, 'Apple', 2024, 12)
        ]

        musteriler_data = [
            (1, 'Kemal', 'Acar', 'kemal.acar@mail.com', '0541-111-1111', 'İstanbul', '2022-01-15', 850),
            (2, 'Sevgi', 'Tekin', 'sevgi.tekin@mail.com', '0542-222-2222', 'Ankara', '2021-05-20', 1200),
            (3, 'Okan', 'Birol', 'okan.birol@mail.com', '0543-333-3333', 'İzmir', '2023-02-10', 450),
            (4, 'Pınar', 'Çakır', 'pinar.cakir@mail.com', '0544-444-4444', 'Bursa', '2022-08-25', 920),
            (5, 'Volkan', 'Erdoğan', 'volkan.erdogan@mail.com', '0545-555-5555', 'Antalya', '2023-06-12', 340),
            (6, 'Gizem', 'Bayrak', 'gizem.bayrak@mail.com', '0546-666-6666', 'İstanbul', '2021-11-30', 1450),
            (7, 'Serkan', 'Uzun', 'serkan.uzun@mail.com', '0547-777-7777', 'Ankara', '2022-03-18', 780),
            (8, 'Aylin', 'Kara', 'aylin.kara@mail.com', '0548-888-8888', 'İzmir', '2023-09-05', 510),
            (9, 'Cem', 'Bulut', 'cem.bulut@mail.com', '0549-999-9999', 'İstanbul', '2021-07-22', 1680),
            (10, 'Melis', 'Aksoy', 'melis.aksoy@mail.com', '0540-000-0000', 'Ankara', '2022-12-08', 890)
        ]

        satislar_data = [
            (1, 1, 3, 1, 2, 70000, '2024-10-15', 'Kredi Kartı'),
            (2, 2, 4, 2, 3, 135000, '2024-10-20', 'Nakit'),
            (3, 3, 3, 3, 5, 7500, '2024-10-25', 'Kredi Kartı'),
            (4, 1, 4, 4, 1, 35000, '2024-11-01', 'Havale'),
            (5, 5, 3, 5, 2, 24000, '2024-11-05', 'Kredi Kartı'),
            (6, 6, 12, 6, 2, 76000, '2024-10-18', 'Taksit'),
            (7, 7, 4, 7, 4, 34000, '2024-10-22', 'Kredi Kartı'),
            (8, 8, 3, 8, 1, 22000, '2024-10-28', 'Havale'),
            (9, 9, 12, 9, 3, 7500, '2024-11-02', 'Nakit'),
            (10, 10, 4, 10, 10, 6000, '2024-11-06', 'Kredi Kartı'),
            (11, 11, 3, 1, 1, 42000, '2024-10-12', 'Taksit'),
            (12, 12, 12, 2, 2, 22000, '2024-10-19', 'Kredi Kartı'),
            (13, 13, 4, 3, 5, 17500, '2024-10-26', 'Havale'),
            (14, 14, 3, 4, 1, 5500, '2024-11-03', 'Nakit'),
            (15, 15, 12, 5, 3, 45000, '2024-11-07', 'Kredi Kartı'),
            (16, 2, 4, 6, 2, 90000, '2024-10-14', 'Taksit'),
            (17, 4, 3, 7, 8, 6400, '2024-10-21', 'Kredi Kartı'),
            (18, 5, 12, 8, 1, 12000, '2024-10-27', 'Havale'),
            (19, 7, 4, 9, 2, 17000, '2024-11-04', 'Nakit'),
            (20, 3, 3, 10, 15, 22500, '2024-11-08', 'Kredi Kartı')
        ]

        projeler_data = [
            (1, 'E-Ticaret Platformu', 'IT', '2024-01-15', '2024-12-31', 800000, 'Devam Ediyor', 13),
            (2, 'Mobil Uygulama Geliştirme', 'IT', '2024-03-01', '2024-11-30', 500000, 'Devam Ediyor', 6),
            (3, 'Dijital Pazarlama Kampanyası', 'Pazarlama', '2024-02-10', '2024-08-31', 200000, 'Tamamlandı', 7),
            (4, 'İK Otomasyon Sistemi', 'İK', '2024-04-01', '2025-03-31', 300000, 'Devam Ediyor', 10),
            (5, 'CRM Entegrasyonu', 'Satış', '2024-05-15', '2024-12-15', 450000, 'Devam Ediyor', 3),
            (6, 'Veri Analiz Dashboard', 'IT', '2024-06-01', '2024-10-30', 250000, 'Tamamlandı', 2),
            (7, 'Sosyal Medya Stratejisi', 'Pazarlama', '2024-07-01', '2025-01-31', 180000, 'Devam Ediyor', 8)
        ]

        proje_atamalari_data = [
            (1, 1, 1, 'Full Stack Developer', '2024-01-15'),
            (2, 1, 6, 'Backend Developer', '2024-01-15'),
            (3, 1, 11, 'DevOps Engineer', '2024-01-20'),
            (4, 2, 1, 'Mobile Developer', '2024-03-01'),
            (5, 2, 6, 'Backend Support', '2024-03-05'),
            (6, 3, 7, 'Proje Lideri', '2024-02-10'),
            (7, 3, 8, 'Sosyal Medya', '2024-02-10'),
            (8, 3, 14, 'İçerik Üretimi', '2024-02-15'),
            (9, 4, 5, 'İK Uzmanı', '2024-04-01'),
            (10, 4, 10, 'Proje Lideri', '2024-04-01'),
            (11, 5, 3, 'Proje Lideri', '2024-05-15'),
            (12, 5, 4, 'CRM Koordinatörü', '2024-05-15'),
            (13, 5, 12, 'Satış Desteği', '2024-05-20'),
            (14, 6, 2, 'Veri Analisti', '2024-06-01'),
            (15, 6, 13, 'Teknik Danışman', '2024-06-01'),
            (16, 7, 7, 'Strateji Lideri', '2024-07-01'),
            (17, 7, 8, 'İçerik Yöneticisi', '2024-07-01')
        ]

        izinler_data = [
            (1, 1, 'Yıllık İzin', '2024-08-01', '2024-08-15', 'Onaylandı', 'Yaz tatili'),
            (2, 2, 'Hastalık İzni', '2024-09-10', '2024-09-12', 'Onaylandı', 'Grip'),
            (3, 3, 'Yıllık İzin', '2024-07-15', '2024-07-30', 'Onaylandı', 'Aile ziyareti'),
            (4, 4, 'Mazeret İzni', '2024-10-05', '2024-10-05', 'Onaylandı', 'Özel'),
            (5, 5, 'Yıllık İzin', '2024-11-20', '2024-11-25', 'Beklemede', 'Planlanan tatil'),
            (6, 7, 'Yıllık İzin', '2024-06-10', '2024-06-20', 'Onaylandı', 'Yurt dışı tatil'),
            (7, 9, 'Hastalık İzni', '2024-10-15', '2024-10-17', 'Onaylandı', 'Ameliyat'),
            (8, 11, 'Yıllık İzin', '2024-12-23', '2025-01-03', 'Beklemede', 'Yılbaşı tatili')
        ]

        stok_hareketleri_data = [
            (1, 1, 'Giriş', 50, '2024-09-01', 'Yeni sipariş'),
            (2, 1, 'Çıkış', 5, '2024-10-15', 'Satış'),
            (3, 2, 'Giriş', 100, '2024-09-15', 'Yeni sipariş'),
            (4, 2, 'Çıkış', 20, '2024-10-20', 'Satışlar'),
            (5, 5, 'Giriş', 75, '2024-09-20', 'Yeni sipariş'),
            (6, 3, 'Çıkış', 50, '2024-10-25', 'Satışlar'),
            (7, 6, 'Giriş', 80, '2024-09-25', 'Yeni sipariş'),
            (8, 7, 'Çıkış', 10, '2024-10-22', 'Satışlar'),
            (9, 8, 'Giriş', 50, '2024-10-01', 'Yeni sipariş'),
            (10, 10, 'Çıkış', 20, '2024-11-06', 'Satışlar')
        ]

        self.cursor.executemany('INSERT OR IGNORE INTO calisanlar VALUES (?,?,?,?,?,?,?,?,?,?,?)', calisanlar_data)
        self.cursor.executemany('INSERT OR IGNORE INTO departmanlar VALUES (?,?,?,?,?)', departmanlar_data)
        self.cursor.executemany('INSERT OR IGNORE INTO urunler VALUES (?,?,?,?,?,?,?,?)', urunler_data)
        self.cursor.executemany('INSERT OR IGNORE INTO musteriler VALUES (?,?,?,?,?,?,?,?)', musteriler_data)
        self.cursor.executemany('INSERT OR IGNORE INTO satislar VALUES (?,?,?,?,?,?,?,?)', satislar_data)
        self.cursor.executemany('INSERT OR IGNORE INTO projeler VALUES (?,?,?,?,?,?,?,?)', projeler_data)
        self.cursor.executemany('INSERT OR IGNORE INTO proje_atamalari VALUES (?,?,?,?,?)', proje_atamalari_data)
        self.cursor.executemany('INSERT OR IGNORE INTO izinler VALUES (?,?,?,?,?,?,?)', izinler_data)
        self.cursor.executemany('INSERT OR IGNORE INTO stok_hareketleri VALUES (?,?,?,?,?,?)', stok_hareketleri_data)

        self.conn.commit()

        self.cursor.execute("SELECT COUNT(*) FROM calisanlar")
        calisan_sayisi = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT COUNT(*) FROM urunler")
        urun_sayisi = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT COUNT(*) FROM satislar")
        satis_sayisi = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT COUNT(*) FROM musteriler")
        musteri_sayisi = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT COUNT(*) FROM projeler")
        proje_sayisi = self.cursor.fetchone()[0]

        print("✅ Genişletilmiş veritabanı başarıyla oluşturuldu!")
        print(f"📊 İstatistikler:")
        print(f"   • {calisan_sayisi} Çalışan")
        print(f"   • {urun_sayisi} Ürün")
        print(f"   • {satis_sayisi} Satış")
        print(f"   • {musteri_sayisi} Müşteri")
        print(f"   • {proje_sayisi} Proje")
        print(f"   • 9 Tablo")

    def get_database_schema(self) -> str:
        """Veritabanı şemasını döndürür"""
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()

        schema = "VERİTABANI ŞEMASI:\n\n"
        for table in tables:
            table_name = table[0]
            self.cursor.execute(f"PRAGMA table_info({table_name})")
            columns = self.cursor.fetchall()

            schema += f"📋 Tablo: {table_name}\n"
            schema += "Kolonlar:\n"
            for col in columns:
                schema += f"  - {col[1]} ({col[2]})\n"
            schema += "\n"

        return schema

    def generate_sql_query(self, question: str) -> str:
        """Soruya göre SQL sorgusu oluşturur"""
        schema = self.get_database_schema()

        prompt = f"""Sen bir SQL uzmanısın. Aşağıdaki veritabanı şemasına göre kullanıcının sorusunu yanıtlayacak SQL sorgusu yaz.

{schema}

KULLANICI SORUSU: {question}

KURALLAR:
1. Sadece SELECT sorguları yaz (INSERT, UPDATE, DELETE yok)
2. Türkçe kolonlar var, dikkat et
3. JOIN'ler gerekiyorsa kullan
4. Yanıt olarak SADECE SQL sorgusunu ver, başka açıklama ekleme
5. SQL sorgusunu ``` işaretleri olmadan ver

SQL SORGUSU:"""

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        sql_query = response.choices[0].message.content.strip()

        sql_query = sql_query.replace("```sql", "").replace("```", "").strip()
        return sql_query

    def execute_query(self, sql_query: str) -> List[Dict]:
        """SQL sorgusunu çalıştırır"""
        try:
            self.cursor.execute(sql_query)
            columns = [description[0] for description in self.cursor.description]
            results = self.cursor.fetchall()

            result_dicts = []
            for row in results:
                result_dicts.append(dict(zip(columns, row)))

            return result_dicts
        except Exception as e:
            return [{"error": f"SQL hatası: {str(e)}"}]

    def generate_natural_answer(self, question: str, sql_query: str, results: List[Dict]) -> str:
        """Sonuçları doğal dilde açıklar"""
        prompt = f"""Kullanıcı şu soruyu sordu: {question}

Bu sorguyu çalıştırdım:
{sql_query}

Sonuçlar:
{json.dumps(results, ensure_ascii=False, indent=2)}

Lütfen bu sonuçları kullanıcıya Türkçe, açık ve anlaşılır bir şekilde açıkla. 
Sayısal verileri belirt, tabloları güzel formatta göster."""

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        return response.choices[0].message.content

    def ask(self, question: str) -> Dict:
        """Ana fonksiyon: Soru sorar ve cevap alır"""
        print(f"\n❓ Soru: {question}")
        print("=" * 60)

        print("🔄 SQL sorgusu oluşturuluyor...")
        sql_query = self.generate_sql_query(question)
        print(f"📝 Oluşturulan SQL:\n{sql_query}\n")

        print("⚙️  Sorgu çalıştırılıyor...")
        results = self.execute_query(sql_query)

        if results and "error" in results[0]:
            print(f"❌ {results[0]['error']}")
            return {"error": results[0]['error']}

        print(f"✅ {len(results)} sonuç bulundu\n")

        print("💬 Cevap hazırlanıyor...")
        answer = self.generate_natural_answer(question, sql_query, results)
        print(f"\n🤖 Cevap:\n{answer}\n")

        return {
            "question": question,
            "sql_query": sql_query,
            "results": results,
            "answer": answer
        }

    def close(self):
        """Bağlantıyı kapatır"""
        self.conn.close()

if __name__ == "__main__":

    API_KEY = "your-openai-key"

    rag = SQLRAG("demo_sirketi.db", API_KEY)

    rag.create_demo_database()

    print("\n" + rag.get_database_schema())

    print("=" * 60)
    print("🤖 SQL RAG SİSTEMİNE HOŞ GELDİNİZ!")
    print("=" * 60)
    print("Veritabanı hakkında soru sorabilirsiniz.")
    print("Çıkmak için 'quit', 'exit' veya 'esc' yazın.\n")

    while True:
        try:

            soru = input("❓ Sorunuz: ").strip()

            if soru.lower() in ['quit', 'exit', 'esc', 'çıkış', 'cikis']:
                print("\n👋 Görüşmek üzere!")
                break

            if not soru:
                print("⚠️  Lütfen bir soru yazın.\n")
                continue

            rag.ask(soru)
            print("\n" + "-" * 60 + "\n")

        except KeyboardInterrupt:

            print("\n\n👋 Görüşmek üzere!")
            break
        except Exception as e:
            print(f"\n❌ Bir hata oluştu: {str(e)}\n")

    rag.close()