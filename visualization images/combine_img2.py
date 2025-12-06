from PIL import Image

def concat_images_vertically(image_paths, output_path="output.jpg"):
    # 讀取所有圖片
    images = [Image.open(p) for p in image_paths]

    # 計算拼接後的寬度與高度
    max_width = max(img.width for img in images)
    total_height = sum(img.height for img in images)

    # 建立新圖片（背景白色，可改成其他顏色）
    new_img = Image.new("RGB", (max_width, total_height), (255, 255, 255))

    # 逐張貼上
    y_offset = 0
    for img in images:
        new_img.paste(img, (0, y_offset))
        y_offset += img.height

    # 儲存結果
    new_img.save(output_path)
    print(f"拼接完成，已輸出到 {output_path}")

# 範例使用
image_files = ["total_emission.png", 
"world_contribution.png", 
"EmmisionSources_industry.png",
"EmmisionSources_waste.png",
"EmmisionSources_agriculture.png", 
"EmmisionSources_energe_table.png"]
concat_images_vertically(image_files, "merged.jpg")