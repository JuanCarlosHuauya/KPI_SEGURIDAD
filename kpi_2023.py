pip install pandas gspread pbpy


import pandas as pd
import gspread
from pbpy import Client

# Conexión a Google Drive y acceso al archivo de Excel
gc = gspread.service_account('path/to/your/service/account/credentials.json')
sh = gc.open('reporte_2023_diciembre').sheet1

# Lectura de datos de Excel y conexión a Power BI
data = sh.get_all_records()
client = Client('path/to/your/power/bi/credentials.json')

# Creación de un conjunto de datos en Power BI
dataset = client.create_dataset('reporte_makros_surco')

# Carga de datos a Power BI
table = dataset.table('estadistico_sst')
table.upload(data)

# Generación de indicadores en Power BI
indicators = {
    'average_revenue': {'column': 'Revenue', 'type': 'Average'},
    'max_revenue': {'column': 'Revenue', 'type': 'Max'},
    'min_revenue': {'column': 'Revenue', 'type': 'Min'},
    'sum_revenue': {'column': 'Revenue', 'type': 'Sum'},
    'count_orders': {'column': 'OrderID', 'type': 'Count'},
}

for indicator_name, indicator_details in indicators.items():
    client.create_indicator(
        dataset_id=dataset.id,
        table_name=table.name,
        indicator_name=indicator_name,
        indicator_type=indicator_details['type'],
        column_name=indicator_details['column'],
    )

# Mostrar los resultados en un dashboar en power bi mediante grafico de lineas y tacometros.
# Paleta de colores azul degradado