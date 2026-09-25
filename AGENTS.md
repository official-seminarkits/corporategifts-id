# AGENTS.md - CorporateGifts.ID Agent Instructions

## Blog Migration Standard Architecture & Immutable Rules
All migrated blog detail articles MUST strictly follow the exact HTML blueprint and classes defined in `PANDUAN_MIGRASI_BLOG.md` and `.agents/rules/blog-migration-rules.md`.
The reference baseline gold standards are `blog/cara-undi-doorprize-bukber-perusahaan.html`, `blog/souvenir-tumbler-panduan-lengkap-untuk-pemula.html`, and `blog/hamper-lifestyle-eksekutif-anniversary.html`.

#### Key Standards & Exact Component Specifications:

1. **Fonts & Preconnect**:
   - Google Fonts `Poppins` (500, 600, 700) and `Inter` (400, 500, 600, 700) with preload and print media onload fallback.

2. **Body Tag**:
   - `<body class="blog-detail-page">` (DILARANG menggunakan `blog-details-page`).

3. **Header & Navigation (Wajib Lengkap)**:
   - Logo: `<a href="/" class="logo d-flex align-items-center me-auto me-xl-0"><img src="../assets/img/logo-header.png" alt="CorporateGifts.ID - Vendor Corporate Gift &amp; Souvenir Perusahaan" style="max-height:40px;width:auto;" width="214" height="40" loading="lazy"></a>`
   - Menu Nav: `Beranda`, `Tentang Kami`, `Layanan`, `Katalog`, `Portofolio`, `<li class="dropdown"><a href="/produk"><span>Produk</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>...` (6 sub-menu produk: Souvenir Kantor, Souvenir Custom, Merchandise Perusahaan, Paket Seminar Kit, Hampers & Parcel, Paket Souvenir Promosi), `Blog` (active), dan `Galeri`.
   - Header CTA: `<a class="btn-getstarted" href="https://wa.me/62895639068080?text=Halo%2C%20saya%20ingin%20konsultasi%20..." target="_blank" rel="noopener"><i class="bi bi-whatsapp me-1"></i> Hubungi Kami</a>`.

4. **Main Tag Wrapping & Layout Hierarchy**:
   - `<main id="main" class="main">` WAJIB membungkus `.breadcrumbs-bar`, `<section class="py-5"><div class="container" data-aos="fade-up"><div class="row g-5">` (detail artikel + sidebar), dan `<section class="py-5 bg-light border-top"><div class="container" data-aos="fade-up">` (rekomendasi artikel terkait), lalu ditutup `</main>` sebelum `<footer>`.
   - Kolom kiri: `<div class="col-lg-8"><article class="article-detail-wrap">...`.
   - Seluruh konten isi artikel, subjudul, callout, tabel, gambar in-body, dan accordion FAQ dibungkus dalam `<div class="article-body">...</div><!-- End Article Body Content -->`.

5. **Breadcrumbs Bar**:
   - `<div class="breadcrumbs-bar py-3 bg-white" style="border-bottom: 1px solid #f1f5f9;"><div class="container"><nav aria-label="breadcrumb" class="m-0 p-0" style="background: transparent;"><ol class="breadcrumb m-0 p-0" style="background: transparent; font-size: 0.88rem;"><li class="breadcrumb-item"><a href="/" style="color: var(--accent-color, #15803d); text-decoration: none; font-weight: 500;">Beranda</a></li><li class="breadcrumb-item"><a href="/blog" style="color: var(--accent-color, #15803d); text-decoration: none; font-weight: 500;">Blog</a></li><li class="breadcrumb-item active" aria-current="page" style="color: #64748b; font-weight: 500;">[Topik / Judul]</li></ol></nav></div></div>`.

6. **Article Header & Meta Bar**:
   - Header Wrap:
     ```html
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
     ```

7. **Featured Image & In-Body Images**:
   - Featured: `<div class="article-featured-img"><img src="../assets/img/blog/[img-1].webp" alt="..." class="img-fluid" loading="lazy" width="1200" height="675"><p class="text-muted text-center small mt-2 fst-italic">[Caption]</p></div>`.
   - In-Body: `<div class="article-inbody-img my-4"><img src="../assets/img/blog/[img-2].webp" alt="..." class="img-fluid rounded-4 shadow-sm w-100" loading="lazy" width="800" height="450"><p class="text-muted text-center small mt-2 fst-italic">[Caption]</p></div>`.

