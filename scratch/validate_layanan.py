import os
import re
import json

base_dir = r"d:\TUGAS KULIAH\Project MKI\ProjectBootstrapAktif\corporategifts-id"
layanan_dir = os.path.join(base_dir, "layanan")

files = [os.path.join(layanan_dir, f) for f in os.listdir(layanan_dir) if f.endswith(".html")]
files.append(os.path.join(base_dir, "layanan.html"))

all_passed = True

print(f"Testing {len(files)} files...\n")

for fpath in files:
    fname = os.path.relpath(fpath, base_dir)
    print(f"=== Checking {fname} ===")
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check JSON-LD
    schema_matches = re.findall(r'<script type="application/ld\+json">([\s\S]*?)</script>', content)
    print(f"  Found {len(schema_matches)} JSON-LD blocks")
    for idx, s in enumerate(schema_matches):
        try:
            parsed = json.loads(s.strip())
            print(f"    Block {idx+1}: Valid JSON (Type: {parsed.get('@type') or [g.get('@type') for g in parsed.get('@graph', [])]})")
        except Exception as e:
            print(f"    Block {idx+1} ERROR: {e}")
            all_passed = False
            
    # Check old text "Detail Solusi"
    if "Detail Solusi" in content or "detail solusi" in content.lower():
        print("  WARNING: Found 'Detail Solusi' in content!")
        all_passed = False
    else:
        print("  OK: No 'Detail Solusi' found.")
        
    # Check image paths
    img_matches = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    for img in img_matches:
        if img.startswith("http"):
            continue
        # normalize path
        if fname.startswith("layanan\\"):
            # relative to layanan/
            real_img = os.path.normpath(os.path.join(layanan_dir, img))
        else:
            real_img = os.path.normpath(os.path.join(base_dir, img))
            
        if not os.path.exists(real_img):
            print(f"  IMAGE NOT FOUND: {img} -> {real_img}")
            all_passed = False
            
    print()

if all_passed:
    print("ALL CHECKS PASSED SUCCESSFULLY!")
else:
    print("SOME CHECKS FAILED!")
