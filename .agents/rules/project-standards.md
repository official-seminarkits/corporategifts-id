# CorporateGifts.ID - General Project Architecture & Rules

## 1. Clean URL Architecture (Cloudflare Pages)
- Seluruh tautan internal wajib menggunakan **Clean URLs non-trailing slash tanpa ekstensi `.html`**:
  - Beranda: `/`
  - Halaman Utama: `/tentang-kami`, `/layanan`, `/katalog`, `/portofolio`, `/blog`, `/galeri`, `/penulis`, `/minta-penawaran`, `/sitemap`
  - Kategori Produk: `/produk/souvenir-kantor`, `/produk/souvenir-custom`, `/produk/merchandise`, `/produk/seminar-kit`, `/produk/hampers`, `/produk/souvenir-promosi`
  - Detail Layanan: `/layanan/cetak-dan-kustomisasi-logo`, `/layanan/custom-packaging-dan-hampers`, `/layanan/desain-mockup-dan-sampling`, `/layanan/distribusi-logistik-cabang`, `/layanan/layanan-produksi-kilat`, `/layanan/pengadaan-resmi-faktur-pajak`
  - Detail Blog: `/blog/<slug>`

## 2. Footer Standar & Partner Network
- **Kolom Halaman (Wajib 8 Link)**:
  `Beranda`, `Tentang Kami`, `Layanan`, `Katalog`, `Portofolio`, `Blog`, `Galeri`, `Sitemap` (`<li><a href="/sitemap">Sitemap</a></li>`).
- **Partner Network (Tepat 5 Domain Resmi)**:
  1. `https://seminarkits.id/` (SeminarKits.ID)
  2. `https://vendormerchandise.web.id/` (Vendor Merchandise)
  3. `https://vendorsouvenirkantor.web.id/` (Vendor Souvenir Kantor)
  4. `https://hampersmalang.web.id/` (Vendor Hampers Malang)
  5. `https://vendorsouvenir.web.id/` (Vendor Souvenir)
- **Footer Styling**: Wajib solid dark background (`#0c121e !important`) tanpa transparansi.

## 3. Floating WhatsApp & Kontak
- Class tombol WhatsApp mengambang: `.floating-wa` dengan tooltip child `.wa-tooltip`.
- Nomor resmi: `+62 895-6390-68080` (`https://wa.me/62895639068080`).

## 4. Halaman Error 404
- File `404.html` wajib memuat tag `<meta name="robots" content="noindex, nofollow">` untuk mencegah pengindeksan error di search engine.

## 5. Page Banner Standard
- Menggunakan wrapper `.page-title` dengan heading terpusat dalam kolom `col-lg-8`.
- Dilengkapi breadcrumbs bar dengan padding compact dan tipografi proporsional.
