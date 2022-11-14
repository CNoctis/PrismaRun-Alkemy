# import the libraries
import logging
from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
import pandas as pd

# defining DAG arguments

default_args = {
 'owner': 'Alkemy_Prisma',
 'start_date': days_ago(0),
 'email': ['some@somemail.com'],
 'email_on_failure': False,
 'email_on_retry': False,
 'retries': 1,
 'retry_delay': timedelta(minutes=5),
}


dag = DAG(
 'dag_unidad_5',
 default_args=default_args,
 description='My first DAG',
 schedule_interval=timedelta(days=1),
)

@dag.task(task_id = "read_top10")
def read_top10():
    
    # Logging
    logger = logging.getLogger(__name__)
    level =logger.setLevel('INFO')
    logger.setLevel(level)

    format = logging.Formatter = '%(asctime)s - %(name)s  - %(message)s'
     
    streamhanler = logging.StreamHandler 
    streamhanler.level('INFO')
    streamhanler.set_name(format)
    logger.addFilter(streamhanler)

    filehandler = logging.FileHandler('/home/cris/airflow/log/log_unidad_5.log') 
    filehandler.level('INFO')
    filehandler.set_name(format)
    logger.addFilter(filehandler)

    # Read CSV from web
    url = "http://winterolympicsmedals.com/medals.csv"
    try:
        df = pd.read_csv(url)
        # Get top 10 countries with most medals
        top_countries = df.NOC.value_counts().sort_values(ascending=False).head(10)
        # Convert pandas series to data frame
        to_countries_df = top_countries.to_frame()
        # Save data frame in Excel format - Completar tu propia ubicación para guardar el archivo de salida
        to_countries_df.to_excel('./home/cris/airflow/log/top10_medals_by_country.xlsx')

        #Logging message INFO Success
        logging.info('... Archivo procesado correctamente ...')
    except:
        #Logging message ERROR Fail
        logging.error('... Error al procesar el archivo',exc_info=True)

# task pipeline
read_top10()