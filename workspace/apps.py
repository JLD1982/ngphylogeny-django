from __future__ import unicode_literals

from django.apps import AppConfig


class WorkspaceConfig(AppConfig):
    name = 'workspace'

    def ready(self):
        import workspace.signals
