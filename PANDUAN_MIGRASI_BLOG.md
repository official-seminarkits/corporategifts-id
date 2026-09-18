# SOP & Panduan Lengkap Migrasi Artikel Blog
**Project**: CorporateGifts.ID  
**Target Hosting**: Cloudflare Pages  
**Template Acuan Standar Emas**: `blog/hampers-bengkulu.html` & `blog/souvenir-event-perusahaan-jakarta.html`

---

## Standar Desain, Font, dan Komponen Resmi

Sebelum memulai migrasi, wajib mengikuti standar teknis berikut yang persis sama dengan acuan `blog/hampers-bengkulu.html`:

### 1. Standar Font Google
Seluruh halaman wajib memuat kombinasi resmi **Poppins** (untuk Judul/Headings) dan **Inter** (untuk Teks Body/Navigasi/Meta):
```html
  <!-- Fonts Preconnect & DNS-Prefetch -->
  <link rel="dns-prefetch" href="https://fonts.googleapis.com">
  <link rel="dns-prefetch" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com" rel="preconnect">
  <link href="https://fonts.gstatic.com" rel="preconnect" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap">
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
  <noscript>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  </noscript>
```

### 2. Tag Body
Tag body wajib menggunakan class:
```html
<body class="blog-detail-page">
```
*(Catatan: DILARANG menggunakan `blog-details-page` agar styling CSS `.blog-detail-page` di `main.min.css` aktif dengan sempurna).*

### 3. Header Navigasi Standar Lengkap
```html
  <!-- ══ HEADER ════════════════════════════════════════════════════════════════ -->
  <header id="header" class="header d-flex align-items-center sticky-top">
    <div class="container position-relative d-flex align-items-center justify-content-between">

      <a href="/" class="logo d-flex align-items-center me-auto me-xl-0">
        <img src="../assets/img/logo-header.png" alt="CorporateGifts.ID - Vendor Corporate Gift &amp; Souvenir Perusahaan"
          style="max-height:40px;width:auto;" width="214" height="40" loading="lazy">
      </a>

      <nav id="navmenu" class="navmenu mx-xl-auto">
        <ul>
          <li><a href="/">Beranda</a></li>
          <li><a href="/tentang-kami">Tentang Kami</a></li>
          <li><a href="/layanan">Layanan</a></li>
          <li><a href="/katalog">Katalog</a></li>
          <li><a href="/portofolio">Portofolio</a></li>
          <li class="dropdown">
            <a href="/produk"><span>Produk</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
            <ul>
              <li><a href="/produk/souvenir-kantor">Souvenir Kantor</a></li>
              <li><a href="/produk/souvenir-custom">Souvenir Custom</a></li>
              <li><a href="/produk/merchandise">Merchandise Perusahaan</a></li>
              <li><a href="/produk/seminar-kit">Seminar Kit</a></li>
              <li><a href="/produk/hampers">Hampers &amp; Parcel</a></li>
              <li><a href="/produk/souvenir-promosi">Paket Souvenir Promosi</a></li>
            </ul>
          </li>
          <li><a href="/blog" class="active">Blog</a></li>
          <li><a href="/galeri">Galeri</a></li>
        </ul>
        <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
      </nav>

      <a class="btn-getstarted"
        href="https://wa.me/62895639068080?text=Halo%2C%20saya%20ingin%20konsultasi%20souvenir%20kantor%20perusahaan" target="_blank"
        rel="noopener">
        <i class="bi bi-whatsapp me-1"></i> Hubungi Kami
      </a>

    </div>
  </header>
```

