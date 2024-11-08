from models.database.database import Database
from custom.helper import Helper

class F3C1Sensor(Database):

    # Constantes referentes aos tipos de sensores
    TYPE_TEMPERATURE = 1
    TYPE_HUMIDITY = 2
    TYPE_LIGHT = 3
    TYPE_RADIATION = 4
    TYPE_SALINITY = 5
    TYPE_PH = 6

    def __init__(self, object_database = None):

        super().__init__(object_database)

        self.table_name = Helper.convert_camel_to_snake_case(self.__class__.__name__)
        self.primary_key_column = 'SNS_ID'


    @staticmethod
    def get_params_to_active_data() -> dict:

        # Regras: Os registros são excluídos de forma lógica
        return {'str_column': 'SNS_STATUS', 'str_type_where': '=', 'value': Database.STATUS_ACTIVE}


    def validate_exists_data(self) -> bool:

        self.set_select([f'COUNT({self.primary_key_column}) as LENGTH'])
        self.set_where([self.get_params_to_active_data()])
        list_data = self.get_list()

        return False if len(list_data) == 0 or 'LENGTH' not in list_data[0] or list_data[0]['LENGTH'] == 0 else True