8. **Table of Contents (TOC)**:
   - Container: `.table-of-contents`
   - Header: `<div class="d-flex justify-content-between align-items-center" id="toc-header" style="cursor: pointer; user-select: none;"><h2 class="m-0 d-flex align-items-center"><i class="bi bi-list-nested text-success me-2"></i> Daftar Isi Artikel</h2><button type="button" class="btn btn-sm btn-light border px-2 py-1 text-muted d-inline-flex align-items-center gap-1" id="toc-toggle-btn" aria-expanded="true" aria-controls="toc-list" style="border-radius: 6px;"><span id="toc-btn-text">Tutup</span><i class="bi bi-chevron-up" id="toc-btn-icon"></i></button></div>`
   - List: `<div id="toc-list" class="mt-2"><ol class="mb-0">...</ol></div>`

9. **Body Content, Callouts, & Tables**:
   - Paragraf pertama diawali: `<strong><a href="/" class="text-success text-decoration-none fw-bold">Corporate Gifts ID</a></strong> - ...`
   - **Poin Kunci / Highlight**: `<div class="article-key-points"><h3 class="h6 fw-bold text-dark mb-2"><i class="bi bi-lightbulb-fill text-success me-2"></i> Poin Kunci ...:</h3><ul class="mb-0 small text-muted ps-3" style="line-height: 1.7;"><li><strong>Label:</strong> Deskripsi.</li></ul></div>`
   - **Callout Baca Juga**: `<div class="article-baca-juga"><span class="badge bg-success text-white px-2 py-1 rounded-pill small fw-bold">Baca Juga</span><a href="/blog/[slug]" class="hover-green">[Judul Artikel] <i class="bi bi-arrow-right ms-1"></i></a></div>`
   - **Tabel Responsif**: Wajib dibungkus `<div class="tbl-wrap"><table class="tbl-corporategifts"><thead>...</thead><tbody><tr><td data-label="Kolom">...</td></tr></tbody></table></div>`. DILARANG menyisipkan inline `<style>` untuk tabel di head.
   - **HTML Semantik Murni**: Dilarang meninggalkan karakter markdown `*` (*italic*) atau `**` (**bold**). Wajib dikonversi ke tag HTML `<em>...</em>` atau `<strong>...</strong>`.
   - **Zero Em-Dashes**: Dilarang menggunakan karakter em-dash (`—` / `&mdash;`), gunakan tanda strip `-`.
   - **Internal Links**: Wajib menyematkan tautan internal natural ke produk (`/produk...`), katalog (`/katalog`), RFQ (`/minta-penawaran`), atau artikel blog relevan (`/blog/[slug]`).

10. **FAQ Accordion**:
    ```html
    <div class="article-faq-compact my-4" id="faq-section">
      <h3 class="h5 fw-bold text-dark mb-3">
        <i class="bi bi-question-circle-fill text-success me-2"></i> Pertanyaan Seputar [Topik] (FAQ)
      </h3>
      <div class="accordion accordion-flush" id="blogFaqAccordion">
        <div class="accordion-item border-bottom">
          <h4 class="accordion-header" id="faqHead1">
            <button class="accordion-button collapsed py-2 px-3 fw-semibold text-dark bg-white" type="button" data-bs-toggle="collapse" data-bs-target="#faqCollapse1" aria-expanded="false" aria-controls="faqCollapse1" style="font-size: 0.88rem;">
              1. [Pertanyaan 1]
            </button>
          </h4>
          <div id="faqCollapse1" class="accordion-collapse collapse" aria-labelledby="faqHead1" data-bs-parent="#blogFaqAccordion">
            <div class="accordion-body py-2 px-3 text-muted" style="line-height: 1.6; font-size: 0.84rem;">
              [Jawaban 1]
            </div>
          </div>
        </div>
        <!-- Item 2 s/d 5 (Item terakhir tanpa class border-bottom) -->
      </div>
    </div>
    ```

