from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats_female = (
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{prefix_female}} {{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}} {{suffix_female}}',
        '{{prefix_female}} {{first_name_female}} {{last_name}} {{suffix_female}}')

    formats_male = (
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{prefix_male}} {{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}} {{suffix_male}}',
        '{{prefix_male}} {{first_name_male}} {{last_name}} {{suffix_male}}',
    )

    formats = formats_male + formats_female

    first_names_female = ('Jeff')
    first_names_male = ('Jeff')

    first_names = first_names_male + first_names_female

    last_names = ('Sushi')

    prefixes_female = ('Mrs.', 'Ms.', 'Miss', 'Dr.')
    prefixes_male = ('Mr.', 'Dr.')

    suffixes_female = ('MD', 'DDS', 'PhD', 'DVM')
    suffixes_male = ('Jr.', 'Sr.', 'I', 'II', 'III',
                     'IV', 'V', 'MD', 'DDS', 'PhD', 'DVM')
