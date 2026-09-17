# Blog Detail Migration Rules & Standard Architecture

## 1. Scope & Baseline Standard
Setiap artikel detail blog di `blog/<slug>.html` wajib mengikuti standar blueprint resmi yang mengacu pada `blog/souvenir-kantor-pajak.html` (Artikel #56) dan `blog/tren-seminar-kit-korporat-terbaru-2026.html` (Artikel #57).

## 2. Struktur HTML & Elemen Wajib
1. **Body Class**: `<body class="blog-detail-page">` (DILARANG menggunakan `blog-details-page`).
2. **Fonts & Preconnect**: Poppins (500, 600, 700) + Inter (400, 500, 600, 700) dengan preload dan fallback print media.
3. **Header Navigasi**:
   - Logo dengan link `/` dan atribut lengkap: `<img src="../assets/img/logo-header.png" alt="CorporateGifts.ID - Vendor Corporate Gift &amp; Souvenir Perusahaan" style="max-height:40px;width:auto;" width="214" height="40" loading="lazy">`
   - Menu lengkap: Beranda, Tentang Kami, Layanan, Katalog, Portofolio, Dropdown Produk (6 sub-menu), Blog (class active), Galeri.
   - Tombol CTA Hubungi Kami WhatsApp.
4. **Breadcrumbs Bar**: Bar putih dengan border bottom tipis, 3 tingkat: Beranda (`/`) > Blog (`/blog`) > Judul Singkat.
5. **Article Header & Meta Bar**:
   - Badge kategori hijau muda pill.
   - Title `<h1>` semantik.
   - Meta bar memuat avatar penulis 44x44 bulat (`../assets/img/penulis/[slug].webp`), nama penulis link ke `/penulis#[slug]`, jabatan, tanggal update (dari kolom kanan Excel), dan estimasi waktu baca.
6. **Featured Image**: `.article-featured-img` dengan gambar lokal WebP berdimensi `1200x675` + caption italic di bawahnya.
7. **Table of Contents (TOC)**: Container `.table-of-contents` dengan toggle button interaktif (`#toc-header`, `#toc-toggle-btn`, `#toc-list`).
8. **Paragraf Pembuka**: Wajib diawali `<strong><a href="/" class="text-success text-decoration-none fw-bold">Corporate Gifts ID</a></strong> - ...`
9. **Kotak Poin Kunci**: `.article-key-points` dengan icon lampu hijau, list ringkasan eksekutif.
10. **Callout Baca Juga**: `.article-baca-juga` dengan badge hijau dan tautan ke `/blog/[slug]`.
11. **Tabel Data**: Wajib dibungkus `<div class="tbl-wrap"><table class="tbl-corporategifts">...</table></div>`. DILARANG menyisipkan inline `<style>` tabel di `<head>`.
12. **FAQ Accordion & Schema**: Minimal 5 item FAQ yang sinkron 1:1 antara accordion `#blogFaqAccordion` dan schema `FAQPage` JSON-LD.
13. **Bottom RFQ Banner**: `.blog-cta-banner` dengan tombol "Minta Penawaran" (`/minta-penawaran`) dan "WhatsApp CS".
14. **Author Box**: `.article-author-box` dengan foto 90x90 (`../assets/img/penulis/[slug].webp`), bio, badge keahlian, dan tautan profil lengkap ke `/penulis#[slug]`.
15. **Share Bar**: Tombol share WhatsApp, LinkedIn, Facebook, dan Copy Link dengan alert JS.
16. **Sidebar Kanan (3 Widget)**:
    - Widget 1: Kategori Produk Kami (6 link).
    - Widget 2: Bantuan Konsultasi Kilat (+62 895-6390-68080).
    - Widget 3: E-Katalog Resmi 2026 PDF (`../assets/docs/katalog-corporategifts-id.pdf`).
17. **Section Artikel Terkait**: 3 kartu rekomendasi dengan badge, excerpt, author footer, dan tautan ke `/blog/[slug]`.

## 3. Formatting & Content Constraints
- **HTML Semantik Murni**: DILARANG menyisakan karakter markdown `*` atau `**`. Konversi ke `<em>` dan `<strong>`.
- **Zero Em-Dashes**: DILARANG menggunakan karakter em-dash (`—` / `&mdash;`). Selalu gunakan strip biasa `-`.
- **Clean URLs**: Semua link internal ke blog menggunakan `/blog/<slug>` tanpa `.html` dan tanpa trailing slash.
- **Internal Linking**: Sisipkan tautan natural ke `/produk/...`, `/katalog`, `/minta-penawaran`, dan artikel blog terkait.

## 4. Author Source of Truth
- **Arinda Zakia**: `/penulis#arinda-zakia` | `../assets/img/penulis/arinda-zakia.webp`
- **Sholikhatun Nikmah**: `/penulis#sholikhatun-nikmah` | `../assets/img/penulis/sholikhatun-nikmah.webp`
- **Vendor Souvenir Kantor**: `/penulis#vendor-souvenir-kantor` | `../assets/img/penulis/vendor-souvenir-kantor.png`
*(DILARANG menggunakan nama "Amelia").*

## 5. Schema.org JSON-LD (5 Blok Wajib)
1. `LocalBusiness & Organization`: `@id: "https://corporategifts.id/#localbusiness"`
2. `Article (Utama)`: `@id: "https://corporategifts.id/blog/<slug>#article"`, `mainEntityOfPage: "https://corporategifts.id/blog/<slug>"`
3. `Article (Ringkasan Eksekutif)`: `@id: "https://corporategifts.id/blog/<slug>#summary"`, `about: "https://corporategifts.id/blog/<slug>#article"`
4. `BreadcrumbList`: 3 tingkat (Beranda > Blog > Judul)
5. `FAQPage`: Array Pertanyaan & Jawaban yang sinkron 1:1 dengan accordion.

## 6. Alur 6 Langkah Sinkronisasi Migrasi
1. `blog/<slug>.html` (detail artikel baru).
2. `blog.html` (kartu blog baru disisipkan secara kronologis menurun).
3. `sitemap.xml` (tambahkan `<loc>` dan `<lastmod>` dengan format ISO YYYY-MM-DD).
4. `_redirects` (wajib di 3 bagian: Blogger 301, Legacy .html 301, dan Trailing slash 301).
5. `llms.txt` (ringkasan 1 baris di bawah `# Blog & Artikel`).
6. `sitemap.html` (sisipkan item pada kategori kartu sitemap yang relevan, perbarui nomor urut `N.`, badge kategori, dan total counter banner).
