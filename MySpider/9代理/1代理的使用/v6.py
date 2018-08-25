from selenium import webdriver

service_args = [
    '--proxy=111.155.116.245:8123',
    '--proxy-type=http'
    '--proxy-auth=username:password'
]
browser = webdriver.PhantomJS(service_args=service_args)
browser.get('http://httpbin.org/get')
print(browser.page_source)