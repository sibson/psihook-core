import structlog

LOGGER = structlog.get_logger()


class AddRequestIdMiddleware(object):

    def process_request(self, request):
        request_id = request.META.get('HTTP_X_REQUEST_ID')
        if not request_id:
            return

        request.id = request_id

        global LOGGER
        LOGGER = LOGGER.new(request_id=request_id)
