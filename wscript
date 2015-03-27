#!/usr/bin/env python

TOP = '.'
APPNAME = 'WireCell'

subdirs = ['data',
           'nav',
           'sst',
#           'tiling',
]

def options(ctx):
    ctx.load('find_package', tooldir='waf-tools')

def configure(ctx):
    ctx.load('find_package', tooldir='waf-tools')
    # ctx.env.LIBPATH_WireCell = ctx.options.prefix + '/lib'
    # ctx.env.INCLUDES_WireCell = ctx.options.prefix + '/include'
 
def build(bld):
    bld.recurse(subdirs)

