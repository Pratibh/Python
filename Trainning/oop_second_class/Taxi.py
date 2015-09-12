__author__ = 'pratibh'


class Taxi:
    driver = " "
    onDuty = " "
    location = " "
    passengerLocation = " "
    no_of_passengers = "1"

    def __init__(self, driver_name, driver_on_duty, driver_location, ):
        self.driver = driver_name
        self.onDuty = driver_on_duty
        self.location = driver_location

    def getPickUp(self, passenger_location, passenger_no, driver_on_duty):

            self.passengerLocation = passenger_location
            self.no_of_passengers = passenger_no

    def setPickUp(self):
        return self.passengerLocation


Driver = Taxi("Arun Amatya", "Yes", "Sanepa")
print "Driver Details and  Location "
print "*****************************"
print Driver.driver
print Driver.onDuty
print Driver.location
print "*****************************"

print "Enter Passenger location"
passengerLocation = raw_input()
print "Enter the no of passengers"
no_of_passenger = raw_input()
isOnDuty = Driver.onDuty
Driver.getPickUp(passengerLocation,no_of_passenger, isOnDuty)