### 4. Breadcrumbs Bar Standar
```html
<div class="breadcrumbs-bar py-3 bg-white" style="border-bottom: 1px solid #f1f5f9;">
  <div class="container">
    <nav aria-label="breadcrumb" class="m-0 p-0" style="background: transparent;">
      <ol class="breadcrumb m-0 p-0" style="background: transparent; font-size: 0.88rem;">
        <li class="breadcrumb-item"><a href="/" style="color: var(--accent-color, #15803d); text-decoration: none; font-weight: 500;">Beranda</a></li>
        <li class="breadcrumb-item"><a href="/blog" style="color: var(--accent-color, #15803d); text-decoration: none; font-weight: 500;">Blog</a></li>
        <li class="breadcrumb-item active" aria-current="page" style="color: #64748b; font-weight: 500;">[Topik / Judul Singkat]</li>
      </ol>
    </nav>
  </div>
</div>
```

### 5. Article Header & Meta Bar Standar
```html
<div class="article-header">
  <span class="badge px-3 py-2 rounded-pill fw-semibold" style="background: rgba(22, 163, 74, 0.1); color: var(--accent-color, #16a34a); font-size: 0.82rem;">
    <i class="bi bi-tag-fill me-1"></i> [Kategori Artikel]
  </span>
  <h1>[Judul Lengkap H1 Artikel]</h1>
  
  <div class="article-meta-bar">
    <div class="d-flex align-items-center">
      <a href="/penulis#[slug-penulis]" class="d-inline-flex me-2">
        <img src="../assets/img/penulis/[slug-penulis].webp" alt="[Penulis] | CorporateGifts.ID" class="rounded-circle" width="44" height="44" loading="lazy" style="object-fit:cover;">
      </a>
      <div>
        <a href="/penulis#[slug-penulis]" class="text-dark d-block fw-bold text-decoration-none" style="font-size: 0.88rem;">[Nama Penulis]</a>
        <span class="text-muted" style="font-size: 0.76rem;">Senior Corporate Gifting Specialist</span>
      </div>
    </div>
    <div class="text-muted ms-auto">
      <i class="bi bi-calendar3 me-1"></i> [Tanggal Update dari Excel] &nbsp;|&nbsp; 
      <i class="bi bi-clock me-1"></i> [N] Menit Baca
    </div>
  </div>
</div>
```
*(Catatan: Tanggal yang digunakan selalu mengambil nilai dari kolom **Tanggal Update** / kolom sebelah kanan di Excel).*

### 6. Featured Image & In-Body Image Standar
```html
<!-- Featured Image (Atas TOC) -->
<div class="article-featured-img">
  <img src="../assets/img/blog/[slug-gambar-1].webp" 
       alt="[Alt Text Deskriptif] | CorporateGifts.ID" 
       class="img-fluid" loading="lazy" width="1200" height="675">
  <p class="text-muted text-center small mt-2 fst-italic">[Caption Ringkas Gambar Featured]</p>
</div>

<!-- In-Body Image (Di Tengah Konten) -->
<div class="article-inbody-img my-4">
  <img src="../assets/img/blog/[slug-gambar-2].webp" 
       alt="[Alt Text Deskriptif] | CorporateGifts.ID" 
       class="img-fluid rounded-4 shadow-sm w-100" loading="lazy" width="800" height="450">
  <p class="text-muted text-center small mt-2 fst-italic">[Caption Ringkas In-Body Image]</p>
</div>
```

### 7. Table of Contents (TOC) Standar
```html
<div class="table-of-contents">
  <div class="d-flex justify-content-between align-items-center" id="toc-header" style="cursor: pointer; user-select: none;">
    <h2 class="m-0 d-flex align-items-center">
      <i class="bi bi-list-nested text-success me-2"></i> Daftar Isi Artikel
    </h2>
    <button type="button" class="btn btn-sm btn-light border px-2 py-1 text-muted d-inline-flex align-items-center gap-1" id="toc-toggle-btn" aria-expanded="true" aria-controls="toc-list" style="border-radius: 6px;">
      <span id="toc-btn-text">Tutup</span>
      <i class="bi bi-chevron-up" id="toc-btn-icon"></i>
    </button>
  </div>
  <div id="toc-list" class="mt-2">
    <ol class="mb-0">
      <li><a href="#section-1">Sub Judul 1</a></li>
      <li><a href="#section-2">Sub Judul 2</a></li>
    </ol>
  </div>
</div>
```

