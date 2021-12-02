from lxml import etree
if __name__ == '__main__':
    doc='''
        <div>
            <ul class='ul items'>
                 <p class="item-0 active"><a href="link1.html">first item</a></p>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
             </ul>
         </div>
        '''

    html = etree.HTML(doc)

    # 最后一个li被限定了
    print(html.xpath("//li[last()]/a/text()"))

    # 会得到所有的`<a>`元素的内容，因为每个<a>标签都是各自父元素的最后一个元素。
    # 本来每个li就只有一个<a>子元素，所以都是最后一个
    print(html.xpath("//li/a[last()]/text()"))
    print(html.xpath("//li/a/text()"))

    # contain
    print(html.xpath("//li/a[contains(text(),'third')]")[0].text)

    # position
    print(html.xpath("//li[position()=2]/a/text()"))
    # 结果为['third item']
    print(html.xpath("//li[last()]/a[position()=1]/text()"))

    # node 就是孩子节点s
    print(html.xpath("//ul/li[@class='item-inactive']/node()"))
    print(html.xpath("//ul/li[@class='item-inactive']"))
    print(html.xpath("//ul/li[@class='item-inactive']/node()/text()"))

    print(html.xpath("//ul[@class='ul items']/node()"))
    # print(html.xpath("/ /ul/node()"))

