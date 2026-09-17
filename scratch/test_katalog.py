import os
import re
import json

base_dir = r"d:\TUGAS KULIAH\Project MKI\ProjectBootstrapAktif\corporategifts-id"
fpath = os.path.join(base_dir, "katalog.html")

with open(fpath, "r", encoding="utf-8") as f:
    content = f.read()

print("=== Checking katalog.html ===")
schema_matches = re.findall(r'<script type="application/ld\+json">([\s\S]*?)</script>', content)
print(f"Found {len(schema_matches)} JSON-LD blocks")
for idx, s in enumerate(schema_matches):
    try:
        parsed = json.loads(s.strip())
        print(f"  Block {idx+1}: Valid JSON (Type: {parsed.get('@type') or [g.get('@type') for g in parsed.get('@graph', [])]})")
    except Exception as e:
        print(f"  Block {idx+1} ERROR: {e}")

img_matches = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
print(f"Found {len(img_matches)} images")
for img in img_matches:
    if img.startswith("http"):
        continue
    real_img = os.path.normpath(os.path.join(base_dir, img))
    if not os.path.exists(real_img):
        print(f"  IMAGE NOT FOUND: {img} -> {real_img}")
    else:
        print(f"  OK: {img}")

print("\nValidation complete!")
