"""Project-level app configuration."""

from django.apps import AppConfig, apps
from django.utils.module_loading import import_module


class ProjectConfig(AppConfig):
    """Configuration that applies to the entire project."""

    name = 'project'

    def ready(self):
        """Perform any project-wide initialization."""
        for app in apps.get_app_configs():
            # Import all serializers modules to ensure API serialization code
            # is initialized (i.e. all defined serializers are registered).
            try:
                import_module('{}.serializers'.format(app.name))
            except ModuleNotFoundError:
                pass
