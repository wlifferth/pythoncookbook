# Problem: You want to feed a text or binary string to code that's been written to operate on file-like objects instead

# Solution: Use theh io.StringIO() and io.BytesIO() classes to create file-like objects that operate on string data.

import io
s = io.StringIO()
s.write("Hello World\n")
print("This is a test", file=s)
print(s.getvalue())

s = io.BytesIO()
s.write(b'binary data')
print(s.getvalue())
