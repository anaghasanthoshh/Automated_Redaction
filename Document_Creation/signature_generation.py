from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

df=pd.read_csv('data.csv')
#names=df['first_name'] +' '+ df['last_name']
#print(names)
font_path='fonts/Bastliga One.ttf'
font_size=50
def generate_signs(name):
    os.makedirs('signature_generated',exist_ok=True)
    img = Image.new("RGBA", (300, 100), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)
    draw.text((20, 20), name, font=font, fill=(0, 0, 0))

    signature_filename = f"{name.lower()}_signature.png"
    signature_path = os.path.join('signature_generated', signature_filename)
    img.save(signature_path)
    return signature_path
updated_csv='data_with_sign.csv'
df['signature_path']=df['first_name'].apply(generate_signs)
df.to_csv(updated_csv,index=False)