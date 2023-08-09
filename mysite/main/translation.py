from .models import Category
from modeltranslation.translator import register, TranslationOptions

@register(Category)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name',)