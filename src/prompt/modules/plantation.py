import datetime
import os
import sys

# > Importante: A definição abaixo referente ao diretório raiz deve ser efetuada antes das importações de arquivos do sistema.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import prompt.main as Main
import prompt.modules.crop as ModuleCrop
from custom.helper import Helper
from models.f3c1crop import F3C1Crop
from models.f3c1plantation import F3C1Plantation

"""
Método responsável pela exibição do cabeçalho do módulo
"""
def show_head_module():

    print('-= Plantações =-')
    print('')


"""
Método responsável por verificar se existem plantações cadastradas
"""
def validate_exists_data():

    object_f3c1_plantation = F3C1Plantation()
    bool_exists_data = object_f3c1_plantation.validate_exists_data()

    if bool_exists_data == False:
        raise Exception('Não existem plantações cadastradas.')


"""
Método responsável por recarregar o módulo "Plantações"
"""
def require_reload():

    input(f'\nPressione <enter> para voltar ao menu do módulo "Plantações"...')
    action_main()


"""
Método responsável por retornar as opções de menu do módulo "Plantações"

Return: list
"""
def get_menu_options() -> list:

    return [
        {
            'code': 1,
            'title': 'Visualizar cadastros',
            'action': action_list
        },{
            'code': 2,
            'title': 'Cadastrar',
            'action': action_insert
        },{
            'code': 3,
            'title': 'Editar',
            'action': action_update
        },{
            'code': 4,
            'title': 'Excluir',
            'action': action_delete
        },{
            'code': 5,
            'title': 'Voltar ao menu principal',
            'action': Main.init_system
        }
    ]


"""
Método responsável por retornar os códigos das opções de menu do módulo "Plantações"

Return: list
"""
def get_menu_options_codes() -> list:

    list_return = []

    list_menu_options = get_menu_options()

    for dict_menu_option in list_menu_options:
        list_return.append(dict_menu_option['code'])

    return list_return


"""
Método responsável pela validação do parâmetro "Opção do menu" do módulo "Plantações"

Return: str
"""
def validate_menu_option() -> str:

    str_return = input(f'Digite uma opção: ')

    while True:

        try:

            if str_return.strip() == '':
                raise Exception('Deve ser definida uma opção válida.')

            if Helper.is_int(str_return) == False: 
                raise Exception('A opção informada deve ser numérica.')

            if int(str_return) not in get_menu_options_codes(): 
                raise Exception('A opção informada deve representar um dos menus disponíveis.')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            str_return = input()

    return str_return


"""
Método responsável por solicitar a opção do sistema que deverá ser executada
"""
def require_menu_option():

    str_option = validate_menu_option()

    list_menu_options = get_menu_options()

    for dict_menu_option in list_menu_options:
        if dict_menu_option['code'] == int(str_option):
            dict_menu_option['action']()


"""
Método responsável pela formatação de visualização do ID do módulo "Plantações"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )

Return: str
"""
def format_data_view_id(dict_data: dict = {}) -> str:

    str_return = 'ID: '
    str_return += f'{dict_data['PLN_ID']}' if 'PLN_ID' in dict_data and type(dict_data['PLN_ID']) != None and Helper.is_int(dict_data['PLN_ID']) == True else 'N/I'

    return str_return


"""
Método responsável pela validação do parâmetro "ID"

Return: int
"""
def validate_id() -> int:

    int_return = input(f'Informe o ID da plantação: ')

    while True:

        try:

            if int_return.strip() == '':
                raise Exception('Deve ser informado um ID válido.')

            if Helper.is_int(int_return) == False: 
                raise Exception('O conteúdo informado deve ser numérico.')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            int_return = input()

    return int(int_return)


"""
Método responsável pela formatação de visualização do nome do módulo "Plantações"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )

Return: str
"""
def format_data_view_name(dict_data: dict = {}) -> str:

    str_return = 'Nome da plantação: '
    str_return += f'{dict_data['PLN_NAME'].strip()}' if 'PLN_NAME' in dict_data and type(dict_data['PLN_NAME']) != None and type(dict_data['PLN_NAME']) == str else 'N/I'

    return str_return


