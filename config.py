import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQGu5nsAK5LhZJdHHe0pWFsAvonXBhf09dcMw1leXG7wwKA0t7MjM5CR8G9inQMe4hmN2MVCSX3t5JVsiXnMaG-6-g-5AECBpbbitQVPfMcwy80dPRFlAKCjPp-FDxjMt7efrwLm8qYfLY-htk7Cw4yAxXm8bTrUKtT0JkG8AxkxjlJp_jJCtziu4ecMEIvXyhEg4HslZ7ouSECzAtQVUlbIes3YLI4gVKs8nnlqI0JNXVc3wkBLEQHFgfzNYkFFuN7H2LYFE1bHXT8mXUa_5h5BhTOwTn3Bg12OnTFcjDIy8oxerpS3vXLc3Hz120lN8DvjTt6s0YwDqezkDI5R9cPDWMa1-gAAAAGX0Kj6AA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
