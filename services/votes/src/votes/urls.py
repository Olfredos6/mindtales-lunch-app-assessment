from rest_framework.routers import DefaultRouter
from voteapi.views import VoteViewSet


router = DefaultRouter()
router.register(r"votes", VoteViewSet)

urlpatterns = router.urls
