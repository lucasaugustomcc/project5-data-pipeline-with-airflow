from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 table="",
                 sql_select="",
                 append_mode=True,
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.sql_select = sql_select
        self.append_mode = append_mode

    def execute(self, context):
        self.log.info("Connecting to Redshift")
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id) 

        if self.append_mode == False:
            self.log.info("Clearing data from destination Redshift table")
            redshift.run("DELETE FROM {}".format(self.table))

        redshift.run(self.sql_select)
        self.log.info(f"Completed loading {self.table} into dimension table")
