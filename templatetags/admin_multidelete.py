from django import template
from django.contrib.admin.templatetags.admin_list import result_headers, items_for_result

register = template.Library()

def results_multidelete(cl):
    for res in cl.result_list:
        yield dict(pk=getattr(res, cl.pk_attname), field_list=list(items_for_result(cl,res)))

def result_list_multidelete(cl):
    return {'cl': cl,
            'result_headers': list(result_headers(cl)),
            'results': list(results_multidelete(cl))}
result_list_multidelete = register.inclusion_tag("admin/change_list_results.html")(result_list_multidelete)

