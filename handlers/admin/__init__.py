from aiogram import Router
from .notification_admin import notication_router
from .photo_admin import photo_router


admin_router = Router()
admin_router.include_router(photo_router)
admin_router.include_router(notication_router)
