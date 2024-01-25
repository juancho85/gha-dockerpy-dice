import os
import random

def set_github_action_output(output_name, output_value):
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
    f.write(f'{output_name}={output_value}')
    f.close()

def tira_dado():
    return random.randint(1, 6)

def run():
    numero_dados = os.getenv('INPUT_NUMERO-DADOS', default="uno")
    set_github_action_output('dado1', tira_dado())
    if numero_dados == "dos":
        set_github_action_output('dado2', tira_dado())
if __name__ == '__main__':
    run()