#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Request
from pygithub3.resources.repos import Release


class List(Request):

    uri = 'repos/{user}/{repo}/releases'
    resource = Release


class Get(Request):

    uri = 'repos/{user}/{repo}/releases/{id}'
    resource = Release


class Create(Request):

    uri = 'repos/{user}/{repo}/releases'
    resource = Release
    body_schema = {
        'schema': ('tag_name', 'target_commitish', 'name', 'body', 'draft', 'prerelease'),
        'required': ('tag_name',),
    }


class Update(Request):

    uri = 'repos/{user}/{repo}/releases/{id}'
    resource = Release
    body_schema = {
        'schema': ('tag_name', 'target_commitish', 'name', 'body', 'draft', 'prerelease'),
        'required': (),
    }


class Delete(Request):

    uri = 'repos/{user}/{repo}/releases/{id}'


# ToDo: Release Assets. - https://developer.github.com/v3/repos/releases/
