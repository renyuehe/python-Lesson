from lxml import etree

if __name__ == '__main__':
    doc='''
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
             </ul>
         </div>
        '''

    html = etree.HTML(doc)
    print(html.xpath("//li"))
    print(html.xpath("//a").__len__())
    print(html.xpath("//a")[0].text)
    print(html.xpath("//p"))

    # html = etree.HTML(doc)
    # print(etree.tostring(html.xpath("//li[@class='item-inactive']")[0]))
    # print(html.xpath("//li[@class='item-inactive']")[0].text)
    # print(html.xpath("//li[@class='item-inactive']/a")[0].text)
    # print(html.xpath("//li[@class='item-inactive']/a/text()"))
    # print(html.xpath("//li[@class='item-inactive']/.."))
    # print(html.xpath("//li[@class='item-inactive']/../li[@class='item-0']"))