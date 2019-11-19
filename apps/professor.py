from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import dash_daq as daq
from app import app


def getData(start_date, end_date):
    BaseDados = pd.DataFrame()
    range_data = pd.date_range(start_date, end_date)
    print(range_data)
    tamanho = len(range_data)
    print(range_data, tamanho)
    print(np.random.normal(size=tamanho))
    BaseDados['luminosidade'] = np.random.random_sample([tamanho, ]) * 1000
    BaseDados['temperatura'] = (np.random.random_sample([tamanho, ]) * 40) - 10
    BaseDados['umidade'] = np.random.random_sample([tamanho, ])
    BaseDados['qtd_alunos'] = np.random.random_integers(size=tamanho, high=100, low=0)
    BaseDados['tamanho_turma'] = [100] * tamanho
    BaseDados.index = range_data

    return BaseDados


BaseDados = getData('2019-09-10', '2019-11-10')


# START_DATE = BaseDados.index.py.min()
# END_DATE = BaseDados.index.py.max()


def main_title():
    return html.Div(className="nav",
                    children=["Sala de Aula Inteligente - Sistemas Distribuídos - 2019.3",
                              html.Div(
                                  className="listInfo",
                                  children=[
                                      html.Div(className="info", children=['Turma: DCC064']),
                                      html.Div(className="info", children=['professor: Pagani'])]
                              )]
                    )


def img():
    return ''
    # html.Div(children=[
    #     html.Img(src='assets/img/mapa_bacia.png', className='mapa'),
    #     dcc.Markdown(children=markdown_text)
    #
    # ], className='description'),


def radio():
    return ''
    # dcc.RadioItems(
    #     id="impute",
    #     options=[
    #         {'label': 'No Imputation', 'value': 'No Imputation'},
    #         {'label': 'Median Imputation', 'value': 'Median Imputation'},
    #     ],
    #     value='No Imputation',
    #     style={'padding': '5px'}
    # ),

    # dcc.Checklist(id="selectedMeasurementStations", options=[
    #     {'label': estacao, 'value': estacao, 'disabled': False} for estacao in estacoesEscolhidas
    # ], value=estacoesEscolhidas, style={'padding': '5px'}
    #               ),


def test():
    return html.H1("nadaaaa")


def panel():
    return \
        html.Div(className='panel', children=[
            html.Div(className='panelContent', children=[
                html.H4(children="Control Panel"),
                dcc.DatePickerRange(
                    id='datepickerrange',
                    start_date=str(BaseDados.index.min()),
                    end_date=str(BaseDados.index.max()),
                    min_date_allowed=str(BaseDados.index.min()),
                    max_date_allowed=str(BaseDados.index.max()),
                    display_format='DD MM YYYY', style={'padding': '5px'}
                ),
                html.Div(className="switchs", children=
                [
                    html.Div(className="switch",
                             children=[
                                 html.Div(className="switchText", children=item),
                                 daq.ToggleSwitch(id=item, value=False),

                             ]) for item in
                    ["Lampada Frente", "Lampada Fundo", "Projetor", "Computador", "ventilador"]

                ]),
            ])])


def build():
    return \
        html.Div(className="page", children=[
            main_title(),
            html.Div(className='content', children=[
                dcc.Graph(id='quantidade_alunos_professor', className='container'),
                dcc.Graph(id='temperatura_professor', className='container'),
                dcc.Graph(id='umidade_professor', className='container'),
                dcc.Graph(id='luminosidade_professor', className='container'),
                dcc.Graph(id='alunos_professor', className='container'),
            ]),
            panel(),
            dcc.Interval(
                id='interval-component',
                interval=1 * 1000,  # in milliseconds
                n_intervals=0
            )
        ])


@app.callback(
    Output('luminosidade_professor', 'figure'),
    [Input('datepickerrange', 'start_date'),
     Input('datepickerrange', 'end_date'),
     # Input('interval-component', 'n_intervals'),

     # Input('selectedMeasurementStations', 'value'),
     # Input('selectedAlgorithms', 'value'),
     # Input('impute', 'value')
     ])
def update_figure(startDate, endDate):
    data = list()

    data.append({
        'x': BaseDados['luminosidade'].loc[startDate:endDate].index,
        'y': BaseDados['luminosidade'].loc[startDate:endDate],
        'type': 'plot',
        # 'name': estacao
    })

    return {
        'data':
            data,
        'layout': {
            'title': 'Luminosidade ao longo do tempo'
        }
    }


