"""
Diagram:

+--------------------+
|  EmojiImageFactory |
|--------------------|
| - _images: dict   |  # Stores unique images
|--------------------|
| + get_image(file_name) |
+--------------------+
         |
         |  (Ensures only one instance per image)
         v
+-----------------+
|  EmojiImage     |
|-----------------|
| - file_name: str |
|-----------------|
| + display()     |
+-----------------+

+-------------------------------------+
|  Emoji                              |
|-------------------------------------|
| - name: str                         |
| - size: int                         |
| - image: EmojiImage                 |
| - symbol: str                        |
|-------------------------------------|
| + display()                          |
+-------------------------------------+

Example Usage:
--------------------------------------------------
emoji1 = Emoji("Crazy Face", 32, "crazy
"""