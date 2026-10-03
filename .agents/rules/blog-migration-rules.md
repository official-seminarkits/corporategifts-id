# Blog Detail Migration Rules & Standard Architecture

## 1. Scope & Baseline Standard
Setiap artikel detail blog di `blog/<slug>.html` WAJIB mengikuti standar blueprint resmi yang mengacu 100% pada artikel gold standard:
- `blog/cara-undi-doorprize-bukber-perusahaan.html`
- `blog/souvenir-tumbler-panduan-lengkap-untuk-pemula.html`
- `blog/_template_blueprint.html` (Template kerangka dasar resmi)

DILARANG mengubah atau memvariasikan struktur dasar, tag pembungkus, kelas CSS, atau urutan elemen.

---

## 2. Standar SEO, Meta Tags, & Karakter

1. **Title Tag (`<title>`)**:
   - Maksimal **50 - 60 karakter** (Batas absolut toleransi: **65 karakter** termasuk suffix ` | CorporateGifts.ID`).
   - Suffix brand ` | CorporateGifts.ID` = 20 karakter. Judul sebelum suffix idealnya **30 - 45 karakter**.
   - Lakukan *smart trimming* jika judul Blogger terlalu panjang. Hindari judul terpotong elipsis (`...`) di Google SERP.
2. **Heading 1 (`<h1>`)**:
   - Maksimal **50 - 70 karakter**. Ringkas, proporsional, dan nyaman dibaca di layar mobile.
3. **Open Graph & Twitter Title (`og:title`, `twitter:title`)**:
   - Maksimal **50 - 60 karakter**.
4. **Meta Description (`<meta name="description">`)**:
   - Optimal **120 - 155 karakter** (maksimal 160 karakter). Wajib memuat ringkasan isi, keyword utama, dan CTA.
5. **GEO Meta Tags (Wajib Baku)**:
   ```html
   <meta name="geo.region" content="ID-JI">
   <meta name="geo.placename" content="Surabaya, Jawa Timur, Indonesia">
   <meta name="geo.position" content="-7.2575;112.7521">
   <meta name="ICBM" content="-7.2575, 112.7521">
   ```
6. **Canonical & Body Tag**:
   - Canonical: `<link rel="canonical" href="https://corporategifts.id/blog/[slug]">`
   - Body Tag: `<body class="blog-detail-page">` (DILARANG menggunakan `blog-details-page`).

---

## 3. Standar Baku 5 Schema JSON-LD (Wajib 100% Lengkap)

Setiap artikel blog wajib memuat 5 schema terpisah dalam tag `<script type="application/ld+json">`:

1. **Schema 1: LocalBusiness & Organization**
   - `@id`: `"https://corporategifts.id/#localbusiness"`
   - `name`: `"CorporateGifts.ID"`
   - `alternateName`: `"Vendor Corporate Gift & Souvenir Perusahaan"`
   - `url`: `"https://corporategifts.id/"`
   - `logo`: `"https://corporategifts.id/assets/img/logo-header.png"`
   - `image`: `"https://corporategifts.id/assets/img/services/vendor-souvenir-perusahaan.webp"`
   - `telephone`: `"+62895639068080"`
   - `priceRange`: `"Rp15.000 - Rp750.000"`
   - `address`: Wajib lengkap (`streetAddress: "Jl. Basuki Rahmat No. 12-18, Tegalsari"`, `addressLocality: "Surabaya"`, `addressRegion: "Jawa Timur"`, `postalCode: "60261"`, `addressCountry: "ID"`).
   - `openingHoursSpecification`: Weekdays (08:30-17:30) & Saturday (09:00-15:00).
   - `sameAs`: WA, Instagram, Facebook, TikTok, domain jaringan.

2. **Schema 2: Article (Utama `#article`)**
   - `@id`: `"https://corporategifts.id/blog/[slug]#article"`
   - `mainEntityOfPage`: `{"@type": "WebPage", "@id": "https://corporategifts.id/blog/[slug]"}`
   - `headline`, `description`, `datePublished`, `dateModified`.
   - `image`: Array 2 URL gambar WebP (`[ "...-1.webp", "...-2.webp" ]`).
   - `author`: `{"@type": "Person", "name": "[Nama]", "url": "https://corporategifts.id/penulis#[slug]", "jobTitle": "[Jabatan]", "sameAs": "https://corporategifts.id/penulis#[slug]"}`.
   - `publisher`: `{"@type": "Organization", "@id": "https://corporategifts.id/#localbusiness", "name": "CorporateGifts.ID", "url": "https://corporategifts.id/", "logo": {"@type": "ImageObject", "url": "https://corporategifts.id/assets/img/logo-header.png"}}`.
   - `articleSection`, `inLanguage: "id-ID"`.

3. **Schema 3: Article (Ringkasan Eksekutif `#summary`)**
   - `@id`: `"https://corporategifts.id/blog/[slug]#summary"`
   - `headline`: `"Ringkasan Eksekutif: [Judul]"`
   - `description`: Ringkasan 1-2 kalimat dari Poin Kunci.
   - `image`: Array 1 URL gambar WebP featured (`[ "...-1.webp" ]`).
   - Properti wajib: `datePublished`, `dateModified`, `author`, `publisher` (merujuk ke `#localbusiness`), dan `"about": {"@id": "https://corporategifts.id/blog/[slug]#article"}`.

4. **Schema 4: BreadcrumbList**
   - 3 level ListItem berurutan:
     1. Beranda (`https://corporategifts.id/`)
     2. Blog (`https://corporategifts.id/blog`)
     3. [Judul Artikel] (`https://corporategifts.id/blog/[slug]`)