@app.callback(
    Output('umidade_professor', 'figure'),
    [Input('datepickerrange', 'start_date'),
     Input('datepickerrange', 'end_date'),
     # Input('interval-component', 'n_intervals'),

     # Input('selectedMeasurementStations', 'value'),
     # Input('selectedAlgorithms', 'value'),
     # Input('impute', 'value')
     ])
def update_figure(startDate, endDate):
    data = list()
    data.append({
        'x': BaseDados['umidade'].loc[startDate:endDate].index,
        'y': BaseDados['umidade'].loc[startDate:endDate],
        'type': 'plot',
        # 'name': estacao
    })

    return {
        'data':
            data,
        'layout': {
            'title': 'Umidade ao longo do tempo'
        }
    }


@app.callback(
    Output('temperatura_professor', 'figure'),
    [Input('datepickerrange', 'start_date'),
     Input('datepickerrange', 'end_date'),
     # Input('interval-component', 'n_intervals'),

     # Input('selectedMeasurementStations', 'value'),
     # Input('selectedAlgorithms', 'value'),
     # Input('impute', 'value')
     ])
def update_figure(startDate, endDate):
    data = list()
    data.append({
        'x': BaseDados['temperatura'].loc[startDate:endDate].index,
        'y': BaseDados['temperatura'].loc[startDate:endDate],
        'type': 'plot',
        # 'name': estacao
    })

    return {
        'data':
            data,
        'layout': {
            'title': 'Temperatura ao longo do tempo'
        }
    }


@app.callback(
    Output('alunos_professor', 'figure'),
    [Input('datepickerrange', 'start_date'),
     Input('datepickerrange', 'end_date'),
     # Input('interval-component', 'n_intervals'),

     # Input('selectedMeasurementStations', 'value'),
     # Input('selectedAlgorithms', 'value'),
     # Input('impute', 'value')
     ])
def update_figure(startDate, endDate):
    data = list()
    data.append({
        'x': BaseDados['qtd_alunos'].loc[startDate:endDate].index,
        'y': BaseDados['qtd_alunos'].loc[startDate:endDate],
        'type': 'bar',
        # 'name': estacao
    })

    return {
        'data':
            data,
        'layout': {
            'title': 'quantidade de alunos ao longo do tempo'
        }
    }


@app.callback(
    Output('quantidade_alunos_professor', 'figure'),
    [Input('datepickerrange', 'start_date'),
     Input('datepickerrange', 'end_date'),
     # Input('interval-component', 'n_intervals'),
     # Input('selectedMeasurementStations', 'value'),
     # Input('selectedAlgorithms', 'value'),
     # Input('impute', 'value')
     ])
def update_figure(startDate, endDate):
    # BaseDados = getData(startDate, endDate)
    print('alunosssssssss', BaseDados['qtd_alunos'][endDate])
    data = go.Pie(values=[
        BaseDados['qtd_alunos'][endDate],
        BaseDados['tamanho_turma'][endDate] - BaseDados['qtd_alunos'][endDate]
    ],
        labels=[
            'quantidade alunos presentes',
            'quantidade alunos ausentes'
        ])
    return {
        'data':
            [data],
        'layout': {
            'title': 'quantidade de alunos ao longo do tempo'
        }
    }


#
# #
# # @app.callback(
# #     Output('MAPE BarPlot', 'figure'),
# #     [Input('selectedMeasurementStations', 'value'),
# #      Input('selectedAlgorithms', 'value'),
# #      ])
# # def update_figure(selectedStations, selectAlgortithm):
# #     print(selectedStations)
# #     data = list()
# #
# #     if 'LSTM' in selectAlgortithm:
# #         data.append({
# #             'x': ['station' + estacao for estacao in selectedStations],
# #             'y': [np.mean(mapeLstm[estacao]) for estacao in selectedStations],
# #             # 'error_y': [np.std(mapeLstm[estacao]) for estacao in selectedStations],
# #             'type': 'bar', 'name': "LSTM"})
# #
# #     if 'ARIMA' in selectAlgortithm:
# #         data.append({
# #             'x': ['station' + estacao for estacao in selectedStations],
# #             'y': [mapesARIMA[estacao] for estacao in selectedStations],
# #             'type': 'bar', 'name': "ARIMA"
# #         })
# #
# #     return {
# #         'data':
# #             data,
# #         'layout': {
# #             'title': 'MAPE of each forecast algorithm'
# #         }
# #     }

layout = build()
