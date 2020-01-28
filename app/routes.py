from flask import Flask, redirect, render_template, url_for
import qrcode
import os
import fnmatch
from weasyprint import HTML
from app import app
from app.forms import QrCreatorFrm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    qrCodeFrm = QrCreatorFrm()
    title = 'Zattoo QR Code Creator'
    if qrCodeFrm.validate_on_submit(): 
        title = 'Display QR Code'       
        qrCodeLink = qrCodeFrm.qrCodeLink.data
        imgFileName = qrCodeFrm.imgFileName.data
        print(f'Form Validated With Link -> {qrCodeLink} And Name -> {imgFileName}')
        qrImageFile = CreateQrCode(qrCodeLink, imgFileName)
        return render_template('displayimg.html', imgFile=qrImageFile, imgFileName=imgFileName, title=title)
    return render_template('qrcodefrm.html', qrCodeFrm=qrCodeFrm, title=title)

def CreateQrCode(qrCodeLink, imgFileName):
    qr = qrcode.QRCode(
        version = 1,    
        box_size = 5,
        border = 2
        )
    qrData = qrCodeLink
    qr.add_data(qrData)
    qr.make(fit=True)
    img = qr.make_image(fill='#777777', back_color='#cecece')
    baseDir = os.path.abspath(os.path.dirname(__file__))
    baseDir += '/static/qrImages/'
    print(f'The Save Dir {baseDir}')
    img.save(os.path.join(baseDir,imgFileName+'.png'))
    return 'qrImages/'+imgFileName+'.png'

@app.route('/list')
def list():
    fileList = []    
    fileExt = '*.png'
    baseDir = os.path.abspath(os.path.dirname(__file__))
    baseDir += '/static/qrImages'
    for fileImg in os.listdir(baseDir):
        if fnmatch.fnmatch(fileImg, fileExt):
            fileList.append(fileImg)
            
    
    return render_template('list.html', fileList=fileList, title='List All QR Codes')