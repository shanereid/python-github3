#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Service


class Releases(Service):
    """ Consume `Releases API
    <http://developer.github.com/v3/repos/releases>`_

    """

    def list(self, user=None, repo=None):
        """ Get repository's releases

        :param str user: Username
        :param str repo: Repository
        :returns: A :doc:`result`

        .. note::
            Remember :ref:`config precedence`
        """
        request = self.make_request('repos.releases.list', user=user, repo=repo)
        return self._get_result(request)

    def get(self, release_id, user=None, repo=None):
        """ Get a single release

        :param int release_id: Release id
        :param str user: Username
        :param str repo: Repository

        .. note::
            Remember :ref:`config precedence`
        """
        request = self.make_request('repos.releases.get',
            id=release_id, user=user, repo=repo)
        return self._get(request)

    def create(self, data, user=None, repo=None):
        """ Create a release

        :param dict data: Input. See `github release doc`_
        :param str user: Username
        :param str repo: Repository

        .. note::
            Remember :ref:`config precedence`

        ::

            data = {
                "tag_name": "v1.0.0",
                "target_committish": "abcde....",
                "name": "v1.0.0 'Snowbunny'",
                "body": "This is a release",
                "draft": True,
                "prerelease": False
            }
            releases_service.create(data, user='octocat', repo='oct_repo')
        """
        request = self.make_request('repos.releases.create',
            user=user, repo=repo, body=data)
        return self._post(request)

    def update(self, release_id, data, user=None, repo=None):
        """ Update a single release

        :param int release_id: Release id
        :param dict data: Input. See `github hooks doc`_
        :param str user: Username
        :param str repo: Repository

        .. note::
            Remember :ref:`config precedence`

        ::

            releases_service.update(42, dict(draft=False), user='octocat',
                repo='oct_repo')
        """
        request = self.make_request('repos.releases.update',
            id=release_id, user=user, repo=repo, body=data)
        return self._patch(request)

    def delete(self, release_id, user=None, repo=None):
        """ Delete a single release

        :param int release_id: Release id
        :param str user: Username
        :param str repo: Repository

        .. note::
            Remember :ref:`config precedence`
        """
        request = self.make_request('repos.releases.delete',
            id=release_id, user=user, repo=repo)
        self._delete(request)
