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
        while ($this->head == null)
        {
            $this->head = $newNode;
            break;
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
        if ($node->node == $value)
        {
            $this->head = $node->nextNode;
        }
        while ($node && $node->nextNode->node != $value) {
            $node = $node->nextNode;
        }
        if ($node != null) {
            $node->nextNode = $node->nextNode->nextNode;
        }
    }

    public function size(): int
    {
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

echo $a->search(20);
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