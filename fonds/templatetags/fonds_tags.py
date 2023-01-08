from django import template
register = template.Library()

def twopart(a_list):
    half = len(a_list)//2
    k = [a_list[:half], a_list[half:]]
    return list(map(lambda x: ''.join(x), k))

@register.filter
def firstpart(a_list):
    return twopart(a_list)[0]

@register.filter
def secondpart(a_list):
    return twopart(a_list)[1]

@register.filter
def index(indexable, i):
    return indexable[i]

@register.filter
def get_photo_url(value):
    return value.photo.url

@register.filter
def range_temp(value):
    return range(value)
