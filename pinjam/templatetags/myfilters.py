from django import template
from django.http import QueryDict

register = template.Library()

@register.filter(name='addclass')
def addclass(value, args):

	qs = QueryDict(args)
	if qs.get('classes') and qs.get('place'):
		return value.as_widget(attrs={'class':qs['classes'],'placeholder':qs['place']})
	else:
		return value.as_widget(attrs={'class':'input100'})
