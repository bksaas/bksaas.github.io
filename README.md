## Setup

1. Install and Pull

```shell

npm install hexo-cli -g
# git clone -b hexo https://github.com/bksaas/bksaas.github.io.git
# git submodule init && git submodule update
git clone --recursive -b hexo https://github.com/bksaas/bksaas.github.io.git
cd bksaas.github.io
npm install

```

2. Run dev

```shell
hexo server -p 4000
```

3. Bulid and Deploy

```shell
hexo clean && hexo generate
hexo deploy
```

or

```shell
hexo clean && hexo g && hexo d
```

4. New Post

```shell
hexo new abc
vim sources/_post/abc.md
```

5. Image to Markdown

  - linux
    xclip + snapshot + qcloud_cos
  - mac
    ipic
  - windows
    shareX + upyun
