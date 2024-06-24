import qrcode
img = qrcode.make('Bishworaj Poudel')
type(img)  # qrcode.image.pil.PilImage
img.save("bishworaj.png")
