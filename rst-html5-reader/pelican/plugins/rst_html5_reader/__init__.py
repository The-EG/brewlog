from .rst_html5_reader import *  # NOQA


from docutils.parsers.rst import directives
from .brewing_directives import Brew, Fermentable, MashStep, BoilItem, FermentationStep, FermentationIngredient
directives.register_directive('brew', Brew)
directives.register_directive('fermentable', Fermentable)
directives.register_directive('mashstep', MashStep)
directives.register_directive('boil_item', BoilItem)
directives.register_directive('ferm_step', FermentationStep)
directives.register_directive('ferm_ingredient', FermentationIngredient)