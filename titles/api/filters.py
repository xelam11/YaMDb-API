import django_filters

from titles.models import Title


class TitleFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(
        field_name='category', lookup_expr='slug'
    )
    genre = django_filters.CharFilter(field_name='genre', lookup_expr='slug')
    name = django_filters.CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = Title
        fields = ('category', 'genre', 'name', 'year')
