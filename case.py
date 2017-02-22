#!/usr/bin/env python 
import sys
import os
import inflection
if len(sys.argv) < 2 or len(sys.argv[1].strip()) == 0:
	arg = os.popen("pbpaste").read().strip()
else:
    arg = sys.argv[1]

camel = inflection.camelize(inflection.underscore(arg), False)
pascal = inflection.camelize(inflection.underscore(arg))
snake = inflection.underscore(arg)
constant = inflection.underscore(arg).upper()
dash = inflection.dasherize(inflection.underscore(arg))
human = inflection.humanize(inflection.underscore(arg))

output = """
<?xml version="1.0"?>
<items>
    <item valid="YES">
        <title>""" + camel+ """</title>
        <subtitle>camelCase</subtitle>
        <icon>icon.png</icon>
        <arg>""" + camel+ """</arg>
    </item>
    <item valid="YES">
        <title>""" + snake+ """</title>
        <subtitle>snake_case</subtitle>
        <icon>icon.png</icon>
        <arg>""" + snake+ """</arg>
    </item>
    <item valid="YES">
        <title>""" + constant + """</title>
        <subtitle>CONST_CASE</subtitle>
        <icon>icon.png</icon>
        <arg>""" + constant+ """</arg>
    </item>
    <item valid="YES">
        <title>""" + pascal+ """</title>
        <subtitle>PascalCase</subtitle>
        <icon>icon.png</icon>
        <arg>""" + pascal+ """</arg>
    </item>
    <item valid="YES">
        <title>""" + dash+ """</title>
        <subtitle>dash-case</subtitle>
        <icon>icon.png</icon>
        <arg>""" + dash+ """</arg>
    </item>
    <item valid="YES">
        <title>""" + human + """</title>
        <subtitle>Human case</subtitle>
        <icon>icon.png</icon>
        <arg>""" + human + """</arg>
    </item>
</items>
"""
print output