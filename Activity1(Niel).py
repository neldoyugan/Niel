from PIL import Image, ImageDraw, ImageFont

# Create a blank image (white background)
width, height = 500, 500
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

center_x = width // 2
center_y = height // 2 - 30   # shift medal up to make space for ribbon

# --- Ribbon (red and blue straps, BEHIND medal) ---
draw.polygon([(center_x - 40, center_y + 50), (center_x - 10, center_y + 200), (center_x - 60, center_y + 200)], fill="red")
draw.polygon([(center_x + 40, center_y + 50), (center_x + 10, center_y + 200), (center_x + 60, center_y + 200)], fill="blue")

# --- Medal Circle (gold) ---
radius = 150
draw.ellipse(
    (center_x - radius, center_y - radius, center_x + radius, center_y + radius),
    fill="gold", outline="black", width=4
)

# --- Inner Circle (to give depth effect) ---
inner_radius = 120
draw.ellipse(
    (center_x - inner_radius, center_y - inner_radius, center_x + inner_radius, center_y + inner_radius),
    fill="yellow", outline="black", width=2
)

# --- Engraved Text on Medal ---
engraving = "Spirit of\nSportsmanship"
lines = engraving.split("\n")

try:
    font_size = 28
    font_text = ImageFont.truetype("arial.ttf", font_size)
except:
    font_text = ImageFont.load_default()
    font_size = 20

total_height = len(lines) * (font_size + 5)
start_y = center_y - total_height // 2

for i, line in enumerate(lines):
    bbox = draw.textbbox((0, 0), line, font=font_text)
    text_w = bbox[2] - bbox[0]
    x = center_x - text_w // 2
    y = start_y + i * (font_size + 5)
    draw.text((x, y), line, fill="black", font=font_text)

# --- Name at bottom of canvas ---
name_text = "Niel Angelo Rico Doyugan"

try:
    name_font = ImageFont.truetype("arial.ttf", 22)
except:
    name_font = ImageFont.load_default()

bbox = draw.textbbox((0, 0), name_text, font=name_font)
text_w = bbox[2] - bbox[0]
draw.text((center_x - text_w // 2, height - 40), name_text, fill="black", font=name_font)

# --- Show and Save ---
image.show()
image.save("CSELEC3_3B_DoyuganNielAngeloRico_Activity1.png")

