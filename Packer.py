#!/usr/bin/python

import http.client, urllib, sys, os

#from py_mini_racer import py_mini_racer
from requests_html import HTML

# Define the parameters for the POST request and encode them in
# a URL-safe format.

input = """
function hello(name) {  
    alert('Hello, ' + name);  
}
hello('New user');
"""

print( sys.path[0])


#sys.argv[1])

params = urllib.parse.urlencode([
    ('js_code', input),
    ('compilation_level', 'SIMPLE_OPTIMIZATIONS'),
    ('output_format', 'text'),
    ('output_info', 'compiled_code')
  ])

# Always use the following value for the Content-type header.
headers = { "Content-type": "application/x-www-form-urlencoded" }
conn = http.client.HTTPSConnection('closure-compiler.appspot.com')
conn.request('POST', '/compile', params, headers)
response = conn.getresponse()
html = response.read()
encoding = response.headers.get_content_charset('utf-8')
decoded_html = html.decode(encoding)
print( decoded_html)
conn.close()

print("And doing the JS evaluation")

jsInput = """
function escramble_758(){
    var a,b,c
    a='+1 '
    b='84-'
    a+='425-'
    b+='7450'
    c='9'
    return a+c+b;
}
function Bongle() {
    return 3 * 4;
}
function Processing(input) {
    return input.replace(/e/g, '');
}
"""
#"function hello(name) {   alert('Hello, ' + name);  } hello('New user'); "
jsInput = jsInput + "let content = `" + str(decoded_html) + "`;"

#jsFile = open(os.path.join(sys.path[0], 'Packer.js'))
#jsContents = jsFile.read()
#print(jsContents)

#jsInput = jsInput + jsContents

jsInput = jsInput + """
function DoPack() {
    //let output = packer.Pack(content, true, true);
    let output = Processing(content, true, true);
    return output;
}
"""

print(jsInput)



html = HTML(html="<a href='https://datanirvana.github.io/JavaScript-Minify-Pack/Packer.html'>")

jsInput = """
function escramble_758(){
    var a,b,c
    a='+1 '
    b='84-'
    a+='425-'
    b+='7450'
    c='9'
    return a+c+b;
}
"""

#jsInput = jsInput + "let content = `" + str(decoded_html) + "`;"

jsInput = "function Test() { return packer.Pack('function DoPack()', true, true );}"

val = html.render(script=jsInput, reload=False)
print(val);


jsInput = jsInput + """
function Processing(input) {
    return input.replace(/e/g, '');
}
function DoPack() {
    //let output = packer.Pack(content, true, true);
    let output = Processing(content, true, true);
    return output;
}
"""


#ctx = py_mini_racer.MiniRacer()
#ctx.eval( jsInput)
#temp = ctx.call("escramble_758")
#print(temp)
#temp = ctx.call("Bongle")
#print(temp)
#temp = ctx.call("DoPack")
#print(temp)