"""
Método responsável pela validação do parâmetro "Nome"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )

Return: str
"""
def validate_name(dict_data: dict = {}) -> str:

    bool_is_update = ('PLN_ID' in dict_data and type(dict_data['PLN_ID']) == int)

    str_label = f'Importante: Caso deseje manter o nome atual ( abaixo ), basta ignorar o preenchimento.\n{format_data_view_name(dict_data)}\n' if bool_is_update == True else ''
    str_label += f'Informe o nome da plantação: '
    str_return = input(f'{str_label}')

    object_f3c1_plantation = F3C1Plantation()

    while True:

        try:

            if bool_is_update == False and str_return.strip() == '':
                raise Exception('Deve ser informado um nome válido.')

            if bool_is_update == False and type(str_return) != str: 
                raise Exception('O conteúdo informado deve ser texto.')

            if str_return.strip() != '':

                list_params_validate = [

                    {'str_column': 'LOWER(PLN_NAME)', 'str_type_where': '=', 'value': str_return.lower().strip()},
                    F3C1Plantation.get_params_to_active_data()

                ]

                if bool_is_update == True:

                    list_params_validate.append({'str_column': 'PLN_ID', 'str_type_where': '!=', 'value': dict_data['PLN_ID']})

                dict_plantation = object_f3c1_plantation.set_where(list_params_validate).get_one()

                if type(dict_plantation) == dict:
                    raise Exception(f'Já existe um registro cadastrado com o nome "{str_return.strip()}".')

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            str_return = input()

    return str(str_return.strip())


"""
Método responsável pela validação do parâmetro "Cultura"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )

Return: str
"""
def validate_crop_id(dict_data: dict = {}) -> int:

    bool_is_update = ('PLN_ID' in dict_data and type(dict_data['PLN_ID']) == int)

    str_label = f'Importante: Caso deseje manter a cultura atual ( abaixo ), basta ignorar o preenchimento.\n{ModuleCrop.format_data_view_name(dict_data)}\n' if bool_is_update == True else ''
    str_label += f'Informe a cultura: '
    int_return = input(f'{str_label}')

    while True:

        try:

            if bool_is_update == False and int_return.strip() == '':
                raise Exception('Deve ser informado uma cultura válida.')

            if int_return.strip() != '' and Helper.is_int(int_return) == False: 
                raise Exception('O conteúdo informado deve ser numérico.')

            if Helper.is_int(int_return) == True:

                ModuleCrop.get_data_by_id(int_return)

            break

        except Exception as error:

            print(f'{error} Tente novamente: ', end = '')
            int_return = input()

    return str(int_return.strip())


"""
Método responsável pela formatação de visualização da data de cadastro do módulo "Plantações"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )

Return: str
"""
def format_data_view_insert_date(dict_data: dict = {}) -> str:

    str_return = 'Data de cadastro: '
    str_return += f'{Helper.convert_date_to_pt_br(dict_data['PLN_INSERT_DATE'])}' if 'PLN_INSERT_DATE' in dict_data and type(dict_data['PLN_INSERT_DATE']) != None and type(dict_data['PLN_INSERT_DATE']) == datetime.datetime else 'N/I'

    return str_return


"""
Método responsável pela formatação de visualização da data de atualização do módulo "Plantações"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )

Return: str
"""
def format_data_view_update_date(dict_data: dict = {}) -> str:

    str_return = 'Data de atualização: '
    str_return += f'{Helper.convert_date_to_pt_br(dict_data['PLN_UPDATE_DATE'])}' if 'PLN_UPDATE_DATE' in dict_data and type(dict_data['PLN_UPDATE_DATE']) != None and type(dict_data['PLN_UPDATE_DATE']) == datetime.datetime else 'N/I'

    return str_return


