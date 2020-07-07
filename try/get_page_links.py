from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

url = "http://127.0.0.1/"

# for a f2e , maybe i'd better using Javascript function instead of selenium's methods
# let's write that javascript function
js = '''
getElementInfo = {
    getElementsAttributes(tag_name, attr) {
        return Array.prototype.map.call(document.getElementsByTagName(tag_name), v => v[attr])
    },
      getLocationHref() {
        return window.location.href
    }
}

get_a_href = Object.assign({
    getLink() {
        return this.getElementsAttributes("a", "href")
    }
}, getElementInfo)

get_iframe_src = Object.assign({
    getLink() {
        return this.getElementsAttributes("iframe", "src");
    }
}, getElementInfo)

return {
    a_links:get_a_href.getLink(),
    iframe_links: get_iframe_src.getLink(),
    frame_links: getElementInfo.getElementsAttributes("frame","src"),
    location_href: getElementInfo.getLocationHref()
}
'''

chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)

print(driver.execute_script(js))

sleep(2)

driver.quit()
