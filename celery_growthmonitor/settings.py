from datetime import timedelta

from django.conf import settings as django_settings

from .apps import CeleryGrowthMonitorConfig as appConfig

TTL = getattr(
    django_settings,
    f"{appConfig.name.upper()}_TTL",
    getattr(django_settings, "CELERY_TASK_RESULT_EXPIRES", timedelta(10)),
)  # 10 days
if not isinstance(TTL, timedelta):
    if TTL:
        TTL = timedelta(TTL)
    else:
        # None or 0
        TTL = timedelta(0)
"""
Time to live. After that time, jobs should be dropped from file system.
"""

# Custom prefix in the media root folder
APP_MEDIA_ROOT = getattr(
    django_settings, f"{appConfig.name.upper()}_MEDIA_ROOT", ""
)
