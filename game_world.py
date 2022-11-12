world = [] # 게임 월드의 정의

objects = [[], []]

def add_object(o, depth):
    # world.append(o)
    objects[depth].append(o)

def add_objects(ol, depth):
    objects[depth] += ol

def remove_object(o):
    # world.remove(o) # 리스트로부터 삭제
    # del o  # 실제로 메모리 삭제

    for layer in objects:
        if o in layer:
            layer.remove(o)
            del o
            return
    raise ValueError('Trying destroy non existing object')


def all_objects():
    for layer in objects:
        for o in layer:
            yield o

def clear():
    for o in all_objects():
        del o
    for layer in objects():
        layer.clear