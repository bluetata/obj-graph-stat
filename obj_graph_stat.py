import os
import objgraph

def obj_graph_stat(mark=''):
    file_path = r'D:\obj_graph.txt'
    if not os.path.exists(file_path):
        file = open(file_path, 'w')
        file.close()
    file = open(file_path, 'a')
    file.write(f'******************{str(now_datetime())}-{mark}******************\n')
    objgraph.show_most_common_types(limit=20, file=file)
    file.write(f'-'*20)
    file.write('\n')
    # 返回heap内存详情
    # heap = hp.heap()
    # byvia返回该对象的被哪些引用， heap[0]是内存消耗最大的对象
    # references = heap[0].byvia
    # file.write(str(references))
    file.write('\n\n')
    file.close()