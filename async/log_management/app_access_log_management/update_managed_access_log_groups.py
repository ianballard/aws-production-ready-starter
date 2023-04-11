import os

from core_lib.utils.lambda_util import lambda_handler
from core_lib.services.logs import log_service


@lambda_handler()
def update_managed_log_groups(event):
    filter_name = "access_log_filter"
    app_access_logger_function_arn = os.getenv("APP_ACCESS_LOGGER_FUNCTION_ARN")
    event_filter = "APP_ACCESS_LOG"

    log_service.put_subscription_filters_on_all_function_logs(
        filter_name=filter_name,
        destination_arn=app_access_logger_function_arn,
        event_filter=event_filter,
    )