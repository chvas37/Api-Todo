from drf_yasg import openapi

api_info = openapi.Info(
    title="todoapp",
    default_version='v1',
    description="My API description",
    terms_of_service="https://www.todoapp.com/terms/",
    contact=openapi.Contact(email="contact@todoapp.com"),
    license=openapi.License(name="My License"),
)