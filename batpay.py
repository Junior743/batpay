


################################## PARAMETERS ##################################
#################### MUDE OS PARAMETROS DO PROGRAMA AQUI #######################
################################################################################

ALUGUEL = 65000.00
IPTU = 12000.00

################################################################################
################################################################################
## desenvolvido por: Junior Sousa
## email: carloshenriquesousajunior@gmail.com





################################## IMPORTS ##################################
import sys
import argparse
from splitwise import Splitwise


################################## CONFIG ##################################
config = {
    "aluguel": ALUGUEL,
    "iptu": IPTU,
    "isAuthenticated": False,
    "locationToSaveFile": '/',
    "client_id": '2IFtKvuwi5MMhHqwCr4rFocDPc4tfoR2pSzXqait',
    "client_secret": 'AAzHaABGKBBkGRPMg9jOFqoudLvNPq14GUNLXQMN',
    "scopes": [],
    "auth_uri": 'https://secure.splitwise.com/oauth/authorize',
    "token_uri": 'https://secure.splitwise.com/oauth/token',
}


################################## SPREADSHEET SERVICES ##################################
def make_spreadsheet():
    print('Construindo planilha...')
    return True


################################## HTTP SERVICES ##################################
def authenticate_service():
    return True

def get_expenses_service():
    print('Buscando informações no splitwise...')
    spreadsheet = make_spreadsheet()
    return spreadsheet


################################## COMMAND LINE (PARSERS) ##################################
def make_parser():
    argument_parser = argparse.ArgumentParser(description='Batpay, app especializado em fazer o rateio de contas fixas e variáveis da mansão wayne.')
    parser = define_arguments_parser(argument_parser)
    args = parser.parse_args()
    execute_args_parser(args)

    return args

def define_arguments_parser(parser):
    parser.add_argument('--aluguel', type=float, help='Atribua o valor do aluguel (ex: 1234.99 (utilizar ponto))')
    parser.add_argument('--iptu', required=False, type=float, help='Atribua o valor da facada (ex: 1234.99 (utilizar ponto))')

    return parser

def execute_args_parser(args):
    if args.aluguel:
        config["aluguel"] = args.aluguel
    if args.iptu:
        config["iptu"] = args.iptu


################################## CONTROLLERS ##################################
def main():
    try:
        if sys.platform.startswith('linux'):
            main_unix()
        elif sys.platform.startswith('win32'):
            main_windows()
        elif sys.platform.startswith('darwin'):
            main_unix()

    except Exception as ex:
        print('\nOccoreu um erro durante a execução: \n\n' + str(ex))

def main_unix():
    config["locationToSaveFile"] = "~/"
    result = main_common()
    if result:
        print('\nPlanilha gerada com sucesso em: ' + config["locationToSaveFile"])
    else:
        print('\nFalhou!!!')

def main_windows():
    config["locationToSaveFile"] = "C:\\"
    result = main_common()
    if result:
        print('\nPlanilha gerada com sucesso em: ' + config["locationToSaveFile"])
    else:
        print('\nFalhou!!!')

def main_common():
    command_args = make_parser()
    print('\nFazendo autenticação no servidor do splitwise...')
    config["isAuthenticated"] = authenticate_service()
    if config["isAuthenticated"]:

        print('Serviço autenticado!')
        print('\nProcessando...')
        # do something
        return True

    else:
        print('\nO serviço não conseguiu se autenticar na API do splitwise.')
        return False


################################## INIT ##################################
if __name__ == "__main__":
    main()
