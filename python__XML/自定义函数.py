from lxml import etree

#定义函数
def ends_with(context,s1,s2):
    return s1[0].endswith(s2)

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
    ns = etree.FunctionNamespace(None)
    ns['ends-with'] = ends_with #将ends_with方法注册到方法命名空间中
    print(html.xpath("//li[ends-with(@class,'active')]"))
    print(html.xpath("//li[ends-with(@class,'active')]/a/text()"))