"""
Método responsável pela formatação de visualização de dados do módulo "Plantações"

Arguments:
- dict_data: Dict contendo os dados conforme retorno do banco de dados ( dictionary )
- bool_show_id: Status informando se o parâmetro "ID" deverá ser exibido ( bool )
- bool_show_insert_date: Status informando se o parâmetro "Data de cadastro" deverá ser exibido ( bool )
- bool_show_update_date Status informando se o parâmetro "Data de atualização" deverá ser exibido ( bool )

Return: str
"""
def format_data_view(dict_data: dict = {}, bool_show_id: bool = True, bool_show_insert_date: bool = True, bool_show_update_date: bool = True) -> str:

    str_return = None

    if len(dict_data) > 0:

        str_return = ''
        str_return += f'- {format_data_view_id(dict_data)} \n' if bool_show_id == True else ''
        str_return += f'- {format_data_view_name(dict_data)} \n'
        str_return += f'- {ModuleCrop.format_data_view_name(dict_data)} \n'
        str_return += f'- {format_data_view_insert_date(dict_data)} \n' if bool_show_insert_date == True else ''
        str_return += f'- {format_data_view_update_date(dict_data)} \n' if bool_show_update_date == True else ''

    return str_return


"""
Método responsável pela exibição de cadastros do módulo "Plantações"
"""
def action_list():

    Main.init_step()

    validate_exists_data()

    show_head_module()

    object_f3c1_plantation = F3C1Plantation()

    object_f3c1_plantation.set_select(['PLN.*', 'CRP.CRP_NAME'])
    object_f3c1_plantation.set_table('F3_C1_PLANTATION PLN')
    object_f3c1_plantation.set_join([{'str_type_join': 'INNER JOIN', 'str_table': 'F3_C1_CROP CRP', 'str_where': 'CRP.CRP_ID = PLN.PLN_CRP_ID'}])
    object_f3c1_plantation.set_where([F3C1Plantation.get_params_to_active_data()])
    object_f3c1_plantation.set_order([{'str_column': 'PLN.PLN_ID', 'str_type_order': 'ASC'}])
    list_data = object_f3c1_plantation.get_data().get_list()

    for dict_data in list_data:

        print(format_data_view(dict_data))
    
    require_reload()


"""
Método responsável por executar a ação de retorno de dados de uma determinada plantação
"""
def get_data_by_id(int_pln_id: int = 0) -> dict:

    object_f3c1_plantation = F3C1Plantation()

    object_f3c1_plantation.set_select(['PLN.*', 'CRP.CRP_NAME'])
    object_f3c1_plantation.set_table('F3_C1_PLANTATION PLN')
    object_f3c1_plantation.set_join([{'str_type_join': 'INNER JOIN', 'str_table': 'F3_C1_CROP CRP', 'str_where': 'CRP.CRP_ID = PLN.PLN_CRP_ID'}])
    object_f3c1_plantation.set_where([

        {'str_column': 'PLN.PLN_ID', 'str_type_where': '=', 'value': int_pln_id},
        F3C1Plantation.get_params_to_active_data()

    ])

    dict_data = object_f3c1_plantation.get_data().get_one()

    if type(dict_data) == type(None):
        raise Exception(f'Nenhum registro foi localizado com o ID {int_pln_id}.')

    return object_f3c1_plantation


"""
Método responsável por executar a ação de retorno de dados de uma determinada cultura
"""
def get_data_crop_by_id(crp_id: int = 0) -> dict:

    object_f3c1_crop = ModuleCrop.get_data_by_id(crp_id)
    dict_data = object_f3c1_crop.get_one()

    return dict_data




# ... Demais parâmetros...


