# 8.2.6 セキュリティについての注意
# 危険
from xml.etree.ElementTree import parse
et = parse(xmlfiles)
# 対策済み
from defusedxml.ElementTree import parse
et = parse(xmlfile)