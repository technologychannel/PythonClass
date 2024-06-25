import qrcode

### WIFI Link
phone = "9805832889"
message = "Hello How are you"
sms = f"SMSTO:{phone}:{message}"
img = qrcode.make(sms)
type(img)  # qrcode.image.pil.PilImage
img.save("sms.png")

latt = 28.397455
long = 84.1301506


### Create QR Code Generator That Send Email to User
### Title: My First Email Using Python
### Body: Hello this is my first email using python.