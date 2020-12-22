import argparse
import cProfile, pstats, sys
import logging

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)

def findAllPaths(target, deadends):
    start = ''.join(['0' for x in target])
    nodes = [start] # initial
    targetNodes = [target]
    pastNodes = set()
    targetPastNodes = set()
    steps = 0

    nodes = filterNodes(nodes, deadends)
    targetNodes = filterNodes(targetNodes, deadends)

    while len(nodes) > 0 and len(pastNodes)<10000 and len(targetNodes) >0 and len(targetPastNodes)<10000:
        if matchedNodeFound(nodes, targetNodes):
            return steps
        
        nodes, pastNodes = moveOneStep(nodes, pastNodes, deadends)
        steps += 1

        if matchedNodeFound(nodes, targetNodes):
            return steps

        targetNodes, targetPastNodes = moveOneStep(targetNodes, targetPastNodes, deadends)
        steps += 1

    return -1

def matchedNodeFound(nodes1, nodes2):
    intersection = [x for x in nodes1 if x in nodes2]
    return len(intersection) > 0

def moveOneStep(nodes, pastNodes, deadends):
    for i in range(0, len(nodes)):
        node = nodes.pop(0)
        pastNodes.add(node)
        nextNodes = oneMove(node)
        # filter the nodes in deadends
        nextNodes = filterNodes(nextNodes, deadends)
        # filter the nodes already passed: 0000 -> 0001, next step shall not go back to 0000
        nextNodes = filterNodes(nextNodes, pastNodes)
        nodes.extend(nextNodes)
        # logging.debug("currentNode: %s, \nnextNodes: %s", node, nextNodes)
    return nodes, pastNodes

def filterNodes(nodes, deadends):
    return [x for x in nodes if x not in deadends]

def oneMove(start):
    result = []
    for i in range(0, len(start)): 
        result.append(forward(start, i))
        result.append(backward(start, i))
    return result

def forward(start, index): 
    next = (int(start[index]) + 1) % 10
    return start[:index] + str(next) + start[index+1:]

def backward(start, index): 
    next = int(start[index]) - 1
    if next < 0:
        next += 10
    return start[:index] + str(next) + start[index+1:]                


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # arguments ref: https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
    parser.add_argument("--deadends", help="deadends like 0101,0102", nargs='?', type=str, const="1207,9207,0107,0307,0217,0297,0206,0208", default="1207,9207,0107,0307,0217,0297,0208")
    parser.add_argument("--target", help="the target to search", nargs='?', type=str, const="0207", default="0207")
    args = parser.parse_args()
    deadends = [i for i in args.deadends.split(',')] 
    target = args.target

    deadends = ["7867","6676","8687","7886","6768","8877","6767","6676","6666","7876","6688","6677","6877","7786","6778","6868","6868","7867","7668","7666","8868","7887","6788","7687","7788","7877","6867","6867","7876","8787","8878","6668","6878","6766","8667","8688","6788","7687","8887","8766","6867","8867","7866","7866","6686","7776","8687","7888","6777","6678","6678","6686","6677","7886","6876","8666","6667","7768","7688","7668","6786","7766","7867","8866","7887","6676","8776","6867","8888","6678","8687","6868","7888","8666","6678","6668","7678","7667","8786","8768","6766","8776","8677","7788","7868","7878","6786","6678","6876","7667","8866","8666","8768","8886","8787","8688","8766","8867","7886","6876","7776","7867","8668","7777","8888","7767","8778","8888","6876","8777","7877","8866","8668","8878","7678","8787","7788","8887","8667","7887","6686","8778","7768","8787","7677","6768","7877","7788","7768","6768","6786","7887","7768","6676","6777","8686","7867","8788","8887","8776","7677","8786","8678","7666","8776","7676","6767","8776","8888","8766","8876","7777","7677","6767","7878","7868","8677","7677","8788","6667","8866","8887","6686","6777","6676","8787","6788","8866","6767","8676","8868","8768","8888","7866","7877","7768","7686","7888","6666","6887","6787","7667","6676","8666","8886","8878","8678","8868","8888","8867","7878","7787","8776","7877","6788","8778","6768","8677","8678","6778","7888","6866","6768","6666","6887","8866","7676","7866","7876","7678","7686","8887","7676","6788","8787","6666","8866","6876","8676","8688","8887","7887","7777","8887","8688","6668","6686","6887","7677","6867","6786","6877","7788","6667","8778","8786","8767","7778","8867","8877","6668","8886","7888","7767","7666","8678","8668","8767","7666","6787","6886","8787","6886","8768","8767","8676","6767","8776","8768","8687","8778","7888","6768","7878","6668","7688","6687","7866","8878","6877","7667","8886","7876","6667","8877","7666","7668","7676","6888","6686","7666","7688","7666","6678","6676","7678","8788","7667","7767","8766","6867","8767","8676","8786","8667","6678","6778","8877","8788","6866","7687","6876","8878","8866","6788","6877","8768","8778","8778","8866","7866","7887","7878","8766","8778","7868","8787","6676","8668","7866","8787","8767","6876","8867","6688","6886","6668","6878","7866","8678","8867","7667","7878","8778","8777","7866","8878","7868","6876","7688","7677","7678","7777","8888","8776","8688","6878","8877","7678","7777","7878","6678","6688","6868","8876","6668","8877","8786","6688","8766","8887","6678","8886","8876","8888","8878","6786","7686","7867","7767","7888","8866","6876","7767","6687","6687","6688","6868","8668","6886","8686","7766","8777","8667","8886","7676","7768","6788","8688","7676","7686","8777","7886","7788","6666","7687","6676","6777","6866","6767","7787","7877","6777","6886","7877","7787","7787","8768","7787","8778","6766","7677","6788","6786","6767","8687","6687","8668","6876","6666","7676","8667","6688","6766","6677","7667","8668","8866","7686","8866","8687","8866","8768","7886","6877","8877","6676","6887","6788","8877","8887","8886","8887","6676","8867","6867","7768","8868","6668","7878","7887","8768","6876","7787","7876","8886","6778","7778","7687","6686","7787","8767","8668","7686","7678","8788","6687","8666","7877","6668","7686","6866","6888","8786","7778","7786","8787","6777","6867","7787","7777","6766","8666","6778","6867","8668","8667","7678","8668","7677","8787","6876","6668","7788","7688","7687","8778","8787","8688","8867"]
    target = "6776"

    print(deadends)
    print(target)

    prof = cProfile.Profile()
    prof.enable()
    # # steps = prof.runcall(findAllPaths, target, deadends)
    # steps = cProfile.run("findAllPaths(target, deadends)")

    steps = findAllPaths(target, deadends)
    
    prof.disable()
    ps = pstats.Stats(prof, stream=sys.stdout)
    ps.print_stats()
    
    print(steps)