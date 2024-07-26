#include <atomic>
#include <cassert>
#include <iostream>
#include <thread>
#include <vector>

constexpr int N = 100000;
constexpr int T = 50;
std::atomic<int> cnt = {0};

void f() {
  for (int n = 0; n < N; ++n) {
    // use counter.fetch_add(1, std::memory_order_relaxed) get high performance
    // in weak memory platform. default memory order is
    // std::memory_order_seq_cst
    cnt++;
    cnt.fetch_add(1,std::memory_order_relaxed);
  }
}

int main() {
  while(true){
    std::vector<std::thread> v;
    for (int n = 0; n < T; ++n) {
      v.emplace_back(f);
    }
    for (auto &t : v) {
      t.join();
    }
    assert(cnt.load() == 2 * N * T);
    std::cout << "Final cnt value is " << cnt << '\n';
  }
}
