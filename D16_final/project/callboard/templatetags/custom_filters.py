from django import template


register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def uf(value):
   for i in value:
      if str(i) == 'Набор':
         value = value.replace(i, '')
   return str(value)