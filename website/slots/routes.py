from flask import *
from website.api_calls import *

slots= Blueprint('slots', __name__)

@slots.route('/')
def check_availibility():
    return render_template('slots_main.html')


@slots.route('/districts/<district_id>')
def check_availibility_districts(district_id):
    api=APISetu()
    slots=api.check_availibility_district(str(district_id),'27-05-2021')
    print(slots)
    return render_template('slots_district.html',slots=slots["centers"])

@slots.route('/pincode/<pincode>')
def check_availibility_pin():
    api=APISetu()
    slots=api.check_availibility_pincode(str(pincode),'27-05-2021')
    print(slots)
    return render_template('slots_pincode.html',slots)
    