from datetime import datetime
import pprint
from custom.helper import Helper
from custom.openweather import OpenWeather
from models.f3_c1_irrigation import F3C1Irrigation

class Irrigation:

    def __init__(self):

        pass


    def exception(self, str_message: str = '') -> str:

        if str_message.strip() != '':
            raise Exception(f'[Irrigation] {str_message}')


    """
    Método responsável por verificar se uma determinada plantação deverá ser a irrigação iniciada automaticamente a partir de validações dos parâmetros preenchidos

    Arguments:
    - dict_filters_plantation: Parâmetros relacionados à plantação ( dict )
    - dict_measurement: Parâmetros relacionados à medição da plantação ( dict )
    - dict_filters_rain: Parâmetros relacionados à localização da plantação para verificação de chuvas ( dict )
   
    """
    def validate_begin_execution_by_plantation(self, dict_params: dict = {}) -> dict:

        dict_return = {'status': True, 'dict_data': {'dict_analysis_filters_plantation': {'status': False}, 'dict_analysis_filters_rain': {'status': False}}}

        try:

            dict_filters_plantation = dict_params.get('dict_filters_plantation', {})
            dict_measurement = dict_params.get('dict_measurement', {})
            dict_filters_rain = dict_params.get('dict_filters_rain', {})

            """
            Validação utilizando os filtros da plantação

            - Regras: A partir de parâmetros específicos, será possível verificar se uma irrigação automática poderá ou não ser iniciada.
            """

            # Parâmetros relacionados às configurações da plantação
            float_temp_min = dict_filters_plantation.get('float_temp_min', None)
            float_temp_max = dict_filters_plantation.get('float_temp_max', None)
            float_humidity_min = dict_filters_plantation.get('float_humidity_min', None)
            float_humidity_max = dict_filters_plantation.get('float_humidity_max', None)
            float_light_min = dict_filters_plantation.get('float_light_min', None)
            float_light_max = dict_filters_plantation.get('float_light_max', None)
            float_radiation_min = dict_filters_plantation.get('float_radiation_min', None)
            float_radiation_max = dict_filters_plantation.get('float_radiation_max', None)
            float_salinity_min = dict_filters_plantation.get('float_salinity_min', None)
            float_salinity_max = dict_filters_plantation.get('float_salinity_max', None)
            float_ph_min = dict_filters_plantation.get('float_ph_min', None)
            float_ph_max = dict_filters_plantation.get('float_ph_max', None)

            # Parâmetros relacionados à medição que deverá ser utilizada na filtragem
            int_sensor_type = dict_measurement.get('int_sensor_type', None)
            float_value = dict_measurement.get('float_value', None)
            
            # <PENDENTE>
            
            """
            Validação utilizando os filtros destinados à validação de chuva no local da plantação

            - Regras: A partir de parâmetros de geolocalização, será possível verificar se a região da plantação possui chuvas mapeadas e, caso positivo, se o limite atende às regras para iniciaçao de irrigação automática.
            """

             # Parâmetros relacionados aos filtros para validação de chuva
            float_latitude = dict_filters_rain.get('float_latitude', None)
            float_longitude = dict_filters_rain.get('float_longitude', None)

            if type(float_latitude) != type(None) and type(float_longitude) != type(None):

                # Parâmetro referente à quantidade de horas que deverá ser considerada para análise
                # > Padrão: 1h
                int_next_hours_validate_rain = dict_filters_rain.get('int_next_hours_validate_rain', 4)

                # Parâmetro referente à quantidade média máxima de chuva aceita para que a irrigação possa ser iniciada automaticamente
                # > Padrão: 0 mm
                float_max_average_rain_volume = dict_filters_rain.get('float_max_average_rain_volume', 0.00)

                # Variável que irá armazenar a quantidade de chuva prevista para as horas definidas para validação
                float_rain_volume = 0.00

                object_open_weather = OpenWeather()

                dict_data_open_weather = object_open_weather.get_weather_forecast_data_by_location(float_latitude = float_latitude, float_longitude = float_longitude)
                if dict_data_open_weather['status'] == False: 
                    self.exception(str(dict_data_open_weather['message']))

                try:

                    for dict_weather in dict_data_open_weather['dict_data']['list'][:int_next_hours_validate_rain]:

                        float_rain_volume += dict_weather.get('rain', {}).get('3h', 0.00)

                    # Variável que irá armazenar a média de chuva prevista para as horas definidas para validação
                    float_average_rain_volume = (float_rain_volume / int_next_hours_validate_rain)

                    if float_average_rain_volume > float_max_average_rain_volume:
                        self.exception(f'A quantidade média de chuva prevista para para a(s) próxima(s) {int_next_hours_validate_rain} hora(s) é de {float_average_rain_volume:.2f} mm e está acima do máximo permitido ( {float_max_average_rain_volume:.2f} mm ).')

                    dict_return['dict_data']['dict_analysis_filters_rain']['status'] = True
                    dict_return['dict_data']['dict_analysis_filters_rain']['str_analisys'] = f'A quantidade média de chuva prevista para para a(s) próxima(s) {int_next_hours_validate_rain} hora(s) é de {float_average_rain_volume:.2f} mm e está abaixo do máximo permitido ( {float_max_average_rain_volume:.2f} mm ).'

                except Exception as error:

                    dict_return['dict_data']['dict_analysis_filters_rain'] = {'status': False, 'message': error}

        except Exception as error:

            dict_return = {'status': False, 'message': error}

        return dict_return


