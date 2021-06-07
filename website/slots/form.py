from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,SubmitField
from wtforms.validators import DataRequired

class PinForm(FlaskForm):
    pincode=StringField('PINCODE',validators=[DataRequired()])
    submit=SubmitField('SEARCH')

class DistrictForm(FlaskForm):
    states=SelectField('CHOOSE STATE',choices=[("1"	,"Andaman and Nicobar Islands"),
                                                ("2"," Andhra Pradesh"),
                                                ("3","Arunachal Pradesh"),
                                                ("4",	"Assam"),
                                                ("5","Bihar"),
                                                ("6"	,"Chandigarh"),
                                                ("7","Chhattisgarh"),
                                                ("8",	"Dadra and Nagar Haveli"),
                                                ("9",	"Delhi"),
                                                ("10","Goa"),
                                                ("11","Gujarat"),
                                                ("12",	"Haryana"),
                                                ("13",	"Himachal Pradesh"),
                                                ("14","Jammu and Kashmir"),
                                                ("15","Jharkhand")])
                                               
    districts=SelectField('CHOOSE DISTRICT',choices=[])
    submit=SubmitField('SEARCH')
