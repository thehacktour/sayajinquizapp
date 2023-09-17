from .views import QuizEndPoint
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register("quiz", QuizEndPoint, basename="quiz")

urlpatterns = router.urls