# # modo aluno e professor
# # aulas que foi e aula que nao foi
# # por disciplina
# # visualizaçao painel
#

import dash

external_stylesheets = ['']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True