"""
Método responsável pela exibição da funcionalidade de cadastro do módulo "Plantações"
"""
def action_insert():

    Main.init_step()

    show_head_module()

    print('Os parâmetros abaixo fazem parte do cadastro principal da plantação.')
    print('')

    str_pln_name = validate_name()

    print('')

    int_pln_crp_id = validate_crop_id()

    Main.loading('Salvando dados, por favor aguarde...')

    # -------
    # Etapa 2
    # -------

    Main.init_step()

    show_head_module()

    dict_data = {}

    dict_data['PLN_NAME'] = str_pln_name
    dict_data['PLN_CRP_ID'] = int_pln_crp_id

    object_f3c1_plantation = F3C1Plantation()
    object_f3c1_plantation.insert(dict_data)

    # > Regras: Processo de complemento do objeto de dados, adicionando os parâmetros referente à cultura selecionada
    dict_data_crop = get_data_crop_by_id(int_pln_crp_id)
    dict_data['CRP_NAME'] = dict_data_crop['CRP_NAME']

    print(format_data_view(dict_data = dict_data, bool_show_id = False, bool_show_insert_date = False, bool_show_update_date = False))

    print('Registro cadastrado com sucesso.')

    require_reload()


"""
Método responsável pela exibição da funcionalidade de atualização do módulo "Plantações"
"""
def action_update():

    Main.init_step()

    show_head_module()

    validate_exists_data()

    int_pln_id = validate_id()

    # -------
    # Etapa 2
    # -------

    Main.loading('Verificando dados, por favor aguarde...')

    Main.init_step()

    show_head_module()

    object_f3c1_plantation = get_data_by_id(int_pln_id)
    dict_data = object_f3c1_plantation.get_one()

    print('Os dados abaixo representam o cadastro atual do registro informado.')
    print('')

    print(format_data_view(dict_data))

    input(f'Pressione <enter> para continuar...')

    # -------
    # Etapa 3
    # -------

    Main.init_step()

    show_head_module()

    print('Os parâmetros abaixo fazem parte do cadastro principal da plantação.')
    print('')

    str_pln_name = validate_name(dict_data)

    print('')

    int_pln_crp_id = validate_crop_id(dict_data)

    Main.loading('Salvando dados, por favor aguarde...')

    # -------
    # Etapa 4
    # -------

    Main.init_step()

    show_head_module()

    if str_pln_name.strip() != '':
        dict_data['PLN_NAME'] = str_pln_name

    if int_pln_crp_id.strip() != '':
        dict_data['PLN_CRP_ID'] = int_pln_crp_id

    object_f3c1_plantation.update(dict_data)

    # > Regras: Processo de complemento do objeto de dados, adicionando os parâmetros referente à cultura selecionada
    dict_data_crop = get_data_crop_by_id(int_pln_crp_id)
    dict_data['CRP_NAME'] = dict_data_crop['CRP_NAME']

    print(format_data_view(dict_data = dict_data, bool_show_update_date = False))

    print('Registro atualizado com sucesso.')
    
    require_reload()


"""
Método responsável pela exibição da funcionalidade de exclusão do módulo "Plantações"
"""
def action_delete():

    Main.init_step()

    show_head_module()

    validate_exists_data()

    int_pln_id = validate_id()

    # -------
    # Etapa 2
    # -------

    Main.loading('Verificando dados, por favor aguarde...')

    Main.init_step()

    show_head_module()

    object_f3c1_plantation = get_data_by_id(int_pln_id)
    dict_data = object_f3c1_plantation.get_one()

    dict_data['PLN_STATUS'] = 0

    object_f3c1_plantation.update(dict_data)

    print('Registro excluído com sucesso.')

    require_reload()


"""
Método responsável pela exibição padrão do módulo "Plantações"
"""
def action_main():

    try:

        Main.init_step()

        Main.test_connection_by_database()

        show_head_module()

        list_menu_options = get_menu_options()

        for dict_menu_option in list_menu_options:
            print(f'{dict_menu_option['code']}. {dict_menu_option['title']}')

        print('')

        require_menu_option()

    except Exception as error:

        print(f'> Ocorreu o seguinte erro: {error}')
        require_reload()