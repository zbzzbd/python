locarot_suffer={

    ('css', 'default'): [''],
    ('css', 'content'): [''],
    ('css', 'header'): [' th'],
    ('css', 'footer'): [' tfoot td'],
    ('css', 'row'): [' tr:nth-child(%s)'],
    ('css', 'last-row'): [' tr:nth-last-child(%s)'],
    ('css', 'col'): [' tr td:nth-child(%s)', ' tr th:nth-child(%s)'],
    ('css', 'last-col'): [' tr td:nth-last-child(%s)', ' tr th:nth-last-child(%s)'],

}

print locarot_suffer[('css', 'last-row')]