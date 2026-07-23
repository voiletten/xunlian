### BS4核心语法

- 创建解析对象 ： BeautifulSoup(resp.text, "html.parser") - 解析HTML
- CSS选择器 ： soup.select("div.news_box ul li h4") - 选择新闻标题元素
- 获取文本 ： get_text(strip=True) - 获取标签内文本并去除空白
- 获取属性 ： ["href"] - 获取链接属性
  
  ### 反爬问题及解决
  
  问题 ：使用了未安装的 lxml 解析器库

解决 ：改用 Python 内置的 html.parser 解析器，无需额外安装

代码中也设置了 headers（User-Agent、Referer等）来模拟浏览器访问，避免被识别为爬虫。
