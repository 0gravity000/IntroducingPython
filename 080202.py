# 8.2.2 XML
<?XML verion="1.0"?>
<menu>
    <breakfast hours="7-11">
        <item price="$6.00">breakfast burritos</item>
        <item price="$4.00">pancakes</item>
    </breakfast>
    <lunch hours="11-3">
        <item price="$5.00">hamburger</item>
    </lunch>
    <dinner hours="3-10">
        <item price="$8.00">spaghetti</item>
    </dinner>
</menu>

import xml.etree.ElementTree as et
tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
root.tag

for child in root:
    print('tag:', child.tag, 'attributes:', child.attrib)
    for grandchile in child:
        print('¥ttag:', grandchile.tag, 'attributes:', grandchile.attrib)

len(root)   # menuセクションの数

len(root[0])    # 朝食の項目の数