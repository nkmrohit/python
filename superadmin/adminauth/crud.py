from crudbuilder.abstract import BaseCrudBuilder
from .models import Person

from crudbuilder.abstract import BaseCrudBuilder
from crudbuilder.formset import BaseInlineFormset

class PersonCrud(BaseCrudBuilder):
        model = Person
        search_fields = ['name']
        tables2_fields = ('name', 'email')
        tables2_css_class = "table table-bordered table-condensed"
        tables2_pagination = 20  # default is 10
        modelform_excludes = ['created_by', 'updated_by']
        login_required=True
        permission_required=True
        # permissions = {
        #   'list': 'example.person_list',
        #       'create': 'example.person_create'
        # }