## Prettify JSON

+ The script read the json-file and displays the data in a convenient way
---
### Quickstart

+ Script takes the path to the file as a parameter
+ Script checks the path, if there is no file - prints an error
+ Script prints an error if the file is empty or not json
---


+ Example of script launch on Linux, Python 3.5:

```bash
$ python pprint_json.py <path to file>

```
+ Example output information from a file

'''
      "properties": {
        "Attributes": {
          "Address": "улица Академика Королёва, дом 3",
          "AdmArea": "Северо-Восточный административный округ",
          "ClarificationOfWorkingHours": null,
          "District": "Останкинский район",
          "IsNetObject": "да",
          "Name": "Магазин «Отдохни»",
          "OperatingCompany": "Отдохни",
          "PublicPhone": [
            {
              "PublicPhone": "(495) 424-95-15"
            }
          ],
          "TypeService": "реализация продовольственных товаров",
          "WorkingHours": [
            {
              "DayOfWeek": "понедельник",
              "Hours": "09:00-23:00"
            },
            {
              "DayOfWeek": "вторник",
              "Hours": "09:00-23:00"
            },
          ],
          "global_id": 171714826
        },
        "DatasetId": 1854,
        "ReleaseNumber": 2,
        "RowId": "a5d9874a-600e-400d-8512-a8215599ecaa",
        "VersionNumber": 1
      },
      "type": "Feature"
    },
    {
      "geometry": {
        "coordinates": [
          37.72775243734561,
          55.61668660260342
        ],
        "type": "Point"
      },

'''

---
### Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
