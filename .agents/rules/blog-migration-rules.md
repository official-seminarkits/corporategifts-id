# Blog Detail Migration Rules & Standard Architecture

## 1. Scope & Baseline Standard
Setiap artikel detail blog di `blog/<slug>.html` WAJIB mengikuti standar blueprint resmi yang mengacu 100% pada `blog/hampers-bengkulu.html` dan `blog/souvenir-event-perusahaan-jakarta.html`.

DILARANG mengubah atau memvariasikan struktur, tag pembungkus, kelas CSS, atau urutan elemen.

---

## 2. Blueprint Kerangka HTML Wajib (100% Identik)

```html
<!DOCTYPE html>
<html lang="id">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">

  <!-- ======= SEO, AEO, & GEO OPTIMIZATION ======= -->
  <title>[Judul Artikel] | CorporateGifts.ID</title>
  <meta name="description" content="[Deskripsi]">
  <meta name="keywords" content="[Keywords]">
  <meta name="author" content="[Penulis]">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <link rel="canonical" href="https://corporategifts.id/blog/[slug]">

  <!-- GEO Meta Tags -->
  <meta name="geo.region" content="ID">
  <meta name="geo.placename" content="Indonesia">
  <meta name="geo.position" content="-7.2575;112.7521">
  <meta name="ICBM" content="-7.2575, 112.7521">

  <!-- Open Graph (OG) -->
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://corporategifts.id/blog/[slug]">
  <meta property="og:title" content="[Judul Artikel]">
  <meta property="og:description" content="[Deskripsi]">
  <meta property="og:image" content="https://corporategifts.id/assets/img/blog/[featured-img].webp">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675">
  <meta property="og:site_name" content="CorporateGifts.ID">
  <meta property="og:locale" content="id_ID">
  <meta property="article:published_time" content="[YYYY-MM-DDTHH:mm:ss+07:00]">
  <meta property="article:modified_time" content="[YYYY-MM-DDTHH:mm:ss+07:00]">
  <meta property="article:section" content="[Kategori]">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="https://corporategifts.id/blog/[slug]">
  <meta name="twitter:title" content="[Judul Artikel]">
  <meta name="twitter:description" content="[Deskripsi]">
  <meta name="twitter:image" content="https://corporategifts.id/assets/img/blog/[featured-img].webp">

  <!-- Favicons -->
  <link href="../assets/img/favicon.png" rel="icon">
  <link href="../assets/img/apple-touch-icon.png" rel="apple-touch-icon">

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

  <!-- Vendor CSS Files -->
  <link rel="preload" href="../assets/vendor/bootstrap/css/bootstrap.min.css" as="style">
  <link rel="preload" href="../assets/css/main.min.css" as="style">
  <link href="../assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="../assets/css/main.min.css" rel="stylesheet">
  <link href="../assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet" media="print" onload="this.media='all'">
  <noscript><link href="../assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet"></noscript>
  <link href="../assets/vendor/aos/aos.css" rel="stylesheet" media="print" onload="this.media='all'">
  <noscript><link href="../assets/vendor/aos/aos.css" rel="stylesheet"></noscript>
  <link href="../assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">

  <!-- ======= 5 JSON-LD SCHEMAS ======= -->
  <!-- 1. LocalBusiness & Organization -->
  <!-- 2. Article (Utama) -->
  <!-- 3. Article (Ringkasan Eksekutif) + WAJIB properti image -->
  <!-- 4. BreadcrumbList (3 levels) -->
  <!-- 5. FAQPage (Sinkron 1:1) -->
</head>

<body class="blog-detail-page">

  <!-- ══ HEADER ════════════════════════════════════════════════════════════════ -->
  <header id="header" class="header d-flex align-items-center sticky-top">
    <div class="container position-relative d-flex align-items-center justify-content-between">
      <a href="/" class="logo d-flex align-items-center me-auto me-xl-0">
        <img src="../assets/img/logo-header.png" alt="CorporateGifts.ID - Vendor Corporate Gift &amp; Souvenir Perusahaan" style="max-height:40px;width:auto;" width="214" height="40" loading="lazy">
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
              <li><a href="/produk/seminar-kit">Paket Seminar Kit</a></li>
              <li><a href="/produk/hampers">Hampers &amp; Parcel</a></li>
              <li><a href="/produk/souvenir-promosi">Paket Souvenir Promosi</a></li>
            </ul>
          </li>
          <li><a href="/blog" class="active">Blog</a></li>
          <li><a href="/galeri">Galeri</a></li>
        </ul>
        <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
      </nav>
      <a class="btn-getstarted" href="https://wa.me/62895639068080?text=Halo%2C%20saya%20ingin%20konsultasi%20..." target="_blank" rel="noopener">
        <i class="bi bi-whatsapp me-1"></i> Hubungi Kami
      </a>
    </div>
  </header>

  <main id="main" class="main">

    <!-- ══ BREADCRUMBS ════════════════════════════════════════════════════════ -->
    <div class="breadcrumbs-bar py-3 bg-white" style="border-bottom: 1px solid #f1f5f9;">
      <div class="container">
        <nav aria-label="breadcrumb" class="m-0 p-0" style="background: transparent;">
          <ol class="breadcrumb m-0 p-0" style="background: transparent; font-size: 0.88rem;">
            <li class="breadcrumb-item"><a href="/" style="color: var(--accent-color, #15803d); text-decoration: none; font-weight: 500;">Beranda</a></li>
            <li class="breadcrumb-item"><a href="/blog" style="color: var(--accent-color, #15803d); text-decoration: none; font-weight: 500;">Blog</a></li>
            <li class="breadcrumb-item active" aria-current="page" style="color: #64748b; font-weight: 500;">[Topik / Judul]</li>
          </ol>
        </nav>
      </div>
    </div>

    <!-- ══ MAIN ARTICLE & SIDEBAR SECTION ════════════════════════════════════ -->
    <section class="py-5">
      <div class="container" data-aos="fade-up">
        <div class="row g-5">

          <!-- Left Column: Article Content -->
          <div class="col-lg-8">
            <article class="article-detail-wrap">

              <!-- Article Header -->
              <div class="article-header">
                <span class="badge px-3 py-2 rounded-pill fw-semibold" style="background: rgba(22, 163, 74, 0.1); color: var(--accent-color, #16a34a); font-size: 0.82rem;">
                  <i class="bi bi-[icon] me-1"></i> [Kategori]
                </span>
                <h1>[Judul Artikel]</h1>
                
                <div class="article-meta-bar">
                  <div class="d-flex align-items-center">
                    <a href="/penulis#[slug]" class="d-inline-flex me-2">
                      <img src="../assets/img/penulis/[slug].webp" alt="[Nama Penulis] | CorporateGifts.ID" class="rounded-circle" width="44" height="44" loading="lazy" style="object-fit:cover;">
                    </a>
                    <div>
                      <a href="/penulis#[slug]" class="text-dark d-block fw-bold text-decoration-none" style="font-size: 0.88rem;">[Nama Penulis]</a>
                      <span class="text-muted" style="font-size: 0.76rem;">Senior Corporate Gifting Specialist</span>
                    </div>
                  </div>
                  <div class="text-muted ms-auto">
                    <i class="bi bi-calendar3 me-1"></i> [Tanggal Update Indonesia] &nbsp;|&nbsp; 
                    <i class="bi bi-clock me-1"></i> [N] Menit Baca
                  </div>
                </div>
              </div>

              <!-- Featured Image -->
              <div class="article-featured-img">
                <img src="../assets/img/blog/[img-1].webp" alt="[Alt Image 1]" class="img-fluid" loading="lazy" width="1200" height="675">
                <p class="text-muted text-center small mt-2 fst-italic">[Caption Image 1]</p>
              </div>

              <!-- Table of Contents (Daftar Isi) -->
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
                    <!-- Heading links -->
                  </ol>
                </div>
              </div>

              <!-- Article Body -->
              <div class="article-body">
                <p><strong><a href="/" class="text-success text-decoration-none fw-bold">Corporate Gifts ID</a></strong> - [Isi Paragraf Pembuka...]</p>

                <!-- Poin Kunci -->
                <div class="article-key-points">
                  <h3 class="h6 fw-bold text-dark mb-2"><i class="bi bi-lightbulb-fill text-success me-2"></i> Poin Kunci ...:</h3>
                  <ul class="mb-0 small text-muted ps-3" style="line-height: 1.7;">
                    <li><strong>...:</strong> ...</li>
                  </ul>
                </div>

                <!-- Callout Baca Juga -->
                <div class="article-baca-juga">
                  <span class="badge bg-success text-white px-2 py-1 rounded-pill small fw-bold">Baca Juga</span>
                  <a href="/blog/[slug-terkait]" class="hover-green">[Judul Artikel Terkait] <i class="bi bi-arrow-right ms-1"></i></a>
                </div>

                <!-- In-Body Image -->
                <div class="article-inbody-img my-4">
                  <img src="../assets/img/blog/[img-2].webp" alt="[Alt Image 2]" class="img-fluid rounded-4 shadow-sm w-100" loading="lazy" width="800" height="450">
                  <p class="text-muted text-center small mt-2 fst-italic">[Caption Image 2]</p>
                </div>

                <!-- Responsive Table -->
                <div class="tbl-wrap">
                  <table class="tbl-corporategifts">
                    <thead>...</thead>
                    <tbody>...</tbody>
                  </table>
                </div>

                <!-- FAQ Accordion -->
                <div id="faq-section" class="article-faq-compact my-4">
                  <h3 class="h5 fw-bold text-dark mb-3"><i class="bi bi-patch-question text-success me-2"></i> Pertanyaan Seputar ... (FAQ)</h3>
                  <div class="accordion accordion-flush" id="blogFaqAccordion">
                    <!-- Accordion Items -->
                  </div>
                </div>

                <!-- Kesimpulan -->
                <h2 id="kesimpulan-praktis">Kesimpulan Praktis</h2>
                <p>...</p>
              </div><!-- End Article Body -->

              <!-- Bottom RFQ CTA Banner -->
              <div class="card border-0 mt-5 shadow-sm text-center text-md-start blog-cta-banner">
                <div class="d-flex flex-column flex-md-row align-items-center justify-content-between gap-3">
                  <div>
                    <h3 class="h5 fw-bold text-dark mb-1">[Heading CTA Banner]</h3>
                    <p class="small text-muted mb-0">[Deskripsi CTA Banner]</p>
                  </div>
                  <div class="blog-cta-actions flex-shrink-0">
                    <a href="/minta-penawaran" class="btn btn-success rounded-pill px-4 py-2 fw-semibold" style="background: var(--accent-color, #16a34a); border-color: var(--accent-color, #16a34a);">
                      <i class="bi bi-pencil-square me-1"></i> Minta Penawaran
                    </a>
                    <a href="https://wa.me/62895639068080?text=Halo%20CorporateGifts.ID,%20saya%20ingin%20konsultasi%20..." target="_blank" rel="noopener" class="btn btn-outline-success rounded-pill px-3 py-2 fw-semibold">
                      <i class="bi bi-whatsapp me-1"></i> WhatsApp CS
                    </a>
                  </div>
                </div>
              </div>

              <!-- Author Box -->
              <div class="article-author-box mt-4">
                <a href="/penulis#[slug]" class="flex-shrink-0 me-3">
                  <img src="../assets/img/penulis/[slug].webp" alt="[Nama] | CorporateGifts.ID" width="90" height="90" loading="lazy" class="rounded-circle shadow-sm" style="object-fit:cover;">
                </a>
                <div>
                  <h3 class="h6 fw-bold text-dark mb-1">
                    Ditulis oleh: <a href="/penulis#[slug]" class="text-dark text-decoration-none hover-green">[Nama]</a>
                  </h3>
                  <span class="badge bg-success-subtle text-success px-2 py-1 rounded-pill small fw-semibold mb-2 d-inline-block">Senior Corporate Gifting Specialist &amp; Content Strategist</span>
                  <p class="small text-muted mb-2">[Bio Penulis]</p>
                  <a href="/penulis#[slug]" class="text-success small fw-semibold text-decoration-none">
                    Lihat Profil Lengkap &amp; Panduan Lainnya <i class="bi bi-arrow-right ms-1"></i>
                  </a>
                </div>
              </div>

              <!-- Share Bar -->
              <div class="article-share-bar">
                <div class="fw-semibold small text-dark">Bagikan Artikel Ini:</div>
                <div class="article-share-buttons">
                  <a href="https://api.whatsapp.com/send?text=..." target="_blank" rel="noopener" class="btn-share btn-wa" aria-label="Share via WhatsApp"><i class="bi bi-whatsapp"></i></a>
                  <a href="https://www.linkedin.com/sharing/share-offsite/?url=..." target="_blank" rel="noopener" class="btn-share btn-li" aria-label="Share on LinkedIn"><i class="bi bi-linkedin"></i></a>
                  <a href="https://www.facebook.com/sharer/sharer.php?u=..." target="_blank" rel="noopener" class="btn-share btn-fb" aria-label="Share on Facebook"><i class="bi bi-facebook"></i></a>
                  <button onclick="navigator.clipboard.writeText(window.location.href); alert('Tautan artikel berhasil disalin!');" class="btn-share btn-copy border-0" aria-label="Copy Link"><i class="bi bi-link-45deg"></i></button>
                </div>
              </div>

            </article>
          </div><!-- End Left Column -->

          <!-- Right Column: Sidebar -->
          <div class="col-lg-4">
            <div class="sidebar position-sticky" style="top: 100px;">
              <!-- Widget 1: Kategori Produk Kami -->
              <div class="card border-0 rounded-4 p-4 shadow-sm bg-white mb-4">
                <h3 class="h6 fw-bold text-dark mb-3"><i class="bi bi-grid-fill text-success me-2"></i> Kategori Produk Kami</h3>
                <ul class="list-unstyled mb-0" style="font-size: 0.92rem;">
                  <li class="py-2 border-bottom"><a href="/produk/souvenir-kantor" class="text-decoration-none text-dark d-flex justify-content-between"><span>Souvenir Kantor</span> <i class="bi bi-chevron-right text-muted"></i></a></li>
                  <li class="py-2 border-bottom"><a href="/produk/souvenir-custom" class="text-decoration-none text-dark d-flex justify-content-between"><span>Souvenir Custom VIP</span> <i class="bi bi-chevron-right text-muted"></i></a></li>
                  <li class="py-2 border-bottom"><a href="/produk/merchandise" class="text-decoration-none text-dark d-flex justify-content-between"><span>Merchandise Perusahaan</span> <i class="bi bi-chevron-right text-muted"></i></a></li>
                  <li class="py-2 border-bottom"><a href="/produk/seminar-kit" class="text-decoration-none text-dark d-flex justify-content-between"><span>Paket Seminar Kit</span> <i class="bi bi-chevron-right text-muted"></i></a></li>
                  <li class="py-2 border-bottom"><a href="/produk/hampers" class="text-decoration-none text-dark d-flex justify-content-between"><span>Hampers &amp; Parcel</span> <i class="bi bi-chevron-right text-muted"></i></a></li>
                  <li class="pt-2"><a href="/produk/souvenir-promosi" class="text-decoration-none text-dark d-flex justify-content-between"><span>Paket Souvenir Promosi</span> <i class="bi bi-chevron-right text-muted"></i></a></li>
                </ul>
              </div>

              <!-- Widget 2: Bantuan Konsultasi Kilat -->
              <div class="card border-0 rounded-4 p-4 text-center shadow-sm" style="background: color-mix(in srgb, var(--accent-color, #16a34a) 8%, transparent);">
                <div class="mx-auto mb-3 text-success fs-1">
                  <i class="bi bi-headset"></i>
                </div>
                <h3 class="h6 fw-bold text-dark mb-2">Konsultasi [Topik / Kategori]?</h3>
                <p class="small text-muted mb-3">Diskusikan kebutuhan pengadaan corporate gift B2B, spesifikasi produk, dan jadwal acara bersama tim kami.</p>
                <div class="fw-bold text-success fs-6 mb-3">+62 895-6390-68080</div>
                <a href="https://wa.me/62895639068080?text=Halo%20CorporateGifts.ID,%20saya%20ingin%20konsultasi%20..." target="_blank" rel="noopener" class="btn btn-success rounded-pill w-100 py-2 fw-semibold" style="background: var(--accent-color, #16a34a); border-color: var(--accent-color, #16a34a);">
                  <i class="bi bi-whatsapp me-1"></i> Chat WhatsApp Sekarang
                </a>
              </div>

              <!-- Widget 3: Unduh Katalog PDF -->
              <div class="card border-0 rounded-4 p-4 shadow-sm bg-white mt-4 text-center">
                <i class="bi bi-file-earmark-pdf text-danger fs-1 mb-2"></i>
                <h3 class="h6 fw-bold text-dark mb-2">E-Katalog Resmi 2026</h3>
                <p class="small text-muted mb-3">Unduh dokumen katalog resmi lengkap dengan aneka pilihan merchandise instansi, seminar kit, dan gift set siap custom logo.</p>
                <a href="../assets/docs/katalog-corporategifts-id.pdf" download="Katalog-CorporateGifts-ID-2026.pdf" target="_blank" rel="noopener" class="btn btn-outline-dark rounded-pill w-100 py-2 small fw-semibold">
                  <i class="bi bi-download me-1"></i> Unduh Katalog (PDF)
                </a>
              </div>
            </div>
          </div><!-- End Right Column -->

        </div>
      </div>
    </section>

    <!-- ══ SECTION: ARTIKEL TERKAIT ═════════════════════════════════════════ -->
    <section class="py-5 bg-light border-top">
      <div class="container" data-aos="fade-up">
        <div class="d-flex justify-content-between align-items-end mb-4 flex-wrap gap-2">
          <div>
            <span class="text-success fw-bold text-uppercase small tracking-wide">Rekomendasi Wawasan</span>
            <h2 class="h4 fw-bold text-dark m-0">Artikel Terkait Lainnya</h2>
          </div>
          <a href="/blog" class="btn btn-outline-success btn-sm rounded-pill fw-semibold">Lihat Semua Artikel <i class="bi bi-arrow-right ms-1"></i></a>
        </div>

        <div class="row g-4">
          <!-- 3 Kartu Terkait -->
        </div>
      </div>
    </section>
  </main>

  <!-- ══ FOOTER ════════════════════════════════════════════════════════════════ -->
  <footer id="footer" class="footer dark-background">
    <div class="container footer-top">
      <div class="row gy-4">
        <div class="col-lg-4 col-md-12 footer-about">
          <a href="/" class="logo d-inline-flex align-items-center bg-white py-2 px-3 rounded mb-3">
            <img src="../assets/img/logo-header.png" alt="CorporateGifts.ID - Vendor Corporate Gift &amp; Souvenir Perusahaan" style="max-height:40px;width:auto;" width="214" height="40" loading="lazy">
          </a>
          <p>Vendor corporate gift, souvenir perusahaan premium, dan merchandise kantor eksklusif untuk branding dan promosi bisnis Anda. Melayani seluruh Indonesia.</p>
          <div class="social-links d-flex mt-4">
            <a href="https://wa.me/62895639068080" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="bi bi-whatsapp"></i></a>
            <a href="https://www.instagram.com/corporategifts.id" target="_blank" rel="noopener" aria-label="Instagram"><i class="bi bi-instagram"></i></a>
            <a href="https://www.facebook.com/corporategiftsid" target="_blank" rel="noopener" aria-label="Facebook"><i class="bi bi-facebook"></i></a>
            <a href="https://www.tiktok.com/@corporategifts.id" target="_blank" rel="noopener" aria-label="TikTok"><i class="bi bi-tiktok"></i></a>
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
          <p class="mt-3"><strong>WhatsApp:</strong> <a href="https://wa.me/62895639068080" target="_blank" rel="noopener" style="color:inherit;"> +62 895-6390-68080</a></p>
          <p><strong>Website:</strong> <a href="https://corporategifts.id" style="color:inherit;">corporategifts.id</a></p>
        </div>
      </div>
    </div>

    <div class="container py-3" style="border-top:1px solid rgba(255,255,255,.1)">
      <p class="text-center mb-2" style="font-size:.85rem;opacity:.7;font-weight:600;">Partner Network</p>
      <div class="d-flex flex-wrap justify-content-center gap-3" style="font-size:.82rem;">
        <a href="https://seminarkits.id/" target="_blank" rel="noopener" style="color:rgba(255,255,255,.65);">SeminarKits.ID</a>
        <a href="https://vendormerchandise.web.id/" target="_blank" rel="noopener" style="color:rgba(255,255,255,.65);">Vendor Merchandise</a>
        <a href="https://vendorsouvenirkantor.web.id/" target="_blank" rel="noopener" style="color:rgba(255,255,255,.65);">Vendor Souvenir Kantor</a>
        <a href="https://hampersmalang.web.id/" target="_blank" rel="noopener" style="color:rgba(255,255,255,.65);">Vendor Hampers Malang</a>
        <a href="https://vendorsouvenir.web.id/" target="_blank" rel="noopener" style="color:rgba(255,255,255,.65);">Vendor Souvenir</a>
      </div>
    </div>

    <div class="container copyright text-center mt-4">
      <p>&copy; <span id="year"></span> <strong class="px-1 sitename">CorporateGifts.ID</strong> <span>- Vendor Corporate Gift, Souvenir Perusahaan &amp; Merchandise Kantor. All Rights Reserved.</span></p>
    </div>
  </footer>

  <!-- Floating WhatsApp Button -->
  <a href="https://wa.me/62895639068080?text=Halo%2C%20saya%20ingin%20konsultasi%20..." class="floating-wa d-flex align-items-center justify-content-center" target="_blank" rel="noopener" aria-label="Konsultasi via WhatsApp">
    <i class="bi bi-whatsapp"></i>
    <span class="wa-tooltip">Chat via WhatsApp</span>
  </a>

  <!-- Scroll Top -->
  <a href="#" id="scroll-top" class="scroll-top d-flex align-items-center justify-content-center" aria-label="Kembali ke atas"><i class="bi bi-arrow-up-short"></i></a>

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

</body>

</html>
```

---

## 3. Checklist Sinkronisasi 6 Langkah Wajib
1. **`blog/<slug>.html`**: Terapkan kerangka blueprint di atas 1:1.
2. **`blog.html`**: Sisipkan kartu artikel baru pada posisi tanggal update Excel (kolom kanan) secara kronologis menurun.
3. **`sitemap.xml`**: Tambahkan `<loc>` dan `<lastmod>` (YYYY-MM-DD).
4. **`_redirects`**: Tambahkan pengalihan 301 di 3 bagian:
   - Bagian Blogger 301 (atas)
   - Bagian Legacy .html 301
   - Bagian Trailing slash 301
5. **`llms.txt`**: Sisipkan 1 baris ringkasan di bawah `# Blog & Artikel`.
6. **`sitemap.html`**: Sisipkan item pada kategori kartu yang relevan, perbarui nomor urut `N.`, dan perbarui badge jumlah halaman kategori.
