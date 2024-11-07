from custom.helper import Helper
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
    - 
   
    """
    def validate_begin_execution_by_plantation(self, dict_params: dict = {}) -> dict:

        dict_return = {'status': True, 'dict_data': {}}

        try:

            # <PENDENTE>
            # - Desenvolver regras para execução automática
            pass

        except Exception as error:

            dict_return = {'status': False, 'message': error}

        return dict_return


