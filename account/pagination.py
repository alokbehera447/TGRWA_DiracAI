from rest_framework.pagination import PageNumberPagination


class DefaultPageNumberPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 100


def wants_pagination(request):
    qp = getattr(request, "query_params", None)
    if not qp:
        return False
    if qp.get("paginate") in ("1", "true", "yes"):
        return True
    if "page" in qp or "page_size" in qp:
        return True
    return False

