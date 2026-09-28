import base64
import os

images = [
    "vector_one_holdings_logo.jpg",
    "vector_aero_logo.jpg",
    "vector_compute_logo.jpg",
    "vector_intelligence_logo.jpg",
    "vector_academy_logo.jpg",
    "vector_brand_ecosystem.jpg"
]

base_dir = r"c:\Users\User\Desktop\Vector One\Vector_One_Outputs"

for img_name in images:
    img_path = os.path.join(base_dir, img_name)
    if os.path.exists(img_path):
        size = os.path.getsize(img_path)
        with open(img_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
        print(f"{img_name}: {size} bytes, b64_len={len(b64)}")
    else:
        print(f"NOT FOUND: {img_name}")
