# world = [] # 게임 월드의 정의

objects = [[], []]

collision_group = dict()


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
            remove_collision_object(o)
            del o
            return
    raise ValueError('Trying destroy non existing object')


def all_objects():
    for layer in objects:
        for o in layer:
            yield o

def clear():
    for o in all_objects():
        # remove_collision_object(o)
        del o
    for layer in objects:
        layer.clear()

def add_collision_pairs(a, b, group):

    if group not in collision_group:
        print('Add new group')
        collision_group[group] = [[], []] #list of list : list pair

    if a:
        if type(a) == list:
            collision_group[group][0] += a
        else:
            collision_group[group][0].append(a)

    if b:
        if type(b) == list:
            collision_group[group][1] += b
        else:
            collision_group[group][1].append(b)

def all_collision_pairs():
    for group, pairs in collision_group.items():
        for a in pairs[0]:
            for b in pairs[1]:
                yield a, b, group

def remove_collision_object(o):
    for pairs in collision_group.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        elif o in pairs[1]:
            pairs[1].remove(o)