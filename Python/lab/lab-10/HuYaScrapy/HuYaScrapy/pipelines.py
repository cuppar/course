import os


class HuYaPipeline(object):
    file_name = r'/home/cuppar/projects/course/Python/lab/lab-10/lol.csv'

    def process_item(self, item, spider):
        item = dict(item)
        if not os.path.exists(HuYaPipeline.file_name):  # 文件不存在先创建，然后输入表头
            with open(HuYaPipeline.file_name, "x") as f:
                f.write('title,')
                f.write('name,')
                f.write('number')
                f.write('\n')  # ‘\n’ 表示换行
                f.close()
        with open(HuYaPipeline.file_name, "a+") as f:
            f.write(item['title'] + ',')
            f.write(item['name'] + ',')
            f.write(str(item['number']))
            f.write('\n')  # ‘\n’ 表示换行
            f.close()
