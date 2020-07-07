from selenium import webdriver

from time import sleep

driver = webdriver.Chrome()

# get url
driver.get("http://127.0.0.1")

# js = "alert('i am using selenium execute javascript')"
# driver.execute_script(js)

# 要 return , python才能获取js执行的结果，.实际上selenium 给浏览器注入的是一个函数，so,必须得要有 return

js = '''
function GetElementsAttributes(tag_name,attr){
    return Array.prototype.map.call(document.getElementsByTagName(tag_name),v => v[attr])
}

return GetElementsAttributes('a','href')
'''

print(driver.execute_script(js))

# 上面返回的数组，相当于list。这次试试 return js的 object 会返回什么
# 试试 IIEF
js2 = '''
return (function(){
    return {a:121,b:121,c(){return 3}}
})()
'''

print(driver.execute_script(js2))
# {'a': 121, 'b': 121, 'c': {}}  function 没了，变成了 {}


sleep(2)
# 休息2s退出
driver.quit()
