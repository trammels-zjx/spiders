def image(url):
    response = requests.get(url)
    # 获取图片的二进制文本
    img = response.content
    # 文件存储地址

    name = url.split('/')[-1]
    name = 'img/' + name
    # 将图片保存在本地img文件夹下
    with open(name, 'wb') as f:
        f.write(img)