### 8. Article Body, Poin Kunci & Callout Baca Juga
```html
<div class="article-body">
  <p>
    <strong><a href="/" class="text-success text-decoration-none fw-bold">Corporate Gifts ID</a></strong> - [Paragraf pembuka artikel...]
  </p>

  <!-- Box Poin Kunci / Ringkasan Eksekutif -->
  <div class="article-key-points">
    <h3 class="h6 fw-bold text-dark mb-2"><i class="bi bi-lightbulb-fill text-success me-2"></i> Poin Kunci [Topik]:</h3>
    <ul class="mb-0 small text-muted ps-3" style="line-height: 1.7;">
      <li><strong>[Label 1]:</strong> [Deskripsi 1]</li>
      <li><strong>[Label 2]:</strong> [Deskripsi 2]</li>
    </ul>
  </div>

  <!-- Strip Callout Baca Juga -->
  <div class="article-baca-juga">
    <span class="badge bg-success text-white px-2 py-1 rounded-pill small fw-bold">Baca Juga</span>
    <a href="/blog/[slug-artikel-terkait]" class="hover-green">[Judul Artikel Terkait] <i class="bi bi-arrow-right ms-1"></i></a>
  </div>

  <!-- Heading Konten Semantik Standar (Tanpa inline classes yang merusak) -->
  <h2 id="section-1">Judul Sub Bab H2</h2>
  <p>Paragraf teks...</p>
  
  <h3>1. Judul Sub Bab H3</h3>
  <ul>
    <li><strong>Item 1:</strong> Deskripsi item.</li>
  </ul>
</div>
```

### 9. Tabel Responsif Standar
```html
<div class="tbl-wrap">
  <table class="tbl-corporategifts">
    <thead>
      <tr>
        <th>Kolom 1</th>
        <th>Kolom 2</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td data-label="Kolom 1">Data 1</td>
        <td data-label="Kolom 2">Data 2</td>
      </tr>
    </tbody>
  </table>
</div>
```

### 10. Komponen FAQ Standar (Bootstrap Accordion)
```html
<div class="article-faq-compact my-4" id="faq-section">
  <h3 class="h5 fw-bold text-dark mb-3">
    <i class="bi bi-question-circle-fill text-success me-2"></i> Pertanyaan Seputar [Topik] (FAQ)
  </h3>
  
  <div class="accordion accordion-flush" id="blogFaqAccordion">

    <!-- FAQ Item 1 -->
    <div class="accordion-item border-bottom">
      <h4 class="accordion-header" id="faqHead1">
        <button class="accordion-button collapsed py-2 px-3 fw-semibold text-dark bg-white" type="button"
          data-bs-toggle="collapse" data-bs-target="#faqCollapse1" aria-expanded="false"
          aria-controls="faqCollapse1" style="font-size: 0.88rem;">
          1. [Pertanyaan 1]
        </button>
      </h4>
      <div id="faqCollapse1" class="accordion-collapse collapse" aria-labelledby="faqHead1"
        data-bs-parent="#blogFaqAccordion">
        <div class="accordion-body py-2 px-3 text-muted" style="line-height: 1.6; font-size: 0.84rem;">
          [Jawaban 1]
        </div>
      </div>
    </div>

    <!-- FAQ Item 2 s/d Item Terakhir (Item terakhir tanpa class border-bottom) -->
    <div class="accordion-item">
      <h4 class="accordion-header" id="faqHead5">
        <button class="accordion-button collapsed py-2 px-3 fw-semibold text-dark bg-white" type="button"
          data-bs-toggle="collapse" data-bs-target="#faqCollapse5" aria-expanded="false"
          aria-controls="faqCollapse5" style="font-size: 0.88rem;">
          5. [Pertanyaan 5]
        </button>
      </h4>
      <div id="faqCollapse5" class="accordion-collapse collapse" aria-labelledby="faqHead5"
        data-bs-parent="#blogFaqAccordion">
        <div class="accordion-body py-2 px-3 text-muted" style="line-height: 1.6; font-size: 0.84rem;">
          [Jawaban 5]
        </div>
      </div>
    </div>

  </div>
</div>
```

