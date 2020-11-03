from flask import Flask

application = Flask(__name__)

@application.route('/')
def helloworld():
    return "Hey Naveen"

#@application is called decorator
@application.route('/search/seatlayout/<operatorID>/<DateOFtravel>')
def redbusToMorningStar(operatorID,DateOFtravel):

    print(operatorID,DateOFtravel)
    return "Ticket got booked"


if __name__=='__main__':
    application.run()