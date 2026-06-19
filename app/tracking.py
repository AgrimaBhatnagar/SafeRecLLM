import mlflow

def log_query(query, results_count):

    with mlflow.start_run():

        mlflow.log_param(
            "query",
            query
        )

        mlflow.log_metric(
            "results_count",
            results_count
        )
