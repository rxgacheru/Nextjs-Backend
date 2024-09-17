from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class CandlestickData(APIView):
    def get(self, request):
        data = {
            "candlestickdata": [
                {"x": "2023-01-01", "open": 30, "high": 40, "low": 25, "close": 35},
                {"x": "2023-01-02", "open": 35, "high": 45, "low": 30, "close": 40},
                
            ]
        }
        return Response(data)

class LineChartData(APIView):
    def get(self, request):
        data = {
            "labels": ["Jan", "Feb", "Mar", "Apr"],
            "datasets": [
                {
                    "label": "Sales",
                    "data": [10, 20, 30, 40],
                    "borderColor": "rgba(75, 192, 192, 1)",
                    "backgroundColor": "rgba(75, 192, 192, 0.2)"
                }
            ]
        }
        return Response(data)

class BarChartData(APIView):
    def get(self, request):
        data = {
            "labels": ["Product A", "Product B", "Product C"],
            "datasets": [
                {
                    "label": "Revenue",
                    "data": [100, 150, 200],
                    "backgroundColor": ["rgba(255, 99, 132, 0.2)", "rgba(54, 162, 235, 0.2)", "rgba(255, 206, 86, 0.2)"],
                    "borderColor": ["rgba(255, 99, 132, 1)", "rgba(54, 162, 235, 1)", "rgba(255, 206, 86, 1)"],
                    "borderWidth": 1
                }
            ]
        }
        return Response(data)

class PieChartData(APIView):
    def get(self, request):
        data = {
            "labels": ["Red", "Blue", "Yellow"],
            "datasets": [
                {
                    "data": [300, 50, 100],
                    "backgroundColor": ["#FF6384", "#36A2EB", "#FFCE56"],
                    "hoverBackgroundColor": ["#FF6384", "#36A2EB", "#FFCE56"]
                }
            ]
        }
        return Response(data)
