## Playwright UI testing demo

Prerequisites:
- Python 3.12
- Google Chrome
- Docker

### Steps to run the test:

There are two ways to run the test: locally and with docker.

#### Local Run Instructions

* Setup local environment:

```
./test.sh setup-local-env
```

* Run test with following command:

```
./test.sh test-local -m basic_search
```

#### Docker Run Instructions

* Build image:

```
./test.sh build-image
```

* Run test with:

```
./test.sh test-docker -m basic_search
```