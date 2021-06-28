from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 db_checks="",
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.db_checks = db_checks
        self.redshift_conn_id = redshift_conn_id

    def execute(self, context):
        redshift_hook = PostgresHook(self.redshift_conn_id)
        for db_check in self.db_checks:
            records = redshift_hook.get_records(db_check['check_sql'])
            if len(records) != db_check['expected_result']:
                raise ValueError(f"Data quality check failed. {db_check['check_sql']} returned {records[0][0]} results, but expected {db_check['expected_result']} results.")            
            self.log.info(f"Data quality {db_check['check_sql']} check passed with {db_check['expected_result']} records")