11. **Bottom RFQ CTA Banner**:
    ```html
    <div class="card border-0 mt-5 shadow-sm text-center text-md-start blog-cta-banner">
      <div class="d-flex flex-column flex-md-row align-items-center justify-content-between gap-3">
        <div>
          <h3 class="h5 fw-bold text-dark mb-1">[Judul CTA Ringkas]</h3>
          <p class="small text-muted mb-0">[Deskripsi penawaran, mockup gratis, dan katalog resmi].</p>
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
    ```

12. **Author Box**:
    ```html
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
    ```

13. **Share Bar**:
    ```html
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

14. **Sidebar Kanan (3 Widget Standar Wajib)**:
    ```html
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
          <div class="mx-auto mb-3 text-success fs-1"><i class="bi bi-headset"></i></div>
          <h3 class="h6 fw-bold text-dark mb-2">Konsultasi [Topik]?</h3>
          <p class="small text-muted mb-3">Diskusikan kebutuhan souvenir kantor, gift set VIP, dan hampers perusahaan bersama kami.</p>
          <div class="fw-bold text-success fs-6 mb-3">+62 895-6390-68080</div>
          <a href="https://wa.me/62895639068080?text=Halo%20CorporateGifts.ID,%20saya%20ingin%20konsultasi" target="_blank" rel="noopener" class="btn btn-success rounded-pill w-100 py-2 fw-semibold" style="background: var(--accent-color, #16a34a); border-color: var(--accent-color, #16a34a);">
            <i class="bi bi-whatsapp me-1"></i> Chat WhatsApp Sekarang
          </a>
        </div>
        <!-- Widget 3: Unduh E-Katalog PDF -->
        <div class="card border-0 rounded-4 p-4 shadow-sm bg-white mt-4 text-center">
          <i class="bi bi-file-earmark-pdf text-danger fs-1 mb-2"></i>
          <h3 class="h6 fw-bold text-dark mb-2">E-Katalog Resmi 2026</h3>
          <p class="small text-muted mb-3">Unduh dokumen katalog resmi lengkap dengan aneka pilihan merchandise instansi, seminar kit, dan gift set siap custom logo.</p>
          <a href="../assets/docs/katalog-corporategifts-id.pdf" download="Katalog-CorporateGifts-ID-2026.pdf" target="_blank" rel="noopener" class="btn btn-outline-dark rounded-pill w-100 py-2 small fw-semibold">
            <i class="bi bi-download me-1"></i> Unduh Katalog (PDF)
          </a>
        </div>
      </div>
    </div>
    ```

15. **Section Artikel Terkait (3 Rekomendasi)**:
    - `<section class="py-5 bg-light border-top"><div class="container" data-aos="fade-up">`
    - Section header dengan baris "Rekomendasi Wawasan" + "Artikel Terkait Lainnya" + tombol "Lihat Semua Artikel" (`/blog`).
    - 3 Kartu rekomendasi artikel terkait ber-badge kategori pojok kiri atas, excerpt, author footer lengkap (avatar 30x30, nama penulis, dan tombol "Baca ->"), dan tautan ke `/blog/[slug]`. Verifikasi ketat bahwa file gambar di `assets/img/blog` benar-benar ada di disk.

16. **Footer & Scripts (Wajib 100% Identik dengan Master Gold Standard)**:
    ```html
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
            <p class="mt-3"><strong>WhatsApp:</strong>
              <a href="https://wa.me/62895639068080" target="_blank" rel="noopener" style="color:inherit;"> +62 895-6390-68080</a>
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
    <a href="https://wa.me/62895639068080?text=Halo%20CorporateGifts.ID,%20saya%20ingin%20konsultasi%20[topik]" class="floating-wa d-flex align-items-center justify-content-center" target="_blank" rel="noopener" aria-label="Konsultasi via WhatsApp">
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
    ```

17. **Schemas (5 JSON-LD Blocks Bebas Warning Google)**:
    - `LocalBusiness & Organization`: `@id: "https://corporategifts.id/#localbusiness"`. Wajib memuat `address` lengkap (`streetAddress: "Jl. Basuki Rahmat No. 12-18, Tegalsari"`, `addressLocality: "Surabaya"`, `addressRegion: "Jawa Timur"`, `postalCode: "60261"`, `addressCountry: "ID"`) serta `geo` (`latitude: -7.2575`, `longitude: 112.7521`).
    - `Article (Utama)`: `@id` berakhiran `#article` (`https://corporategifts.id/blog/<slug>#article`), `mainEntityOfPage` bernilai `https://corporategifts.id/blog/<slug>`, dan properti `image` ImageObject / array URL gambar.
    - `Article (Ringkasan Eksekutif)`: `@id` berakhiran `#summary` (`https://corporategifts.id/blog/<slug>#summary`), `about` bernilai `https://corporategifts.id/blog/<slug>#article`, dan WAJIB memuat properti `image` (URL gambar featured artikel, `width: 1200`, `height: 675`) agar bebas Google warning *"Kolom image tidak ada"*.
    - `BreadcrumbList`: 3 tingkat (Beranda `https://corporategifts.id/` > Blog `https://corporategifts.id/blog` > Judul `https://corporategifts.id/blog/<slug>`).
    - `FAQPage`: Array Question/Answer yang sinkron 1:1 dengan accordion FAQ.

