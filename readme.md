# Application Name: Spot
Spot is built using Python (Django) for exposing API endpoints for price and rates

## Installation
The environment required for the application can be setup using requirement.txt file present in the project directory


## Running the application at 5000 port
The application can be run at 5000 port using the command "python manage.py runserver 5000"

## Credentials for admin page
The admin page can be viewed using below credentials

admin: admin
password: admin

## Automatic JSON uploader
The JSON file will be automatically uploaded at the start of the project.
File needs to be placed inside static folder with the name "rates.json"
The data format needs to be in the same format as provided in the sample file present in the folder

## API endpoints
```Python

router = DefaultRouter()
router.register('rates', views.parkingRateViewset, basename = 'rates')

######### Router Configuration Starts Here ########


urlpatterns = [
    path('admin/', admin.site.urls),                                              # This url leads you to admin page
    path('', views.JsonData),                                                     # This url leads you to home page for automatic json file upload 
    path('api/price', views.priceapi),                                            # This url is for price api endpoint
    path('api/', include(router.urls)),                                           # This url is for rates api endpoint
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # This url is for swagger
]

```
The above code block gives details about the available api end points and other urls

1. rates api endpoint
[link name] (127.0.0.1:5000/api/rates)

This api endpoint helps to fetch parking rates available in the database. 
User can also retrieve single data point specifying the pk
User can update the parking rates through this endpoint specifying the pk

2. price api endpoint
[link name] (127.0.0.1:5000/api/price)

This api endpoint helps to fetch price for the parking as per the query parameter.
The query parameters "start" and "end" should in ISO-8601 date format as mentioned in the test guideline

## Swagger Spec
The Swagger Spec is avaible at below url
[link name] (127.0.0.1:5000/swagger)

## Browsable API
The Browsable API is also present at each API endpoints for load testing

## Dockerfile
The dockerfile is present in the project folder to prepare docker image

## Performance Metrics
The snapshot of performance metrics for the exposed endpoints is captured in "Performance_Metrics.png" file located in project directory. The testing is done using Locust


