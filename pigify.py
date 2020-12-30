from PIL import Image, ImageDraw, ImageFilter
import requests

class pigify():
    def pigifyUser(pfp, ):
        filename = "pigusers/pig.png"
        author = message.author
        pfp = author.avatar_url
        print(pfp)
        img_data = requests.get(pfp).content
            with open('userimg.jpg', 'wb') as handler:
            handler.write(img_data)
        avatarimage = Image.open('userimg.jpg')
        pigimage = Image.open('pictures/pigs/1.jpg')
        avatarimage = avatarimage.resize((700,700))
        position = (int((pigimage.width/2 - avatarimage.width/2)), int(pigimage.height/2 - avatarimage.height/2))
        pigimage2 = pigimage.copy()
        pigimage2.paste(avatarimage, position)
        x,y = pigimage2.size
        eX, eY = 550,550
        im = Image.new
        mask = Image.new("L", pigimage2.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((x/2 - eX/2,y/2 - eY/2,x/2 + eX/2,  y/2 + eY/2), fill=255)
        mask_blur = mask.filter(ImageFilter.GaussianBlur(10))
        im = Image.composite(pigimage2, pigimage, mask_blur)
        im.save(filename)
        return filename