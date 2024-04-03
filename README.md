# Wordlist Project

## Prerequisites

Make sure you have **Docker** installed and running on your system.

## How to Run

1. Open the terminal and navigate to the `wordlist` directory.
2. Build the Docker image using the following command:
`docker build -t {image_name} .`

3. Run the Docker container with the specified input file name parameter:

`docker run -e FILE_NAME={input file name parameter} -p 8000:8000 {image_name}`

4. to test it, open another terminal and run `curl http://localhost:8000/permutations?word={choose_example_for_a_word}

**NOTE**: If you do not provide `FILE_NAME`, the default value will be "small_word_list.txt".
