# COVID vaccines availability in INDIA
This project contains simple script to find COVID vaccine availability in India. 
It can be automated to send notifications. I am using MS teams notifications.

## Pre-requisites

* python >3+
* pymsteams ( only if MS teams notifications are used)


## Usage

1.  Get state_id for your state 

```
{
  "states": [
    {
      "state_id": 1,
      "state_name": "Andaman and Nicobar Islands"
    },
    {
      "state_id": 2,
      "state_name": "Andhra Pradesh"
    },
    {
      "state_id": 3,
      "state_name": "Arunachal Pradesh"
    },
    {
      "state_id": 4,
      "state_name": "Assam"
    },
    {
      "state_id": 5,
      "state_name": "Bihar"
    },
    {
      "state_id": 6,
      "state_name": "Chandigarh"
    },
    {
      "state_id": 7,
      "state_name": "Chhattisgarh"
    },
    {
      "state_id": 8,
      "state_name": "Dadra and Nagar Haveli"
    },
    {
      "state_id": 37,
      "state_name": "Daman and Diu"
    },
    {
      "state_id": 9,
      "state_name": "Delhi"
    },
    {
      "state_id": 10,
      "state_name": "Goa"
    },
    {
      "state_id": 11,
      "state_name": "Gujarat"
    },
    {
      "state_id": 12,
      "state_name": "Haryana"
    },
    {
      "state_id": 13,
      "state_name": "Himachal Pradesh"
    },
    {
      "state_id": 14,
      "state_name": "Jammu and Kashmir"
    },
    {
      "state_id": 15,
      "state_name": "Jharkhand"
    },
    {
      "state_id": 16,
      "state_name": "Karnataka"
    },
    {
      "state_id": 17,
      "state_name": "Kerala"
    },
    {
      "state_id": 18,
      "state_name": "Ladakh"
    },
    {
      "state_id": 19,
      "state_name": "Lakshadweep"
    },
    {
      "state_id": 20,
      "state_name": "Madhya Pradesh"
    },
    {
      "state_id": 21,
      "state_name": "Maharashtra"
    },
    {
      "state_id": 22,
      "state_name": "Manipur"
    },
    {
      "state_id": 23,
      "state_name": "Meghalaya"
    },
    {
      "state_id": 24,
      "state_name": "Mizoram"
    },
    {
      "state_id": 25,
      "state_name": "Nagaland"
    },
    {
      "state_id": 26,
      "state_name": "Odisha"
    },
    {
      "state_id": 27,
      "state_name": "Puducherry"
    },
    {
      "state_id": 28,
      "state_name": "Punjab"
    },
    {
      "state_id": 29,
      "state_name": "Rajasthan"
    },
    {
      "state_id": 30,
      "state_name": "Sikkim"
    },
    {
      "state_id": 31,
      "state_name": "Tamil Nadu"
    },
    {
      "state_id": 32,
      "state_name": "Telangana"
    },
    {
      "state_id": 33,
      "state_name": "Tripura"
    },
    {
      "state_id": 34,
      "state_name": "Uttar Pradesh"
    },
    {
      "state_id": 35,
      "state_name": "Uttarakhand"
    },
    {
      "state_id": 36,
      "state_name": "West Bengal"
    }
  ],
}
```

2. Get district_id from state_id 
> Copy this URL and update state_id (use state_id from step 1) 
> https://cdn-api.co-vin.in/api/v2/admin/location/districts/{state_id}
> Paste on browser and hit enter.  

3. Get district_id from response from above.
```
{
  "districts": [
    {
      "district_id": 3,
      "district_name": "Nicobar"
    },
    {
      "district_id": 1,
      "district_name": "North and Middle Andaman"
    },
    {
      "district_id": 2,
      "district_name": "South Andaman"
    }
  ],
  "ttl": 24
}
```
5. Update district_ids in script line #10
6. Execute>> python call_cowin.py
