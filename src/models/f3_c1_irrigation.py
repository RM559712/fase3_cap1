from models.database.database import Database
from custom.helper import Helper

class F3C1Irrigation(Database):

    # Constantes referentes à origem da execução
    ORIGIN_MANUAL = 1
    ORIGIN_AUTOMATED = 2

    # Constantes referentes ao status de execução
    STATUS_EXECUTION_RUNNING = 1
    STATUS_EXECUTION_FINISHED = 2

    def __init__(self, object_database = None):

        super().__init__(object_database)

        self.table_name = Helper.convert_camel_to_snake_case(self.__class__.__name__)
        self.primary_key_column = 'IRG_ID'


    @staticmethod
    def get_params_to_active_data() -> dict:

        # Regras: Os registros são excluídos de forma lógica
        return {'str_column': 'IRG_STATUS', 'str_type_where': '=', 'value': 1}


    def validate_exists_data(self) -> bool:

        self.set_select([f'COUNT({self.primary_key_column}) as LENGTH'])
        self.set_where([self.get_params_to_active_data()])
        list_data = self.get_list()

        return False if len(list_data) == 0 or 'LENGTH' not in list_data[0] or list_data[0]['LENGTH'] == 0 else True


    def get_label_origin(self, irg_origin: int = 0) -> str:

        dict_labels = {}
        dict_labels[ self.ORIGIN_MANUAL ] = {'str_label': 'Inicialização manual'}
        dict_labels[ self.ORIGIN_AUTOMATED ] = {'str_label': 'Inicialização automatizada'}

        str_return = dict_labels[ irg_origin ]['str_label'] if irg_origin in dict_labels else 'N/I'
        return str_return


    def get_label_status_execution(self, irg_status_execution: int = 0) -> str:

        dict_labels = {}
        dict_labels[ self.STATUS_EXECUTION_RUNNING ] = {'str_label': 'Em execução'}
        dict_labels[ self.STATUS_EXECUTION_FINISHED ] = {'str_label': 'Finalizado'}

        str_return = dict_labels[ irg_status_execution ]['str_label'] if irg_status_execution in dict_labels else 'N/I'
        return str_return