5. **Schema 5: FAQPage**
   - Selaras 1:1 dengan seluruh pertanyaan dan jawaban pada Accordion FAQ di body halaman.

---

## 4. Struktur Kerangka & Komponen Halaman

Kerangka HTML utuh mengacu pada `blog/_template_blueprint.html`. Wajib mematuhi struktur hierarki berikut:

1. **Tag `<main id="main" class="main">`**:
   - Membungkus:
     a. Breadcrumbs bar (`.breadcrumbs-bar`)
     b. Section py-5 (Grid 2 kolom: `.col-lg-8` konten artikel & `.col-lg-4` sidebar)
     c. Section py-5 bg-light (3 rekomendasi artikel terkait)
   - Ditutup `</main>` sebelum `<footer>`.

2. **Hierarki Konten Artikel (`.col-lg-8` > `.article-detail-wrap`)**:
   - `.article-header`: Badge kategori, tag `<h1>`, avatar penulis (44x44), nama penulis, tanggal update, waktu baca.
   - `.article-featured-img`: Gambar 1 (1200x675) + caption italic.
   - `.table-of-contents`: Tombol toggle collapsible (`#toc-header`, `#toc-list`, `#toc-toggle-btn`).
   - `.article-body`: Membungkus SELURUH konten isi teks, subbab, callout, tabel, gambar in-body, dan FAQ.
     - Paragraf pertama diawali: `<strong><a href="/" class="text-success text-decoration-none fw-bold">Corporate Gifts ID</a></strong> - ...`
     - `.article-key-points`: Box poin kunci ringkasan eksekutif dengan ikon bohlam.
     - `.article-baca-juga`: Badge baca juga + tautan artikel terkait.
     - `.article-inbody-img`: Gambar 2 (800x450) + caption italic.
     - `.tbl-wrap` > `table.tbl-corporategifts`: Tabel responsif (DILARANG inline `<style>`).
     - `#faq-section` > `.accordion.accordion-flush#blogFaqAccordion`: FAQ accordion Bootstrap.
   - `.blog-cta-banner`: Banner RFQ penawaran harga + tombol Minta Penawaran (`/minta-penawaran`) & WhatsApp CS.
   - `.article-author-box`: Kotak biografi penulis (avatar 90x90, nama, badge spesialisasi, bio, link `/penulis#[slug]`).
   - `.article-share-bar`: Tombol share WhatsApp, LinkedIn, Facebook, & Copy Link (`.btn-share`).

3. **Sidebar Kanan (`.col-lg-4` > `.sidebar.position-sticky`)**:
   - Widget 1: Kategori Produk Kami (6 link kategori produk).
   - Widget 2: Bantuan Konsultasi Kilat (Headset icon, nomor WA, CTA chat WhatsApp).
   - Widget 3: E-Katalog Resmi 2026 (Tombol download PDF `../assets/docs/katalog-corporategifts-id.pdf`).

4. **Section Artikel Terkait**:
   - 3 kartu artikel rekomendasi ber-badge kategori, gambar (400x225), excerpt, avatar penulis (30x30), dan tombol "Baca ->".
   - Verifikasi ketat bahwa file gambar di `assets/img/blog/` benar-benar ada di disk.

5. **Kebersihan Konten (Content Cleanliness)**:
   - Dilarang meninggalkan karakter markdown `*` (*italic*) atau `**` (**bold**), wajib tag HTML murni.
   - Zero em-dashes: Dilarang menggunakan tanda `—` atau `&mdash;`, selalu gunakan strip `-`.
   - Tautan internal natural ke produk (`/produk...`), katalog (`/katalog`), RFQ (`/minta-penawaran`), atau artikel blog (`/blog/[slug]`).

---

## 5. Checklist Sinkronisasi 6 Langkah Wajib

Setiap memigrasikan artikel, jalankan alur 6 langkah berikut secara berurutan:
1. `blog/<slug>.html`: Terapkan blueprint dan validasi 5 schema JSON-LD.
2. `blog.html`: Sisipkan kartu artikel baru pada urutan tanggal update kronologis menurun.
3. `sitemap.xml`: Tambahkan `<loc>https://corporategifts.id/blog/<slug></loc>` dan `<lastmod>YYYY-MM-DD</lastmod>`.
4. `_redirects`: Tambahkan 3 baris pengalihan 301 (Blogger legacy, legacy .html, trailing slash).
5. `llms.txt`: Sisipkan ringkasan 1 baris di bawah `# Blog & Artikel`.
6. `sitemap.html`: Sisipkan item pada kategori kartu yang relevan, perbarui nomor urut `N.`, dan update badge counter.

---

## 6. Referensi Pemetaan Penulis (Author Mapping)

| Nama di Excel | Target Anchor di `/penulis` | Jabatan Standar | Avatar Lokal |
| :--- | :--- | :--- | :--- |
| **Arinda Zakia** | `/penulis#arinda-zakia` | Senior Corporate Gifting Specialist | `../assets/img/penulis/arinda-zakia.webp` |
| **Amelia** / **Sholikhatun Nikmah** | `/penulis#sholikhatun-nikmah` | Creative Product Designer & Bespoke Packaging Consultant | `../assets/img/penulis/sholikhatun-nikmah.webp` |
| **Vendor Souvenir Kantor** | `/penulis#vendor-souvenir-kantor` | Senior Corporate Gifting Specialist | `../assets/img/penulis/vendor-souvenir-kantor.png` |

> [!IMPORTANT]
> **Aturan Amelia**: Jika di Excel tertulis "Amelia", wajib otomatis diganti ke "Sholikhatun Nikmah" dengan URL `/penulis#sholikhatun-nikmah` dan avatar `sholikhatun-nikmah.webp`. DILARANG memunculkan nama atau avatar lama "Amelia".
