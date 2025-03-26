class EmojiImage:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def display(self):
        return f"{self.file_name}"

class EmojiImageFactory:
    _images = {}

    @classmethod
    def get_image(cls, file_name: str):
        if file_name not in cls._images:
            cls._images[file_name] = EmojiImage(file_name)
        return cls._images[file_name]


class Emoji:
    def __init__(self, name: str, size: int, file_name: str, symbol: str):
        self.name = name
        self.size = size
        self.image = EmojiImageFactory.get_image(file_name)
        self.symbol = symbol

    def display(self):
        return f"Emoji: {self.name} ({self.symbol}), Size: {self.size}, Image: {self.image.display()}"


emoji1 = Emoji("Crazy Face", 32, "crazy_face.png", "🤪")
emoji2 = Emoji("Crazy Face", 64, "crazy_face.png", "🤪")
emoji3 = Emoji("Rolling on the Floor Laughing", 32, "rofl.png", "🤣")
emoji4 = Emoji("Rolling on the Floor Laughing", 64, "rofl.png", "🤣")
emoji5 = Emoji("Face with Tongue", 32, "tongue_out.png", "😜")
emoji6 = Emoji("Face with Tongue", 64, "tongue_out.png", "😜")


print(emoji1.display())
print(emoji2.display())
print(emoji3.display())
print(emoji4.display())
print(emoji5.display())
print(emoji6.display())

# Verify that only 3 unique images exist
print("Unique images in factory:", len(EmojiImageFactory._images))