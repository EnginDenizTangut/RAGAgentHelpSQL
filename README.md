# RAG (Retrieval-Augmented Generation) Sistemi

Bu proje, büyük bir doküman veritabanından bilgi çekerek sorulara cevap veren bir RAG sistemi içerir.

## Özellikler

- 📚 Büyük ve gerçekçi doküman veritabanı (60+ doküman)
- 💾 SQLite veritabanı desteği
- 🔍 Semantik arama (embedding tabanlı)
- 💬 Soru-cevap sistemi
- 🌍 Türkçe dil desteği
- 🎯 Çoklu kategori desteği (Teknoloji, Sağlık, Finans, Eğitim, vb.)

## Kurulum

1. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

2. Veritabanını oluşturun:
```bash
python3 rag/database_generator.py
```

Bu komut, `rag/database.db` SQLite veritabanı dosyasını oluşturur ve 60+ doküman içerir.

## Kullanım

### Basit Demo

```bash
python rag/demo.py
```

Bu komut interaktif bir soru-cevap arayüzü açar.

### Programatik Kullanım

```python
from rag.rag_system import RAGSystem, load_documents_from_db

# RAG sistemini oluştur
rag = RAGSystem(
    db_path="rag/chroma_db",
    embedding_model="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# Dokümanları SQLite veritabanından yükle (ilk seferinde)
documents = load_documents_from_db("rag/database.db")
rag.add_documents(documents)

# Soru sor
result = rag.answer_question("Yapay zeka nedir?")
print(result["answer"])
```

## Veritabanı Yapısı

Veritabanı şu kategorilerde dokümanlar içerir:

- **Teknoloji**: Yapay zeka, bulut bilişim, siber güvenlik
- **Sağlık**: Kalp sağlığı, beslenme, mental sağlık
- **Finans**: Kişisel finans, kripto para, emeklilik
- **Eğitim**: Online eğitim, dil öğrenme
- **İş Dünyası**: Girişimcilik, dijital pazarlama
- **Spor**: Fitness ve antrenman
- **Seyahat**: Seyahat planlama
- **Yemek**: Sağlıklı pişirme teknikleri

## Sistem Mimarisi

1. **Embedding Modeli**: `paraphrase-multilingual-MiniLM-L12-v2` (Türkçe destekli)
2. **Vektör Veritabanı**: ChromaDB (kalıcı depolama)
3. **Retrieval**: Cosine similarity ile semantik arama
4. **Generation**: OpenAI GPT-3.5 (opsiyonel) veya basit birleştirme

## Dosya Yapısı

```
rag/
├── database_generator.py  # Veritabanı oluşturucu
├── rag_system.py          # Ana RAG sistemi
├── demo.py                # Demo scripti
├── database.db            # SQLite doküman veritabanı (oluşturulacak)
├── chroma_db/             # ChromaDB vektör veritabanı (otomatik oluşturulur)
└── README.md              # Bu dosya
```

## Veritabanı Formatı

Sistem artık SQLite veritabanı (`database.db`) kullanmaktadır. JSON formatı (`database.json`) hala desteklenmektedir ancak öncelik SQLite veritabanındadır.

SQLite veritabanı şu tabloyu içerir:
- **documents**: id, category, title, content, author, date, views

## Notlar

- İlk çalıştırmada embedding modeli indirilecektir (~400MB)
- OpenAI API kullanmak için `OPENAI_API_KEY` environment variable'ını ayarlayın
- Veritabanı ilk oluşturulduğunda biraz zaman alabilir

## Geliştirme

Yeni dokümanlar eklemek için `database_generator.py` dosyasını düzenleyebilirsiniz.
