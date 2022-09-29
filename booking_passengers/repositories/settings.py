from conf import settings

import dataclasses
from backend_shared.page_settings.repository import prismic_repo
from backend_shared.page_settings.session_manager import SessionManager


dataclasses.dataclass
class SettingsReposiory(prismic_repo.SettingsRepository):
    PRISMIC_ENDPOINT = settings.PRISMIC_ENDPOINT
    PRISMIC_TOKEN = settings.PRISMIC_TOKEN
    SESSION_MANAGER = SessionManager().get()
    TEMPLATE_PATH = settings.TEMPLATES_PATH
    TEMPLATE_NAME = settings.TEMPLATE_NAME
    EMAIL_SOPORTE = settings.EMAIL_SOPORTE
    CONNECTION_STR = settings.CONNECTION_STR
    AZURE_QUEUE = settings.AZURE_QUEUE





    