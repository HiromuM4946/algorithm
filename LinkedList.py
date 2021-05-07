from __future__ import annotations
from typing import Any

# dataとnext (ノード) を管理
class Node(object):
    def __init__(self, data: Any, next_node: Node = None):
        self.data = data
        self.next = next_node

# 全体を管理
class LinkedList(object):
    # headを作成
    def __init__(self, head=None) -> None:
        self.head = None

    # データを追加する関数
    def append(self, data: Any) -> None:
        # dataとnextが入ったノードのオブジェクトを作る
        new_node = Node(data)
        # headの中身がNoneの時は、headにそのノードをappendする
        if self.head is None:
            self.head = new_node
            return 
        
        # headの中身がある場合
        # 最後のノードを追いかけ、その次にnew_nodeをappendする
        # head→node→・・・→last_node
        last_node = self.head
        # last_nodeの次のノードがNoneになるまで回す
        while last_node.next:
            last_node = last_node.next
        # last_nodeの次がNoneなので、そこにnew_nodeを入れてあげればデータを追加できる
        last_node.next = new_node


    # 先頭にデータを挿入する
    def insert(self, data: Any) -> Node:
        # dataとnextが入ったノードのオブジェクトを作る
        new_node = Node(data)
        # headはnew_nodeの次とする
        new_node.next = self.head
        # 先頭にnew_nodeをinsertする
        self.head = new_node

    # データの削除
    def remove(self, data: Any) -> None:
        # 削除したデータが先頭の場合
        # current_nodeにheadを入れる
        current_node = self.head
        # current_nodeが存在し、かつcurrent_nodeのデータがremoveしたいデータと一致した場合
        if current_node and current_node.data == data:
            # headにcurrent_nodeのnextを入れる
            self.head = current_node.next
            # current_nodeを削除
            current_node = None
            return
        
        # 削除したいデータが先頭ではない場合
        # current_nodeの一個前
        previous_node = None
        # current_nodeが存在し、current_nodeのデータが削除したデータではない場合
        while current_node and current_node.data != data:
            # current_node.nextにデータをリンクさせるために、current_nodeにデータを保存
            previous_node = current_node
            # whileループで削除したいデータに一致するノードを探す
            current_node = current_node.next
        
        if current_node is None:
            return

        # current_node.nextにprevious_node.nextをリンク
        previous_node.next = current_node.next
        # current_nodeを削除
        current_node = None

    # 逆順にする(iterative)
    def reverse_iterative(self) -> None:
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
        
            previous_node = current_node
            current_node = next_node

        self.head = previous_node
    
    # 逆順にする(recursive)
    def reverse_recursive(self) -> None:
        def _reverse_recursive(current_node: Node, previous_node: Node):
            if not current_node:
                return previous_node
            
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            return _reverse_recursive(current_node, previous_node)
        
        self.head = _reverse_recursive(self.head, None)
    
    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next



if __name__ == '__main__':
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.insert(0)
    # print(l.head.data)
    # print(l.head.next.data)
    # print(l.head.next.next.data)
    # print(l.head.next.next.next.data)
    l.print()

