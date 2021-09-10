# 8.2.2 XML
import xml.etree.ElementTree as et
tree = et.ElementTree(file='./08/menu.xml')
root = tree.getroot()
root.tag

for child in root:
    print('tag:', child.tag, 'attributes:', child.attrib)
    for grandchile in child:
        print('\ttag:', grandchile.tag, 'attributes:', grandchile.attrib)

len(root)   # menuセクションの数

len(root[0])    # 朝食の項目の数
