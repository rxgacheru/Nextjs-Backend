from django.urls import path
from .views import *

urlpatterns = [
    path('api/candlestick-data/', CandlestickData.as_view()),
    path('api/line-chart-data/', LineChartData.as_view()),
    path('api/bar-chart-data/', BarChartData.as_view()),
    path('api/pie-chart-data/', PieChartData.as_view()),
]
