#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Service


class Contents(Service):
    """ Consume `Contents API
    <http://developer.github.com/v3/repos/contents>`_

    """

    def get(self, file_path, user=None, repo=None):
        """ Get a single file

        :param str path: file path
        :param str user: Username
        :param str repo: Repository

        .. note::
            Remember :ref:`config precedence`
        """
        request = self.make_request('repos.contents.get',
            path=file_path, user=user, repo=repo)
        return self._get(request)

    def create(self, file_path, data, user=None, repo=None):
        """ Create a file

        :param dict data: Input. See `github content doc`_
        :param str user: Username
        :param str repo: Repository

        .. note::
            Remember :ref:`config precedence`

        ::

            data = {
                "path": "README.md",
                "message": "This is my commit message",
                "content": "xyz...",
                "branch": "master"
            }
            contents_service.create(data, user='octocat', repo='oct_repo')
        """
        request = self.make_request('repos.contents.create',
            path=file_path, user=user, repo=repo, body=data)
        return self._put(request)

    def update(self, file_path, data, user=None, repo=None):
        """ Update a single file

        :param dict data: Input. See `github content doc`_
        :param str user: Username
        :param str repo: Repository

        .. note::
            Remember :ref:`config precedence`

        ::

            releases_service.update(dict(path='README.md'), user='octocat',
                repo='oct_repo')
        """
        request = self.make_request('repos.contents.update',
            path=file_path, user=user, repo=repo, body=data)
        return self._put(request)

    def delete(self, data, user=None, repo=None):
        """ Delete a single release

        :param dict data: Input. See `github content doc`_
        :param str user: Username
        :param str repo: Repository

        .. note::
            Remember :ref:`config precedence`
        """
        request = self.make_request('repos.contents.delete',
            user=user, repo=repo, body=data)
        self._delete(request)
