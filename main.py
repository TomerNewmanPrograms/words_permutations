import sys
import uvicorn
import logging
from fastapi import FastAPI

app = FastAPI()
logger = logging.getLogger(__name__)

words_permutations = {}


@app.on_event("startup")
async def extract_words():
    try:
        with open(sys.argv[1], "r") as f:
            for line in f:
                for word in line.split():
                    word = word.rstrip('\n')
                    sorted_word = "".join(sorted(word))
                    if sorted_word not in words_permutations:
                        words_permutations[sorted_word] = {word}
                    else:
                        words_permutations[sorted_word].add(word)
            logger.info("dict of words permutations: %s", words_permutations)

    except IndexError as e:
        logger.error("file was not provided, %s", e)
        exit(1)


@app.get("/")
def hello_world():
    return "app is working"


@app.get("/permutations")
async def word_list(word: str):
    sorted_word = "".join(sorted(word))
    if sorted_word in words_permutations:
        return words_permutations[sorted_word]
    else:
        return {}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
