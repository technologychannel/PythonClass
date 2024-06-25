import qrcode
img = qrcode.make('https://brp.com.np')
type(img)  # qrcode.image.pil.PilImage
img.save("websiteqr.png")
