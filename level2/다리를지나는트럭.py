from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    Q = deque(truck_weights)
    truck_arrived = 0 # 도착한 트럭 수
    above_bridge = deque()
    total_weight = 0
    while truck_arrived < len(truck_weights):
        if Q:
            truck = Q.popleft()
            # 만약 다리 위에 아무도 없으면 바로 추가
            if not above_bridge:
                above_bridge.append([truck, bridge_length-1])
                total_weight += truck
                answer += 1
            elif not above_bridge[0][1]:
                arrive = above_bridge.popleft()
                total_weight -= arrive[0]
                truck_arrived += 1
                Q.appendleft(truck)
            elif total_weight + truck <= weight: # 다리 위에 뭐가 있는데, 무게가 적당하면 이동 후 추가
                for move in above_bridge:
                    move[1] -= 1
                above_bridge.append([truck, bridge_length-1])
                total_weight += truck
                answer += 1
            else: # 대기 트럭은 있지만 무거워서 다리에 진입 못하고 전진만 하는 경우
                for move in above_bridge:
                    move[1] -= 1
                Q.appendleft(truck)
                answer += 1
        elif not Q and not above_bridge[0][1]:
            arrive = above_bridge.popleft()
            total_weight -= arrive[0]
            truck_arrived += 1
        else:
            for move in above_bridge:
                move[1] -= 1
            answer += 1
    answer += 1
    return answer