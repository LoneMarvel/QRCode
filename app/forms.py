from app import app
from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class QrCreatorFrm(FlaskForm):
    qrCodeLink = StringField('QR Code Link: ')
    imgFileName = StringField('Save As QR Image Name: ')
