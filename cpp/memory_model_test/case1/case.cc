#include <iostream>
#include <thread>
#include <cassert>

class Data {
public:
  bool status = false;
  // prevent modified data are in the same cache line
  int8_t data[203] = {0};
  int64_t data1 = 0;
  bool data2 = false;
};
void pro(Data *d) {
    d->data1 = 111;
    d->data2 = true;
    d->data[202] = 22;
    // may be reordered in weak memory arch
    d->status = true;
}

void con(Data *d) {
  if (d->status) {
    assert(d->data1 == 111);
    assert(d->data2 == true);
    assert(d->data[202] == 22);
  }
}
int main() {
  while (true) {
    Data d;
    std::thread p1(pro, &d);
    std::thread c1(con, &d);
    c1.join();
    p1.join();
  }
  std::cout << "done!\n";
}

/*
case: case.cc:20: void con(Data*): Assertion `d->data1 == 111' failed.
Aborted 
*/

/*
Architecture:          aarch64
Byte Order:            Little Endian
CPU(s):                128
On-line CPU(s) list:   0-127
Thread(s) per core:    1
Core(s) per socket:    64
Socket(s):             2
NUMA node(s):          4
Model:                 0
CPU max MHz:           2600.0000
CPU min MHz:           200.0000
BogoMIPS:              200.00
L1d cache:             64K
L1i cache:             64K
L2 cache:              512K
L3 cache:              65536K
NUMA node0 CPU(s):     0-31
NUMA node1 CPU(s):     32-63
NUMA node2 CPU(s):     64-95
NUMA node3 CPU(s):     96-127
Flags:                 fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm
*/
