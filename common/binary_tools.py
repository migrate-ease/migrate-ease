"""
Copyright 2020-2023 Alibaba Inc.
Copyright 2017 Arm Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
import struct
from typing import Tuple


def is_binary(filename):
    if not os.path.isfile(filename):
        return False

    with open(filename, 'rb') as f:
        if b'\x00' in f.read():
            return True
        else:
            return False


def get_elf_dict(temp: Tuple[str]):
    elf_header = {}
    elf_header['e_type'] = temp[0]
    elf_header['e_machine'] = temp[1]
    elf_header['e_version'] = temp[2]
    elf_header['e_entry'] = temp[3]
    elf_header['e_phoff'] = temp[4]
    elf_header['e_shoff'] = temp[5]
    elf_header['e_flags'] = temp[6]
    elf_header['e_ehsize'] = temp[7]
    elf_header['e_phentsize'] = temp[8]
    elf_header['e_phnum'] = temp[9]
    elf_header['e_shentsize'] = temp[10]
    elf_header['e_shnum'] = temp[11]
    elf_header['e_shstrndx'] = temp[12]
    return elf_header


def get_elf_machine_code(filename) -> {None, str}:
    if not os.path.isfile(filename):
        return

    if not is_binary(filename):
        return

    with open(filename, 'rb') as f:
        """
        #define EI_NIDENT 16

        typedef struct {
            unsigned char   e_ident[EI_NIDENT];
            Elf32_Half      e_type;
            Elf32_Half      e_machine;
            Elf32_Word      e_version;
            Elf32_Addr      e_entry;
            Elf32_Off       e_phoff;
            Elf32_Off       e_shoff;
            Elf32_Word      e_flags;
            Elf32_Half      e_ehsize;
            Elf32_Half      e_phentsize;
            Elf32_Half      e_phnum;
            Elf32_Half      e_shentsize;
            Elf32_Half      e_shnum;
            Elf32_Half      e_shstrndx;
        } Elf32_Ehdr;

        e_ident
            The initial bytes mark the file as an object file and provide machine-independent 
            data with which to decode and interpret the file's contents. Complete descriptions 
            appear below in ``ELF Identification''.
        e_type
            This member identifies the object file type.
        """
        _e_ident = f.read(16)

        temp = f.read(struct.calcsize('2HI3QI6H'))
        temp = struct.unpack('2HI3QI6H', temp)

        elf_header = get_elf_dict(temp)

        return elf_header['e_machine']


def get_a_elf_machine(filename):
    if not os.path.isfile(filename):
        return

    f_size = os.path.getsize(filename)

    file_dict = {}
    with open(filename, 'rb') as f:
        for i in range(f_size):
            file_dict[i] = f.read(1)

    length_window = 4
    elf_magic_length = 16
    static_lib_machine_code_map = {}
    map_id = 0

    for i in range(f_size - length_window):

        elf_figure = b''

        for j in range(length_window):
            elf_figure = elf_figure + file_dict[i + j]

        if elf_figure == b'\x7fELF':
            size_elf = struct.calcsize('2HI3QI6H')

            temp = b''
            for j in range(size_elf):
                temp = temp + file_dict[i + j + elf_magic_length]

            temp = struct.unpack('2HI3QI6H', temp)
            elfhdr = get_elf_dict(temp)

            static_lib_machine_code_map[map_id] = elfhdr['e_machine']
            map_id = map_id + 1

    return static_lib_machine_code_map


def get_file_arch(machine_code):
    arch_map = {}

    # ELF head machine type, https://github.com/torvalds/linux/blob/master/include/uapi/linux/elf-em.h
    arch_map[0] = 'EM_NONE'
    arch_map[1] = 'EM_M32'
    arch_map[2] = 'EM_SPARC'
    arch_map[3] = 'EM_386'
    arch_map[4] = 'EM_68K'
    arch_map[5] = 'EM_88K'
    arch_map[6] = 'EM_486'  # Perhaps disused
    arch_map[7] = 'EM_860'
    arch_map[8] = 'EM_MIPS'  # MIPS R3000 (officially, big-endian only)
    # Next two are historical and binaries and modules of these types will be rejected by Linux.
    arch_map[10] = 'EM_MIPS_RS3_LE or EM_MIPS_RS4_BE'  # MIPS R3000 little-endian or MIPS R4000 big-endian
    arch_map[15] = 'EM_PARISC'  # HPPA
    arch_map[18] = 'EM_SPARC32PLUS'  # Sun's "v8plus"
    arch_map[20] = 'EM_PPC'  # PowerPC
    arch_map[21] = 'EM_PPC64'  # PowerPC64
    arch_map[23] = 'EM_SPU'  # Cell BE SPU
    arch_map[40] = 'EM_ARM'  # ARM 32 bit
    arch_map[42] = 'EM_SH'  # SuperH
    arch_map[43] = 'EM_SPARCV9'  # SPARC v9 64-bit
    arch_map[46] = 'EM_H8_300'  # Renesas H8/300
    arch_map[50] = 'EM_IA_64'  # HP/Intel IA-64
    arch_map[62] = 'EM_X86_64'  # AMD x86-64
    arch_map[22] = 'EM_S390'  # IBM S/390
    arch_map[76] = 'EM_CRIS'  # Axis Communications 32-bit embedded processor
    arch_map[88] = 'EM_M32R'  # Renesas M32R
    arch_map[89] = 'EM_MN10300'  # Panasonic/MEI MN10300, AM33
    arch_map[92] = 'EM_OPENRISC'  # OpenRISC 32-bit embedded processor
    arch_map[93] = 'EM_ARCOMPACT'  # ARCompact processor
    arch_map[94] = 'EM_XTENSA'  # Tensilica Xtensa Architecture
    arch_map[106] = 'EM_BLACKFIN'  # ADI Blackfin Processor
    arch_map[110] = 'EM_UNICORE'  # UniCore-32
    arch_map[113] = 'EM_ALTERA_NIOS2'  # Altera Nios II soft-core processor
    arch_map[140] = 'EM_TI_C6000'  # TI C6X DSPs
    arch_map[164] = 'EM_HEXAGON'  # QUALCOMM Hexagon
    arch_map[167] = 'EM_NDS32'  # Andes Technology compact code size embedded RISC processor family
    arch_map[183] = 'EM_AARCH64'  # ARM 64 bit
    arch_map[188] = 'EM_TILEPRO'  # Tilera TILEPro
    arch_map[189] = 'EM_MICROBLAZE'  # Xilinx MicroBlaze
    arch_map[191] = 'EM_TILEGX'  # Tilera TILE-Gx
    arch_map[195] = 'EM_ARCV2'  # ARCv2 Cores
    arch_map[243] = 'EM_RISCV'  # RISC-V
    arch_map[247] = 'EM_BPF'  # Linux BPF - in-kernel virtual machine
    arch_map[252] = 'EM_CSKY'  # C-SKY
    arch_map[21569] = 'EM_FRV'  # 0x5441 Fujitsu FR-V

    # 0x9026, This is an interim value that we will use until the committee comes up with a final number.
    arch_map[36902] = 'EM_ALPHA'

    # 0x9041, Bogus old m32r magic number, used by old tools.
    arch_map[36929] = 'EM_CYGNUS_M32R'
    # 0x9916, SW 64 bit
    arch_map[39190] = 'EM_SW64'
    # 0xA390, This is the old interim value for S/390 architecture.
    arch_map[41872] = 'EM_S390_OLD'
    # 0xbeef, Also Panasonic/MEI MN10300, AM33
    arch_map[48879] = 'EM_CYGNUS_MN10300'

    arch = arch_map.get(machine_code, None)
    return arch
