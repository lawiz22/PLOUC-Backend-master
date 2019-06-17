from v1.filters.common import filter_query_params


def album_filter(request, query):
    """
    Filter results based on request query parameters
    """

    allowed = {
        'user': lambda x: int(x),
        'artist_name': lambda x: int(x),
    }

    return filter_query_params(allowed, query, request)
