#include <atomic>
#include <cassert>
#include <string>
#include <thread>

std::atomic<std::string *> ptr;
int data;

void producer() {
  std::string *p = new std::string("Hello");
  data = 42;
  // ptr.store(p, std::memory_order_release);
  ptr.store(p);
}

void consumer() {
  std::string *p2;
  // while (!(p2 = ptr.load(std::memory_order_acquire)))
  while (!(p2 = ptr.load()))
    ;
  assert(*p2 == "Hello"); // never fires
  assert(data == 42);     // never fires
}

int main() {
  std::thread t1(producer);
  std::thread t2(consumer);
  t1.join();
  t2.join();
}
