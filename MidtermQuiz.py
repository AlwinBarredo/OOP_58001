#CODE BY ALWIN
class DistanceConversion:
    def __init__(self, distance):
        self.__distance = distance

    def __meter_to_centimeter(self):
        return self.__distance * 100

    def __meter_to_kilometer(self):
        return self.__distance / 1000

    def __meter_to_inch(self):
        return self.__distance * 39.37

    def convert(self):
        print("{} meters is equal to {} centimeters".format(self.__distance, self.__meter_to_centimeter()))
        print("{} meters is equal to {} kilometers".format(self.__distance, self.__meter_to_kilometer()))
        print("{} meters is equal to {} inches".format(self.__distance, self.__meter_to_inch()))


distance = float(input("Enter distance in meters: "))
converter = DistanceConversion(distance)
converter.convert()