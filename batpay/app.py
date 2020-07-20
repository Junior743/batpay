import traceback
import argparse

from batpay.views import (
    ViewAdministrator
)


class BatPayApplication(object):

    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

    @staticmethod
    def defaults():
        print("BAT PAY - Application for management of apportionments.")

    @classmethod
    def extract_expenses_reports_in_pdf(cls, args):
        pass

    @classmethod
    def extract_expenses_reports_in_csv(cls, args):
        pass

    @classmethod
    def initialize(cls, *args, **kwargs):
        try:

            # criando tradutor de argumentos
            _arguments_interpretor = argparse.ArgumentParser(description=cls.defaults())
            _arguments_interpretor.set_defaults(cls.defaults())

            # declarando conversor de comandos
            _commands = _arguments_interpretor.add_subparsers()

            _reports_commands = _commands.add_parser('resumir', help = 'Resumir Calculo de indicadores')
            _reports_commands.add_argument('-d', '--dominio', action='store', dest='dominio', help='Dominio utilizado utilizado para identificação da operação.', required=True)
            _reports_commands.add_argument('-s', '--semanal', action='store_true', default=False, dest='semanal', help='Resumir semanal')
            _reports_commands.add_argument('-m', '--mensal', action='store_true', default=False, dest='mensal', help='Resumir mensalmente')
            _reports_commands.add_argument('-a', '--anual', action='store_true', default=False, dest='anual', help='Resumir anualmente')
            _reports_commands.add_argument('-e', '--excluir', action='store_true', default=False, dest='excluir', help='Excluir Resumos')
            _reports_commands.set_defaults(func=cls.resumir_indicadores)

            # interpretando argumentos
            _args_cmd = _arguments_interpretor.parse_args()
            if(hasattr(_args_cmd, 'func')):
                _args_cmd.func(_args_cmd)

        except Exception as ex:
            traceback.print_exc()
            raise ex


if __name__ == '__main__':
    BatPayApplication.initialize()
