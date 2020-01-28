import qrcode

qr = qrcode.QRCode(
    version = 1,    
    box_size = 5,
    border = 5
)

qrData = 'https://zattoo2.atlassian.net/wiki/spaces/IT/pages/1173684232/install+Network+Printer+On+MacOS'
qr.add_data(qrData)
qr.make(fit=True)
img = qr.make_image(fill='#777777', back_color='#cecece')
img.save('InstallNetPrinter-ver5.png')