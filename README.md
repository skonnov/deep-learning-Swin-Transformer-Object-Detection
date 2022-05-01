# Deep learning course - SWIN-Transformer Object Detection
## requirements:
* OS: Ubuntu 20.04 or WSL2
* Docker

## step 0:
```sh
git clone https://github.com/skonnov/deep-learning-Swin-Transformer-Object-Detection.git
```

## step 1:
if git-lfs is not installed:
```sh
sudo apt install git-lfs
```

## step 2:
in deep-learning-Swin-Transformer-Object-Detection directory:
```sh
git lfs pull
```


## step 3:
To build image
```sh
docker build -t deep-learning:1.0 .
```

To run image

```sh
docker run -v $PWD/workdir:/workdir deep-learning:1.0
```