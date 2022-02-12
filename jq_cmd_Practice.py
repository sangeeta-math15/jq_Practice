#Call jq.compile to compile a jq program. Call .input() on the compiled program to supply an input value. The input must either be:
#a valid JSON value, such as the values returned from json.load
#unparsed JSON text passed as the keyword argument text.
#Calling first() on the result will run the program with the given input, and return the first output element.

import jq
print(jq.compile(".").input("hello").first() == "hello")
print(jq.compile(".").input(text='"hello"').first() == "hello")
print(jq.compile("[.[]+1]").input([1, 2, 3]).first() == [2, 3, 4])
print(jq.compile(".[]+1").input([1, 2, 3]).first() == 2)


#Call text() instead of first() to serialise the output into JSON text:
print(jq.compile(".").input("42").text() == '"42"')

#When calling text(), if there are multiple output elements, each element is represented by a separate line:
print(jq.compile(".[]").input([1, 2, 3]).text() == "1\n2\n3")

#Call all() to get all of the output elements in a list:
print(jq.compile(".[]+1").input([1, 2, 3]).all() == [2, 3, 4])

#Call iter() to get all of the output elements as an iterator:
iterator = iter(jq.compile(".[]+1").input([1, 2, 3]))
print(next(iterator, None) == 2)
print(next(iterator, None) == 3)
print(next(iterator, None) == 4)
print(next(iterator, None) == None)

#Calling compile() with the args argument allows predefined variables to be used within the program:
program = jq.compile("$a + $b + .", args={"a": 100, "b": 20})
print(program.input(3).first() == 123)

#Convenience functions are available to get the output for a program and input in one call:
print(jq.first(".[] + 1", [1, 2, 3]) == 2)
print(jq.first(".[] + 1", text="[1, 2, 3]") == 2)
print(jq.text(".[] + 1", [1, 2, 3]) == "2\n3\n4")
print(jq.all(".[] + 1", [1, 2, 3]) == [2, 3, 4])
print(list(jq.iter(".[] + 1", [1, 2, 3])) == [2, 3, 4])

#The original program string is available on a compiled program as the program_string attribute:
program = jq.compile(".")
print(program.program_string == ".")

#Object Identifier-Index: .foo
print(jq.compile(".foo").input({"foo":42, "bar":"less interesting data"}).first())

#Optional Object Identifier-Index: .foo?
print(jq.compile('.foo?').input({"foo":42,"bar":"less intersting data"}).first())

#Array Index: .[2]
print(jq.compile('.[0]').input([{"name":"JSON", "good":"true"}, {"name":"XML", "good":"false"}]).all())

#array index slicing
print(jq.compile('.[-2]').input(["a","b","c","d","e"]).all())

#Array/Object Value Iterator: .[]
print(jq.compile('.[]').input([{"name":"JSON", "good":"true"}, {"name":"XML", "good":"false"}]).all())

#comma :,
print(jq.compile('.user').input({"user":"stedolan", "projects": ["jq", "wikiflow"]}).all())

#pipe:|
print(jq.compile('.[]|.name').input([{"name":"JSON", "good":"true"}, {"name":"XML", "good":"false"}]).all())

#paranthesis
print(jq.compile('(. + 2 ) * 5').input(1).all())

#Types and Values:
#Array construction: []
print(jq.compile('[.user, .projects[]]').input({"user":"stedolan", "projects": ["jq", "wikiflow"]}).all())

#object construction:()
print(jq.compile('{user, titiles: .titles[]}').input({"user":"stedolan","titles":["JQ Primer", "More JQ"]}).all())

print(jq.compile('{(.user): .titles}').input({"user":"stedolan","titles":["JQ Primer", "More JQ"]}).all())

#Recursive Descent: ..
print(jq.compile("..|.a?").input([{"a":1}]).first())

#Builtin operators and functions
#Addition
print(jq.compile(".a + .b").input({"a":[1,2], "b": [3,4]}).first())

#substraction
print(jq.compile('. - ["xml", "yaml"]').input(["xml", "yaml", "json"]).first())

#multiplication
print(jq.compile('{"k": {"a": 1, "b": 2}} * {"k": {"a": 0,"c": 3}}').input("null").all())

#length
print(jq.compile('.[] | length').input([[1,2], "string", {"a":2}, "null"]).all())

#has(key)
print(jq.compile('map(has("foo"))').input([{"foo":42}, {}]).all())

print(jq.compile('map(has(2))').input([[0,1], ["a","b","c"]]).all())







