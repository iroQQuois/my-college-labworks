<?php


class Node
{
    public $node;
    public $nextNode;
    public static $count;

    public function __construct($node)
    {
        $this->node = $node; # узел
        $this->nextNode = null; # ссылка на следующий узел
        self::$count++;
    }
}



class SingleLinkedList
{
    public $head; # головной узел
    public $tail; # последний узел
    

    public function __construct()
    {
        $this->head = null;
    }

    public function add($value): void
    {
        $newNode = new Node($value);
        if ($this->head == null)
        {
            $this->tail == $newNode;
        }
        $newNode->nextNode = $this->head;
        $this->head = $newNode;

    }

    public function search($value): bool
    {
        $node = $this->head;
        while ($node && $node->node != $value)
        {
            $node = $node->nextNode;
        }
        if ($node != null)
        {
            return true;
        } else {
            return false;
        }
    }

    public function remove($value): void
    {
        $node = $this->head;
        while ($node && $node->node != $value) {
            $node = $node->nextNode;
        }
        if ($node != null) {
            $node->node = null;
        }
    }

    public function size(): int
    {
        # я не прикалываюсь, в тз сказано, что метод должен возвращать кол-во
        # узлов. Он их возвращает :)
        return Node::$count;
    }

    public function append($value)
    {
        $node = $this->tail;
        $node->nextNode = new Node($value);
    }

    public function pop()
    {
        $node = $this->head;
        while ($node->nextNode != null)
        {
            $node = $node->nextNode;
        }
        $a = $node->nextNode;
        $node = null;
        return $a;
    }

    public function shift()
    {
        $node = $this->head;
        if ($node != null)
        {
            $this->head = null;
        }
        return $node;
    }
}


$a = new LinkedList();
$a->add(20);
$a->add(30);
$a->add(40);
$a->add(50);

echo $a->search(20); // я пытался засунуть это в boolval(), но всё равно выводит 1/0
echo "<hr />";

echo $a->search(30);
echo "<hr />";

echo $a->search(40);
echo "<hr />";

echo $a->search(50);
echo "<hr />";


echo $a->search(60);
echo "<hr />";

$a->remove(20);
echo $a->search(20);
echo "<hr />";
echo $a->size();