from django.shortcuts import render, redirect
from commons.views import RegressView
from records.models import Records
from blog.core import paged


class RecordItem(RegressView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = "records/item.html"

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.c_page(**kwargs)
        record = Records.published_items.by_id(page)
        context.update({
            "record": record.get(),
        })
        return render(request, self.template_name, context)


class RecordList(RegressView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = "records/list.html"

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.c_page(**kwargs)
        if page is "1":
            return redirect("/records/")
        data, pagination = paged(Records.published_items.list_items(), page)
        context.update({
            "list": data,
            "pagination": pagination,
        })
        return render(request, self.template_name, context)
