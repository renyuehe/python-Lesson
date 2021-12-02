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
    print(html.xpath("//*[contains(@class,'item')]"))
    print(html.xpath("//*[starts-with(@class,'ul')]"))
    # print(html.xpath("//*[ends-with(@class,'1')]")) # python 的 xpath 不支持所有的 xpath 列表
    # print(html.xpath("//a[contains(upper-case(@class),'ITEM-INACTIVE')]")) # 也不支持

