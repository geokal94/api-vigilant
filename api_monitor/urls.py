from django.urls import path

from .views import EndpointDetailView, EndpointListCreateView, TestResultListView

urlpatterns = [
    path("endpoints/", EndpointListCreateView.as_view(), name="endpoint-list"),
    path("endpoints/<int:pk>/", EndpointDetailView.as_view(), name="endpoint-detail"),
    path(
        "endpoints/<int:endpoint_id>/results/",
        TestResultListView.as_view(),
        name="test-result-list",
    ),
]
