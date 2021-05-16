#AQI dictionary PM25
pm25_dict = {
    "lev1" : {
        "ihigh" : 50,
        "ilow" : 1,
        "chigh" : 12,
        "clow" : 1,
        "air" : "Good"
        },
    "lev2" : {
        "ihigh" : 100,
        "ilow" : 51,
        "chigh" : 35.4,
        "clow" : 12.1,
        "air" : "Moderate"
        },
    "lev3" : {
        "ihigh" : 150,
        "ilow" : 101,
        "chigh" : 55.4,
        "clow" : 35.5,
        "air" : "Unhealthy for Sensitive Groups"
        },
    "lev4" : {
        "ihigh" : 200,
        "ilow" : 151,
        "chigh" : 150.4,
        "clow" : 55.5,
        "air" : "Unhealthy"
        },
    "lev5" : {
        "ihigh" : 300,
        "ilow" : 201,
        "chigh" : 250.4,
        "clow" : 150.5,
        "air" : "Very Unhealthy"
        },
    "lev6" : {
        "ihigh" : 400,
        "ilow" : 301,
        "chigh" : 350.4,
        "clow" : 250.5,
        "air" : "Hazardous"
        },
    "lev7" : {
        "ihigh" : 500,
        "ilow" : 401,
        "chigh" : 500.4,
        "clow" : 350.5,
        "air" : "Hazardous"
        },
    "lev8" : {
        "ihigh" : 1000,
        "ilow" : 501,
        "chigh" : 1001,
        "clow" : 500.5,
        "air" : "Hazardous and very difficult for indoor air purifiers and Delhirium"
        }
    }
#PM10 dictionary ilow and ihigh are AQI category delimiters
#chigh and clow are pollutant delimiters
#air is the level of health concern
pm10_dict = {
    "lev1" : {
        "ihigh" : 50,
        "ilow" : 1,
        "chigh" : 50,
        "clow" : 1,
        "air" : "Good"
        },
    "lev2" : {
        "ihigh" : 100,
        "ilow" : 51,
        "chigh" : 154,
        "clow" : 51,
        "air" : "Moderate"
        },
    "lev3" : {
        "ihigh" : 150,
        "ilow" : 101,
        "chigh" : 254,
        "clow" : 155,
        "air" : "Unhealthy for Sensitive Groups"
        },
    "lev4" : {
        "ihigh" : 200,
        "ilow" : 151,
        "chigh" : 354,
        "clow" : 255,
        "air" : "Unhealthy"
        },
    "lev5" : {
        "ihigh" : 300,
        "ilow" : 201,
        "chigh" : 424,
        "clow" : 355,
        "air" : "Very Unhealthy"
        },
    "lev6" : {
        "ihigh" : 400,
        "ilow" : 301,
        "chigh" : 504,
        "clow" : 425,
        "air" : "Hazardous"
        },
    "lev7" : {
        "ihigh" : 500,
        "ilow" : 401,
        "chigh" : 604,
        "clow" : 505,
        "air" : "Hazardous"
        },
    "lev8" : {
        "ihigh" : 1000,
        "ilow" : 501,
        "chigh" : 1001,
        "clow" : 605,
        "air" : "Hazardous and very difficult for indoor air purifiers and Delhirium"
        }
    }