### 11. Bottom RFQ CTA Banner, Author Box & Share Bar Standar
```html
<!-- Bottom RFQ CTA Banner -->
<div class="card border-0 mt-5 shadow-sm text-center text-md-start blog-cta-banner">
  <div class="d-flex flex-column flex-md-row align-items-center justify-content-between gap-3">
    <div>
      <h3 class="h5 fw-bold text-dark mb-1">[Judul CTA Pengadaan]</h3>
      <p class="small text-muted mb-0">Dapatkan katalog resmi 2026, sampel mockup digital gratis, dan penawaran harga B2B terbaik yang lengkap dengan faktur pajak.</p>
    </div>
    <div class="blog-cta-actions flex-shrink-0">
      <a href="/minta-penawaran" class="btn btn-success rounded-pill px-4 py-2 fw-semibold" style="background: var(--accent-color, #16a34a); border-color: var(--accent-color, #16a34a);">
        <i class="bi bi-pencil-square me-1"></i> Minta Penawaran
      </a>
      <a href="https://wa.me/62895639068080?text=Halo%20CorporateGifts.ID,%20saya%20ingin%20konsultasi" target="_blank" rel="noopener" class="btn btn-outline-success rounded-pill px-3 py-2 fw-semibold">
        <i class="bi bi-whatsapp me-1"></i> WhatsApp CS
      </a>
    </div>
  </div>
</div>

<!-- Author Box -->
<div class="article-author-box mt-4">
  <a href="/penulis#[slug-penulis]" class="flex-shrink-0 me-3">
    <img src="../assets/img/penulis/[slug-penulis].webp" alt="[Nama Penulis] | CorporateGifts.ID" width="90" height="90" loading="lazy" class="rounded-circle shadow-sm" style="object-fit:cover;">
  </a>
  <div>
    <h3 class="h6 fw-bold text-dark mb-1">
      Ditulis oleh: <a href="/penulis#[slug-penulis]" class="text-dark text-decoration-none hover-green">[Nama Penulis]</a>
    </h3>
    <span class="badge bg-success-subtle text-success px-2 py-1 rounded-pill small fw-semibold mb-2 d-inline-block">[Spesialisasi Penulis]</span>
    <p class="small text-muted mb-2">
      [Bio Penulis]
    </p>
    <a href="/penulis#[slug-penulis]" class="text-success small fw-semibold text-decoration-none">
      Lihat Profil Lengkap &amp; Panduan Lainnya <i class="bi bi-arrow-right ms-1"></i>
    </a>
  </div>
</div>

<!-- Share Bar (Wajib Menggunakan Class .btn-share) -->
<div class="article-share-bar">
  <div class="fw-semibold small text-dark">Bagikan Artikel Ini:</div>
  <div class="article-share-buttons">
    <a href="https://api.whatsapp.com/send?text=[Judul]%20https://corporategifts.id/blog/[slug]" target="_blank" rel="noopener" class="btn-share btn-wa" aria-label="Share via WhatsApp"><i class="bi bi-whatsapp"></i></a>
    <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://corporategifts.id/blog/[slug]" target="_blank" rel="noopener" class="btn-share btn-li" aria-label="Share on LinkedIn"><i class="bi bi-linkedin"></i></a>
    <a href="https://www.facebook.com/sharer/sharer.php?u=https://corporategifts.id/blog/[slug]" target="_blank" rel="noopener" class="btn-share btn-fb" aria-label="Share on Facebook"><i class="bi bi-facebook"></i></a>
    <button onclick="navigator.clipboard.writeText(window.location.href); alert('Tautan artikel berhasil disalin!');" class="btn-share btn-copy border-0" aria-label="Copy Link"><i class="bi bi-link-45deg"></i></button>
  </div>
</div>
```

