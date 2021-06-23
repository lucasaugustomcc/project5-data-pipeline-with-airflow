from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 table="",
                 sql_select="",
                 append_mode=False,
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.sql_select = sql_select

    def execute(self, context):
        self.log.info("Copying data from S3 to Redshift")
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)        
        redshift.run(self.sql_select)
        self.log.info(f"Completed staging to {self.table}")
