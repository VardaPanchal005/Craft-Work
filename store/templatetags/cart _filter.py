from django import template

register=template.library.Library()

@register.filter(name='currency')
def currency(number):
    return "₹ "+str(number);
     
  
  