### 12. Section Rekomendasi Artikel Terkait (3 Kartu Standar)
```html
<section class="py-5 bg-light border-top">
  <div class="container" data-aos="fade-up">
    <div class="d-flex flex-wrap justify-content-between align-items-center mb-4 gap-2">
      <div>
        <span class="text-uppercase fw-bold small text-success" style="letter-spacing:1px;">Rekomendasi Wawasan</span>
        <h2 class="h3 fw-bold text-dark mb-0 mt-1">Artikel Terkait Lainnya</h2>
      </div>
      <a href="/blog" class="btn btn-sm btn-outline-success rounded-pill px-3 py-2 fw-semibold">
        Lihat Semua Artikel <i class="bi bi-arrow-right ms-1"></i>
      </a>
    </div>
    <div class="row g-4">
      <!-- Card Template 1, 2, 3 -->
      <div class="col-lg-4 col-md-6" data-aos="fade-up">
        <div class="card h-100 border-0 shadow-sm rounded-4 overflow-hidden bg-white">
          <div class="position-relative">
            <span class="badge position-absolute top-0 start-0 m-3 px-3 py-1 rounded-pill bg-success text-white" style="font-size:0.75rem;">[Kategori]</span>
            <img src="../assets/img/blog/[img-terkait].webp" alt="[Judul] - CorporateGifts.ID" class="card-img-top" loading="lazy" width="400" height="225" style="height: 200px; object-fit: cover;">
          </div>
          <div class="card-body p-4 d-flex flex-column">
            <p class="text-success small fw-semibold mb-2">[Sub Kategori]</p>
            <h3 class="h6 fw-bold text-dark mb-2" style="line-height:1.4;">
              <a href="/blog/[slug-terkait]" class="text-dark text-decoration-none hover-green">[Judul Artikel Terkait]</a>
            </h3>
            <p class="text-muted small mb-3 flex-grow-1" style="line-height:1.6; font-size:0.85rem;">
              [Ringkasan deskripsi 1-2 kalimat].
            </p>
            <div class="d-flex align-items-center justify-content-between pt-3 border-top mt-auto">
              <div class="d-flex align-items-center">
                <img src="../assets/img/penulis/[slug-penulis].webp" alt="[Penulis] - CorporateGifts.ID" class="rounded-circle me-2" width="30" height="30" style="object-fit:cover;">
                <span class="small fw-semibold text-dark" style="font-size:0.82rem;">[Nama Penulis]</span>
              </div>
              <a href="/blog/[slug-terkait]" class="text-success small fw-bold text-decoration-none" aria-label="Baca artikel [Judul]">
                Baca <i class="bi bi-arrow-right"></i>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

### 13. Footer Standar Lengkap, Floating WhatsApp & Scripts
```html
  <!-- ══ FOOTER ════════════════════════════════════════════════════════════════ -->
  <footer id="footer" class="footer dark-background">

    <div class="container footer-top">
      <div class="row gy-4">

        <div class="col-lg-4 col-md-12 footer-about">
          <a href="/" class="logo d-inline-flex align-items-center bg-white py-2 px-3 rounded mb-3">
            <img src="../assets/img/logo-header.png" alt="CorporateGifts.ID - Vendor Corporate Gift &amp; Souvenir Perusahaan"
              style="max-height:40px;width:auto;" width="214" height="40" loading="lazy">
          </a>
          <p>Vendor corporate gift, souvenir perusahaan premium, dan merchandise kantor eksklusif untuk branding dan
            promosi bisnis Anda. Melayani seluruh Indonesia.</p>
          <div class="social-links d-flex mt-4">
            <a href="https://wa.me/62895639068080" target="_blank" rel="noopener" aria-label="WhatsApp"><i
                class="bi bi-whatsapp"></i></a>
            <a href="https://www.instagram.com/corporategifts.id" target="_blank" rel="noopener"
              aria-label="Instagram"><i class="bi bi-instagram"></i></a>
            <a href="https://www.facebook.com/corporategiftsid" target="_blank" rel="noopener" aria-label="Facebook"><i
                class="bi bi-facebook"></i></a>
            <a href="https://www.tiktok.com/@corporategifts.id" target="_blank" rel="noopener" aria-label="TikTok"><i
                class="bi bi-tiktok"></i></a>
          </div>
        </div>

        <div class="col-lg-2 col-6 footer-links">
          <h3>Halaman</h3>
          <ul>
            <li><a href="/">Beranda</a></li>
            <li><a href="/tentang-kami">Tentang Kami</a></li>
            <li><a href="/layanan">Layanan</a></li>
            <li><a href="/katalog">Katalog</a></li>
            <li><a href="/portofolio">Portofolio</a></li>
            <li><a href="/blog">Blog</a></li>
            <li><a href="/galeri">Galeri</a></li>
            <li><a href="/sitemap">Sitemap</a></li>
          </ul>
        </div>

        <div class="col-lg-2 col-6 footer-links">
          <h3>Produk</h3>
          <ul>
            <li><a href="/produk/souvenir-kantor">Souvenir Kantor</a></li>
            <li><a href="/produk/souvenir-custom">Souvenir Custom</a></li>
            <li><a href="/produk/merchandise">Merchandise Perusahaan</a></li>
            <li><a href="/produk/seminar-kit">Paket Seminar Kit</a></li>
            <li><a href="/produk/hampers">Hampers &amp; Parcel</a></li>
            <li><a href="/produk/souvenir-promosi">Paket Souvenir Promosi</a></li>
          </ul>
        </div>

        <div class="col-lg-4 col-md-12 footer-contact text-center text-md-start">
          <h3>Hubungi Kami</h3>
          <p>Jawa Timur, Indonesia</p>
          <p class="mt-3"><strong>WhatsApp:</strong>
            <a href="https://wa.me/62895639068080" target="_blank" rel="noopener" style="color:inherit;"> +62
              895-6390-68080</a>
          </p>
          <p><strong>Website:</strong>
            <a href="https://corporategifts.id" style="color:inherit;">corporategifts.id</a>
          </p>
        </div>

      </div>
    </div>

    <div class="container py-3" style="border-top:1px solid rgba(255,255,255,.1)">
      <p class="text-center mb-2" style="font-size:.85rem;opacity:.7;font-weight:600;">Partner Network</p>
      <div class="d-flex flex-wrap justify-content-center gap-3" style="font-size:.82rem;">
        <a href="https://seminarkits.id/" target="_blank" rel="noopener"
          style="color:rgba(255,255,255,.65);">SeminarKits.ID</a>
        <a href="https://vendormerchandise.web.id/" target="_blank" rel="noopener"
          style="color:rgba(255,255,255,.65);">Vendor Merchandise</a>
        <a href="https://vendorsouvenirkantor.web.id/" target="_blank" rel="noopener"
          style="color:rgba(255,255,255,.65);">Vendor Souvenir Kantor</a>
        <a href="https://hampersmalang.web.id/" target="_blank" rel="noopener"
          style="color:rgba(255,255,255,.65);">Vendor Hampers Malang</a>
        <a href="https://vendorsouvenir.web.id/" target="_blank" rel="noopener"
          style="color:rgba(255,255,255,.65);">Vendor Souvenir</a>
      </div>
    </div>

    <div class="container copyright text-center mt-4">
      <p>&copy; <span id="year"></span> <strong class="px-1 sitename">CorporateGifts.ID</strong> <span>- Vendor
          Corporate Gift, Souvenir Perusahaan &amp; Merchandise Kantor. All Rights Reserved.</span></p>
    </div>

  </footer>

  <!-- Floating WhatsApp Button -->
  <a href="https://wa.me/62895639068080?text=Halo%2C%20saya%20ingin%20konsultasi%20pengadaan%20corporate%20gift" 
     class="floating-wa d-flex align-items-center justify-content-center" 
     target="_blank" 
     rel="noopener" 
     aria-label="Konsultasi via WhatsApp">
    <i class="bi bi-whatsapp"></i>
    <span class="wa-tooltip">Chat via WhatsApp</span>
  </a>

  <!-- Scroll Top -->
  <a href="#" id="scroll-top" class="scroll-top d-flex align-items-center justify-content-center" aria-label="Kembali ke atas"><i
      class="bi bi-arrow-up-short"></i></a>

  <!-- Vendor JS Files -->
  <script src="../assets/vendor/bootstrap/js/bootstrap.bundle.min.js" defer></script>
  <script src="../assets/vendor/aos/aos.js" defer></script>
  <script src="../assets/vendor/glightbox/js/glightbox.min.js" defer></script>

  <!-- Main JS File -->
  <script src="../assets/js/main.min.js" defer></script>

  <!-- Auto-update copyright year -->
  <script>document.getElementById('year').textContent = new Date().getFullYear();</script>

  <!-- Table of Contents Toggle (Buka/Tutup) -->
  <script>
    (function() {
      const tocHeader = document.getElementById('toc-header');
      const tocList = document.getElementById('toc-list');
      const tocBtnText = document.getElementById('toc-btn-text');
      const tocBtnIcon = document.getElementById('toc-btn-icon');
      const tocToggleBtn = document.getElementById('toc-toggle-btn');

      if (tocHeader && tocList) {
        function toggleTOC() {
          const isClosed = tocList.classList.contains('d-none');
          if (isClosed) {
            tocList.classList.remove('d-none');
            if (tocBtnText) tocBtnText.textContent = 'Tutup';
            if (tocBtnIcon) tocBtnIcon.className = 'bi bi-chevron-up';
            if (tocToggleBtn) tocToggleBtn.setAttribute('aria-expanded', 'true');
          } else {
            tocList.classList.add('d-none');
            if (tocBtnText) tocBtnText.textContent = 'Buka';
            if (tocBtnIcon) tocBtnIcon.className = 'bi bi-chevron-down';
            if (tocToggleBtn) tocToggleBtn.setAttribute('aria-expanded', 'false');
          }
        }
        tocHeader.addEventListener('click', toggleTOC);
        if (tocToggleBtn) {
          tocToggleBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            toggleTOC();
          });
        }
      }
    })();
  </script>
