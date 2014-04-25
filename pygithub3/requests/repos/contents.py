#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Request
from pygithub3.resources.repos import Content

class Get(Request):

    uri = 'repos/{user}/{repo}/contents/{path}'
    resource = Content


class Create(Request):

    uri = 'repos/{user}/{repo}/contents/{path}'
    resource = Content
    body_schema = {
        'schema': ('path', 'message', 'content', 'branch'),
        'required': ('path','message','content'),
    }


class Update(Request):

    uri = 'repos/{user}/{repo}/contents/{path}'
    resource = Content
    body_schema = {
        'schema': ('path', 'message', 'content', 'sha', 'branch'),
        'required': ('path', 'message', 'content', 'sha'),
    }


class Delete(Request):

    uri = 'repos/{user}/{repo}/contents'
    body_schema = {
        'schema': ('path', 'message', 'sha', 'branch'),
        'required': ('path', 'message', 'sha')
    }


# ToDo: Release Assets. - https://developer.github.com/v3/repos/releases/
