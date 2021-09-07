# 8.2.5 YAML
name:
  first: James
  last: McIntyre
dates:
  birth: 1828-05-25
  death: 1906-03-31
datails:
  bearded: true
  themes: [cheese, Canada]
books:
  url: http://www.gutenberg.org/files/36068/36068-h/36068-h.html
poems:
  -title: 'Motto'
  text: |
    politeness, perseverance and pluck,
    To their possessor will bring good luck.
  -title: 'Canadian Charms'
  text: |
    Here industry is not in vain,
    For we have bounteous crops of grain,
    And you behold on every field
    Of grass and roots abundant yield,
    But after all the greatest charm
    Is the sung home upon the farm,
    And stone walls now keep cattle warm.

import YAML
with open('mcintyre.yaml', 'rt') as fin:
  text = fin.read()

data = YAML.load(text)
data['details']

len(data['poems'])

data('poems'[1]['title'])