from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive

def make_entry(text, classes=[]):
    entry = nodes.entry()
    entry['classes'] = classes
    p = nodes.paragraph(text, text)
    entry += p

    return entry

def make_table(cols):
    tbl = nodes.table()
    tbl['classes'] = ['table']

    tgroup = nodes.tgroup(cols=len(cols))
    for n in cols: tgroup += nodes.colspec()
    tbl += tgroup

    thead = nodes.thead()
    tgroup += thead
    row = nodes.row()
    thead += row

    for name in cols: row += make_entry(name, cols[name])        

    tbody = nodes.tbody()
    tgroup += tbody

    tbl.body_node = tbody

    return tbl
    
class ListRow(Directive):
    required_arguments = 1
    final_argument_whitespace = True

    has_content = False

    option_spec = {}

    arg_classes = []

    brew_child_type = 'None'

    def run(self):
        rawargs = self.arguments[0]
        if ';' in rawargs: args = rawargs.split(';')
        else: args = rawargs.split(',')

        args = [a.strip() for a in args]

        row = nodes.row()
        for name, classes in zip(args, self.arg_classes):
            row += make_entry(name, classes)
        
        row.brew_child_type = self.brew_child_type

        return [row]

class BoilItem(ListRow):
    arg_classes = [
        ['text-end'], # time
        [],           # name
        ['text-end'], # amount
        ['text-end'], # aa
        ['text-end']  #ibus
    ]

    brew_child_type = 'boil'

class MashStep(ListRow):
    arg_classes = [
        ['text-end'], # step
        [],           # type
        ['text-end'], # time
        [],           # target
        [],           # strike
        []            # amount
    ]

    brew_child_type = 'mash'

class Fermentable(ListRow):
    arg_classes = [
        ['text-end'], # perc
        [],           # name
        ['text-end'], # color
        []
    ]

    brew_child_type = 'fermentable'

class FermentationStep(ListRow):
    arg_classes = [
        [], [], []
    ]

    brew_child_type = 'ferment_step'

class FermentationIngredient(ListRow):
    arg_classes = [
        [], [], []
    ]

    brew_child_type = 'ferment_ingredient'

class Brew(Directive):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True

    option_spec = {
        'name': directives.unchanged_required,
        'style': directives.unchanged,
        'og': directives.unchanged_required,
        'fg': directives.unchanged_required,
        'abv': directives.unchanged_required,
        'volume': directives.unchanged_required,
        'efficiency': directives.unchanged,
        'boil_length': directives.unchanged_required,
        'ibus': directives.unchanged,
        'color': directives.unchanged,
        'act_og': directives.unchanged,
        'act_fg': directives.unchanged,
        'act_abv': directives.unchanged,
        'packaged': directives.unchanged,
        'carbonation': directives.unchanged
    }

    has_content = True

    def summary_row(self, name, value):
        row = nodes.row()

        title = nodes.strong(name, name)
        entry = nodes.entry()
        entry['classes'] = ['text-end']
        row += entry
        entry += title

        val = nodes.paragraph(value, value)
        entry = nodes.entry()
        row += entry
        entry += val

        return row

    def run(self):
        self.assert_has_content()

        grid = nodes.container()
        grid['classes'] += ['container-fluid']

        row = nodes.container()
        row['classes'] += ['row', 'justify-content-end']
        grid += row

        summary_col = nodes.container()
        summary_col['classes'].extend(['col-lg-4', 'col-12', 'd-flex','flex-column', 'justify-content-between'])
        row += summary_col

        summarytbl = nodes.table()
        summarytbl['classes'] = ['table']
        infodiv = nodes.container()
        infodiv += nodes.paragraph('Beer Info', 'Beer Info')
        infodiv += summarytbl
        summary_col += infodiv

        tgroup = nodes.tgroup(cols=2)
        tgroup += nodes.colspec()
        tgroup += nodes.colspec()
        summarytbl += tgroup

        summarybdy = nodes.tbody()
        tgroup += summarybdy

        opts = [
            ('Name', 'name'),
            ('Style', 'style'),
            ('Est. OG', 'og'),
            ('Est. FG', 'fg'),
            ('Est. ABV', 'abv'),
            ('Volume', 'volume'),
            ('Efficiecy', 'efficiency'),
            ('Boil Length', 'boil_length'),
            ('Est. IBUs', 'ibus'),
            ('Est. Color', 'color')
        ]

        for lbl, key in opts:
            if key in self.options:
                summarybdy += self.summary_row(lbl, self.options[key])

        brewdaytbl = nodes.table()
        brewdaytbl['classes'] = ['table']
        brewdaydiv = nodes.container()
        brewdaydiv += nodes.paragraph('Results','Results')
        brewdaydiv += brewdaytbl
        summary_col += brewdaydiv

        tgroup = nodes.tgroup(cols=2)
        tgroup += nodes.colspec()
        tgroup += nodes.colspec()
        brewdaytbl += tgroup

        brewdaybody = nodes.tbody()
        tgroup += brewdaybody

        brewdayvals = [
            ('Actual OG', 'act_og'),
            ('Actual FG', 'act_fg'),
            ('Actual ABV', 'act_abv'),
            ('Packaged On', 'packaged'),
            ('Carbonation', 'carbonation')
        ]

        for lbl, key in brewdayvals:
            val = self.options[key] if key in self.options else ''
            brewdaybody += self.summary_row(lbl, val)

        detailscol = nodes.container()
        detailscol['classes'].extend(['col-lg-8', 'col-12'])
        row += detailscol

        fermentables = make_table({
            "%": ['text-end'],
            "Name": [],
            "Color": ['text-end'],
            "Amount": []
        })
        detailscol += nodes.paragraph('Fermentables','Fermentables')
        detailscol += fermentables

        mash = make_table({
            "Step": ['text-end'],
            "Type": [],
            "Time": ['text-end'],
            "Target": [],
            "Strike": [],
            "Amount": []
        })
        detailscol += nodes.paragraph('Mash','Mash')
        detailscol += mash

        boil = make_table({
            'Time': ['text-end'],
            'Name': [],
            'Amount': ['text-end'],
            'AA%': ['text-end'],
            'IBUs': ['text-end']
        })
        detailscol += nodes.paragraph('Boil','Boil')
        detailscol += boil

        ferment_steps = make_table({
            'Step': [],
            'Time': [],
            'Temp': []
        })
        detailscol += nodes.paragraph('Fermentation Steps', 'Fermentation Steps')
        detailscol += ferment_steps

        ferment_ingredients = make_table({
            'Name': [],
            'Step': [],
            'Amount': []
        })
        detailscol += nodes.paragraph('Fermentation Ingredients', 'Fermentation Ingredients')
        detailscol += ferment_ingredients

        children = nodes.Element()
        self.state.nested_parse(self.content, self.content_offset, children)

        child_types = {
            'fermentable': fermentables,
            'mash': mash,
            'boil': boil,
            'ferment_step': ferment_steps,
            'ferment_ingredient': ferment_ingredients
        }

        for child in children:
            if not hasattr(child, 'brew_child_type'): continue
            if child.brew_child_type in child_types:
                child_types[child.brew_child_type].body_node += child

        return [grid]

