class Node:
    """Klasa wezel - do pamietania pojedynczej danej."""
    def __init__(self, dane=None, next_node=None):
    # konstruktor - domyslnie oba pola maja specjalna wartosc None
    # next_node bedzie wskazywalo na kolejny wezel takiej samej postaci lub na None
        self.dane = dane
        self.next_node  = next_node
    def __str__(self):
        return str(self.dane)

class Queue:
    # Implementacja kolejki FIFO za pomoca listy dowiazanej. Zobacz do podrecznika Cormen et al.
    def __init__(self):
    # konstruktor - domyslnie zmienne _head (glowa) oraz _tail (ogon) maja specjalna wartosc None
    # rozmiar moze byc przydatny do obslugi bledow oraz sprawdzenia czy kolejka nie jest pusta
        self.size = 0
        self._head = None
        self._tail = None

    def isEmpty(self):
      return self.size == 0
    # sprawdzenie czy kolejka FIFO jest pusta


    def enqueue(self, dane):
      nowy = Node(dane)
      if self.isEmpty():
        self._head = nowy
        stary = self._tail
        self._tail = nowy
      else:
        self._tail.next_node = nowy
        self._tail = nowy
      self.size += 1
        # wstawianie do kolejki FIFO - brak obslugi bledow (nadmiar)
        # zapamietujemy poprzdni ogon
        # ogonem staje sie nowo wstawiany wezel
        # sa dwie mozliwosci

            # Jesli lista nie jest pusta, nowy wezel ktory jest teraz ogonem podwiazujemy pod poprzedni ogon

        # zwiekszamy liczbe danych w kolejce FIFO


    def dequeue(self):        # usuwanie z kolejki FIFO
      if self.isEmpty():
        raise Exception("Kolejka jest pusta")
      else:
        self._head = self._head.next_node # glowa staje sie nastepnik glowy
        self.size -= 1  # zmniejszamy liczbe danych w kolejce FIFO
        # to ponizej napawde nie jest potrzebne, ale jest to dodane dla celow dydaktycznych i przejrzystosci kodu

    def first(self):
    # zwracanie elementu z kolejki FIFO
      if self.isEmpty():
        raise ValueError("Kolejka FIFO jest pusta!")
      return self._head.dane
  

q1 = Queue()
q1.enqueue(7)
q1.enqueue(3)
q1.enqueue(4)

q1.first()
q1.dequeue()
q1.first()