18. **Full 6-Step Sync Checklist (Wajib Setiap Migrasi 1 Artikel)**:
    - **Step 1**: `blog/<slug>.html` (artikel detail dengan Clean URLs tanpa .html dan tanpa trailing slash).
    - **Step 2**: `blog.html` (disisipkan sesuai urutan tanggal update kronologis menurun, link kartu ke `/blog/<slug>`, pagination dinamis client-side).
    - **Step 3**: `sitemap.xml` (`<loc>https://corporategifts.id/blog/<slug></loc>` dan `<lastmod>YYYY-MM-DD</lastmod>`).
    - **Step 4**: `_redirects` (WAJIB update di 3 bagian setiap kali migrasi 1 artikel):
      1. **Bagian Blogger 301 Redirects** (bagian atas file):
         ```
         # [Judul Artikel]
         /<YYYY>/<MM>/<slug>.html /blog/<slug> 301
         /<slug>/ /blog/<slug> 301
         /<slug> /blog/<slug> 301
         ```
      2. **Bagian `# Legacy .html to Clean URLs (Non-Trailing Slash) 301 Redirects`** (di bawah header `# Blog Detail Pages Legacy .html 301`):
         ```
         /blog/<slug>.html /blog/<slug> 301
         ```
      3. **Bagian `# Trailing Slash to Non-Trailing Slash 301 Redirects`** (di bawah header `# Trailing Slash to Non-Trailing Slash 301 Redirects`):
         ```
         /blog/<slug>/ /blog/<slug> 301
         ```
    - **Step 5**: `llms.txt` (ringkasan 1 baris di bawah `Blog & Artikel` dengan URL `https://corporategifts.id/blog/<slug>`).
    - **Step 6**: `sitemap.html` (WAJIB disisipkan pada kategori kartu sitemap yang relevan, update nomor urut item `N.`, link ke `/blog/<slug>`, update badge jumlah artikel di header kategori, dan update total counter halaman di banner).

19. **Author Standard**:
    - Penulis resmi 3 orang:
      1. **Arinda Zakia** (`/penulis#arinda-zakia`, avatar `../assets/img/penulis/arinda-zakia.webp`)
      2. **Sholikhatun Nikmah** (`/penulis#sholikhatun-nikmah`, avatar `../assets/img/penulis/sholikhatun-nikmah.webp`)
      3. **Vendor Souvenir Kantor** (`/penulis#vendor-souvenir-kantor`, avatar `../assets/img/penulis/vendor-souvenir-kantor.png`)
    - DILARANG menggunakan nama atau avatar lama "Amelia".

20. **Date Source of Truth**:
    - Selalu gunakan nilai dari kolom Excel **Tanggal Update** (kolom kanan) untuk tanggal artikel, meta bar, schema JSON-LD, kartu `blog.html`, dan `sitemap.xml`.

21. **Execution & Tool Constraints**:
    - DILARANG membuat file script python (`.py`) untuk migrasi atau validasi karena memperlambat alur kerja. Gunakan tool bawaan IDE secara langsung.
    - Wajib memverifikasi keberadaan file fisik gambar lokal di `assets/img/blog/` sebelum menuliskan path-nya.
