# Problem: You want to read or write data encoded as JSON (JavaScript Object Notation)

# Solution: The json module provides an easy way to encode and decode data in JSON. The two main functions are json.dumps() and json.loads(), mirroring the interface used in other serialization libraries, such as pickle.

import json

data =  {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23,
        'other': ["Entry 1", 82, "Entry 3"]
        }

json_str = json.dumps(data)
print(json_str)

