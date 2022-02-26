"""
Final Implementation of WeatherData.  Complete all the TODOs
"""


class Subject:
    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered or removed.
    def registerObserver(observer):
        pass
    def removeObserver(observer):
        pass

    # This method is called to notify all observers
    # when the Subject's state (measuremetns) has changed.
    def notifyObservers():
        pass

# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and
# passing the measurements to the observers.
class Observer:
    def update(self, temp, humidity, pressure):
        pass

# WeatherData now implements the subject interface.
class WeatherData(Subject):

    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0


    def registerObserver(self, observer):
        # When an observer registers, we just
        # add it to the end of the list.
        self.observers.append(observer)

    def removeObserver(self, observer):
        # When an observer wants to un-register,
        # we just take it off the list.
        self.observers.remove(observer)

    def notifyObservers(self):
        # We notify the observers when we get updated measurements
        # from the Weather Station.
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurementsChanged()

    # other WeatherData methods here.

class CurrentConditionsDisplay(Observer):

    def __init__(self, weatherData):
        self.temerature = 0
        self.humidity = 0
        self.pressure = 0

        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer
                                            # so it gets data updates.
    def update(self, temperature, humidity, pressure):
        self.temerature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print("Current conditions:", self.temerature,
                "F degrees and", self.humidity,"[%] humidity",
                "and pressure", self.pressure)

# TODO: implement StatisticsDisplay class and ForecastDisplay class.

class StatisticsDisplay(Observer):
    def __init__(self, weather_data):
        self.temperature = []
        self.humidity = []
        self.pressure = []

        self.weatherData = weather_data
        self.weatherData.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.temperature.append(temperature)

        self.humidity.append(humidity)

        self.pressure.append(pressure)
        
        self.display()

    def display(self):
        self.minTemp = min(self.temperature)
        self.maxTemp = max(self.temperature)    
        self.averageTemp = sum(self.temperature) / len(self.temperature)

        self.minHumidity = min(self.humidity)
        self.maxHumidity = max(self.humidity)
        self.averageHumidity = sum(self.humidity) / len(self.humidity)

        self.minPressure = min(self.pressure)
        self.maxPreassure = max(self.pressure)
        self.averagePressure = sum(self.pressure) / len(self.pressure)

        print("Temp:\n Temp Avg:", self.averageTemp,
                "Temp Min:", self.minTemp,
                "Temp Max:", self.maxTemp,
                "\n Humidity: \n Humidity Avg:", self.averageHumidity,
                "Humidity Min:", self.minHumidity,
                "Humidity Max:", self.maxHumidity,
                "\n Pressure: Pressure Avg:", self.averagePressure,
                "Pressure Min:", self.minPressure,
                "Pressure Max:", self.maxPreassure
        )


class ForecastDisplay(Observer):
    def __init__(self, weather_data):
        self.forecastTemp = 0
        self.forecastHumidity = 0
        self.forecastPressure = 0

        self.weatherData = weather_data
        self.weatherData.registerObserver(self)

    def update(self, temp, humidity, pressure):
        self.forecastTemp = temp + 0.11 * humidity + 0.2 * pressure
        self.forecastHumidity = humidity - 0.9 * humidity
        self.forecastPressure = pressure + 0.1 * temp - 0.21 * pressure

        self.display()

    def display(self):
        print("Forecast: \n",
                "Temp:", self.forecastTemp,
                "Humidity:", self.forecastHumidity,
                "Pressure:", self.forecastPressure
        )


class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)

        # TODO: Create two objects from StatisticsDisplay class and
        # ForecastDisplay class. Also register them to the concerete instance
        # of the Subject class so the they get the measurements' updates.
        # The StatisticsDisplay class should keep track of the min/average/max
        # measurements and display them.
        statistics_display = StatisticsDisplay(weather_data)

        # The ForecastDisplay class shows the weather forcast based on the current
        # temperature, humidity and pressure. Use the following formuals :
        # forcast_temp = temperature + 0.11 * humidity + 0.2 * pressure
        # forcast_humadity = humidity - 0.9 * humidity
        # forcast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
        forecast_display = ForecastDisplay(weather_data)


        weather_data.setMeasurements(80, 65,30.4)
        weather_data.setMeasurements(82, 70,29.2)
        weather_data.setMeasurements(78, 90,29.2)

        # un-register the observer
        weather_data.removeObserver(current_display)
        weather_data.removeObserver(statistics_display)
        weather_data.removeObserver(forecast_display)
        weather_data.setMeasurements(120, 100,1000)



if __name__ == "__main__":
    w = WeatherStation()
    w.main()