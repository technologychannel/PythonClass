import qrcode
img = qrcode.make('Bishworaj Poudel')


### WIFI Link
wifi_type = "WPA"
wifi_ssid = "iambrp_fpkhr"
wifi_password = "Passw0rd@1234"
wifi = f"WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;"
img = qrcode.make(wifi)
type(img)  # qrcode.image.pil.PilImage
img.save("wifi.png")