```

---

## Alur Kerja Setiap Migrasi Artikel (Checklist 6 Langkah Wajib)

Setiap migrasi 1 artikel baru, jalankan alur 6 langkah berikut secara berurutan:

```
[1. Buat blog/<slug>.html (Clean URL, non-trailing slash)] 
       ↓
[2. Update blog.html (urut tanggal update kronologis menurun, link ke /blog/<slug>)] 
       ↓
[3. Update sitemap.xml (<loc>https://corporategifts.id/blog/<slug></loc>)] 
       ↓
[4. Update _redirects (Wajib 3 Bagian: Blogger 301, Legacy .html 301, & Trailing Slash 301)] 
       ↓
[5. Update llms.txt (Ringkasan 1 baris ke https://corporategifts.id/blog/<slug>)] 
       ↓
[6. Update sitemap.html (Sisipkan ke kategori kartu yang relevan & update counter)] 
```

---

## Referensi Pemetaan Penulis (Author Mapping)

| Nama Penulis di Excel | Target Anchor di `/penulis` | Jabatan Standar | Avatar Lokal |
| :--- | :--- | :--- | :--- |
| **Arinda Zakia** | `/penulis#arinda-zakia` | Senior Corporate Gifting Specialist | `../assets/img/penulis/arinda-zakia.webp` |
| **Sholikhatun Nikmah** | `/penulis#sholikhatun-nikmah` | Senior Corporate Gifting Specialist | `../assets/img/penulis/sholikhatun-nikmah.webp` |
| **Vendor Souvenir Kantor** | `/penulis#vendor-souvenir-kantor` | Senior Corporate Gifting Specialist | `../assets/img/penulis/vendor-souvenir-kantor.png` |
*(DILARANG menggunakan nama atau avatar lama "Amelia").*
