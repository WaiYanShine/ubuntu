# -*- coding: utf-8 -*-
# Copyright (C) 2014 Canonical
#
# Authors:
#  Didier Roche
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; version 3.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

"""Tests for games framework"""

from . import ContainerTests
import os
from ..large import test_games
from ..tools import get_data_dir, UMAKE


class BlenderInContainer(ContainerTests, test_games.BlenderTests):
    """This will test the Blender editor inside a container"""

    TIMEOUT_START = 20
    TIMEOUT_STOP = 10

    def setUp(self):
        self.hosts = {443: ["www.blender.org", "download.blender.org"]}
        self.apt_repo_override_path = os.path.join(self.APT_FAKE_REPO_PATH, 'blender')
        super().setUp()
        # override with container path
        self.installed_path = os.path.join(self.install_base_path, "games", "blender")


class Unity3DInContainer(ContainerTests, test_games.Unity3DTests):
    """This will test the Unity 3D editor inside a container"""

    TIMEOUT_START = 20
    TIMEOUT_STOP = 10

    def setUp(self):
        self.hosts = {443: ["forum.unity3d.com", "beta.unity3d.com"]}
        self.apt_repo_override_path = os.path.join(self.APT_FAKE_REPO_PATH, 'unity3d')
        super().setUp()
        # override with container path
        self.installed_path = os.path.join(self.install_base_path, "games", "unity3d")


class TwineInContainer(ContainerTests, test_games.TwineTests):
    """This will test Twine inside a container"""

    TIMEOUT_START = 20
    TIMEOUT_STOP = 10

    def setUp(self):
        self.hosts = {443: ["api.github.com", "github.com"]}
        super().setUp()
        # override with container path
        self.installed_path = os.path.join(self.install_base_path, "games", "twine")


class SuperpowersInContainer(ContainerTests, test_games.SuperpowersTests):
    """This will test Superpowers inside a container"""

    TIMEOUT_START = 20
    TIMEOUT_STOP = 10

    def setUp(self):
        self.hosts = {443: ["api.github.com", "github.com"]}
        self.apt_repo_override_path = os.path.join(self.APT_FAKE_REPO_PATH, 'superpowers')
        super().setUp()
        # override with container path
        self.installed_path = os.path.join(self.install_base_path, "games", "superpowers")

    def test_install_with_changed_download_page(self):
        """Installing Superpowers should fail if download page has significantly changed"""
        download_page_file_path = os.path.join(get_data_dir(), "server-content", "api.github.com",
                                               "repos", "superpowers", "superpowers-app", "releases", "latest")
        umake_command = self.command('{} games superpowers'.format(UMAKE))
        self.bad_download_page_test(self.command(self.command_args), download_page_file_path)
        self.assertFalse(self.launcher_exists_and_is_pinned(self.desktop_filename))
        self.assertFalse(self.is_in_path(self.exec_link))


class GDevelopInContainer(ContainerTests, test_games.GDevelopTests):
    """This will test GDevelop inside a container"""

    TIMEOUT_START = 20
    TIMEOUT_STOP = 10

    def setUp(self):
        self.hosts = {443: ["api.github.com", "github.com", "raw.githubusercontent.com"]}
        self.apt_repo_override_path = os.path.join(self.APT_FAKE_REPO_PATH, 'unity3d')
        super().setUp()
        # override with container path
        self.installed_path = os.path.join(self.install_base_path, "games", "gdevelop")

    def test_install_with_changed_download_page(self):
        """Installing GDevelop should fail if download page has significantly changed"""
        download_page_file_path = os.path.join(get_data_dir(), "server-content", "api.github.com",
                                               "repos", "4ian", "GD", "releases", "latest")
        umake_command = self.command('{} games gdevelop'.format(UMAKE))
        self.bad_download_page_test(self.command(self.command_args), download_page_file_path)
        self.assertFalse(self.launcher_exists_and_is_pinned(self.desktop_filename))
        self.assertFalse(self.is_in_path(self.exec_link))


class GodotInContainer(ContainerTests, test_games.GodotTests):
    """This will test Godot inside a container"""

    TIMEOUT_START = 20
    TIMEOUT_STOP = 10

    def setUp(self):
        self.hosts = {443: ["godotengine.org", "downloads.tuxfamily.org"]}
        super().setUp()
        # override with container path
        self.installed_path = os.path.join(self.install_base_path, "games", "godot")

    def test_install_with_changed_download_page(self):
        """Installing Godot should fail if download page has significantly changed"""
        download_page_file_path = os.path.join(get_data_dir(), "server-content", "godotengine.org",
                                               "download", "linux", "index.html")
        umake_command = self.command('{} games godot'.format(UMAKE))
        self.bad_download_page_test(self.command(self.command_args), download_page_file_path)
        self.assertFalse(self.launcher_exists_and_is_pinned(self.desktop_filename))
        self.assertFalse(self.is_in_path(self.exec_link))
