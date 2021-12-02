from lxml import etree
if __name__ == '__main__':
    doc='''
        <div>
            <ul class='ul items'>
                 <li class="item-0 active"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
             </ul>
         </div>
        '''
    html = etree.XML(doc)
    print(html.xpath("//a/text()"))
    print(html.xpath("//a")[0].text)
    print(html.xpath("//ul")[0].text)
    print(len(html.xpath("//ul")[0].text))
    print(html.xpath("//ul/text()"))