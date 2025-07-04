def get_operator_from_request(request):
    name_from_url = request.GET.get("operator-name")
    if name_from_url:
        request.session["selected_operator"] = name_from_url
        return name_from_url
    return request.session.get("selected_operator")
