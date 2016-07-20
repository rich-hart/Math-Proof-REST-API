from django.conf.urls import url, include
from rest_framework import routers
from .views import ProofViewSet, StatementViewSet 

router = routers.DefaultRouter()
router.register(r'proofs', ProofViewSet)
router.register(r'statements', StatementViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
